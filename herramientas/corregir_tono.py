#!/usr/bin/env python3
"""Corrige la dominante cálida (amarilla/naranja) de imágenes generadas.

Método: se toma una zona que DEBERÍA ser neutra (gris o blanca) y se calcula
cuánto se desvía cada canal. Esa desviación se elimina de toda la imagen
multiplicando cada canal por una ganancia (balance de blancos por referencia).

Formas de indicar la zona neutra:
  --borde 4          usa una franja del 4 % alrededor de la imagen (ideal si se
                     generó sobre fondo gris neutro #808080 o blanco).
  --zona x,y,an,al   rectángulo en píxeles (por ejemplo, un lino blanco o una
                     muestra gris pintada a propósito).
  --mundo-gris       sin referencia: supone que la media de toda la imagen es
                     gris. Menos fiable en ilustraciones muy coloridas.

Uso:
  python corregir_tono.py MAP-01_v1.png --borde 3
  python corregir_tono.py carpeta_entrada/ -o carpeta_salida/ --borde 4
  python corregir_tono.py personaje.png --zona 40,40,120,120 --fuerza 0.8

Requisitos: Python 3, Pillow y numpy (pip install pillow numpy).
"""
import argparse
import os
import sys

import numpy as np
from PIL import Image

EXTENSIONES = (".png", ".jpg", ".jpeg", ".webp")


def indice_amarillo(rgb):
    """Positivo = cálido/amarillo; negativo = frío/azul. Escala 0-255."""
    r, g, b = rgb
    return (r + g) / 2.0 - b


def mascara_borde(alto, ancho, porcentaje):
    banda = max(1, int(round(min(alto, ancho) * porcentaje / 100.0)))
    m = np.zeros((alto, ancho), dtype=bool)
    m[:banda, :] = True
    m[-banda:, :] = True
    m[:, :banda] = True
    m[:, -banda:] = True
    return m


def mascara_zona(alto, ancho, zona):
    x, y, an, al = zona
    m = np.zeros((alto, ancho), dtype=bool)
    m[max(0, y):min(alto, y + al), max(0, x):min(ancho, x + an)] = True
    return m


def corregir(img, modo, valor, fuerza):
    tiene_alfa = img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info)
    rgba = img.convert("RGBA")
    datos = np.asarray(rgba).astype(np.float64)
    rgb, alfa = datos[..., :3], datos[..., 3]
    alto, ancho = alfa.shape

    if modo == "borde":
        m = mascara_borde(alto, ancho, valor)
    elif modo == "zona":
        m = mascara_zona(alto, ancho, valor)
    else:
        m = np.ones((alto, ancho), dtype=bool)
    m &= alfa > 0
    # Ignora sombras profundas y luces quemadas: no informan del balance.
    lum = rgb.mean(axis=2)
    m &= (lum > 20) & (lum < 245)
    if modo == "borde" and m.sum() >= 50:
        # Si el personaje toca el borde, descarta lo que no se parece al fondo
        # dominante (pelo, ropa): sólo quedan los píxeles cercanos a la mediana.
        mediana = np.median(rgb[m], axis=0)
        m &= np.abs(rgb - mediana).sum(axis=2) < 24
    if m.sum() < 50:
        raise ValueError("La zona de referencia tiene muy pocos píxeles útiles.")

    media = rgb[m].mean(axis=0)
    objetivo = media.mean()
    ganancia = objetivo / np.maximum(media, 1e-6)
    ganancia = 1.0 + (ganancia - 1.0) * fuerza

    salida = np.clip(rgb * ganancia, 0, 255)
    nueva_media = (rgb[m] * ganancia).mean(axis=0)
    out = np.dstack([salida, alfa]).astype(np.uint8)
    imagen = Image.fromarray(out, "RGBA")
    if not tiene_alfa:
        imagen = imagen.convert("RGB")
    return imagen, media, nueva_media, ganancia


def neutralizar_blancos(imagen, fuerza):
    """Lleva hacia el gris neutro sólo los píxeles claros y poco saturados
    (linos, camisas, encajes pintados en crema). No toca la piel ni los colores."""
    tiene_alfa = imagen.mode == "RGBA"
    rgba = imagen.convert("RGBA")
    datos = np.asarray(rgba).astype(np.float64)
    rgb, alfa = datos[..., :3], datos[..., 3]
    lum = rgb.mean(axis=2, keepdims=True)
    sat = (rgb.max(axis=2) - rgb.min(axis=2))[..., None]
    peso = np.clip((lum - 165.0) / 55.0, 0, 1) * np.clip(1.0 - sat / 55.0, 0, 1) * fuerza
    salida = np.clip(rgb + (lum - rgb) * peso, 0, 255)
    out = np.dstack([salida, alfa]).astype(np.uint8)
    res = Image.fromarray(out, "RGBA")
    return res if tiene_alfa else res.convert("RGB")


def amarillo_de_blancos(imagen):
    rgb = np.asarray(imagen.convert("RGB")).astype(np.float64)
    m = rgb.mean(axis=2) > 200
    if m.sum() < 50:
        return float("nan")
    c = rgb[m]
    return float(((c[:, 0] + c[:, 1]) / 2 - c[:, 2]).mean())


def procesar(ruta, destino, args):
    img = Image.open(ruta)
    if args.zona:
        modo, valor = "zona", tuple(int(v) for v in args.zona.split(","))
    elif args.mundo_gris:
        modo, valor = "mundo", None
    else:
        modo, valor = "borde", args.borde
    imagen, antes, despues, ganancia = corregir(img, modo, valor, args.fuerza)
    print(f"{os.path.basename(ruta)}: referencia RGB {antes.round(1)} "
          f"(amarillo {indice_amarillo(antes):+.1f}) -> {despues.round(1)} "
          f"(amarillo {indice_amarillo(despues):+.1f}); ganancias {ganancia.round(3)}")
    if args.blancos > 0:
        previo = amarillo_de_blancos(imagen)
        imagen = neutralizar_blancos(imagen, args.blancos)
        print(f"   blancos: amarillo {previo:+.1f} -> {amarillo_de_blancos(imagen):+.1f}")
    imagen.save(destino)


def main():
    p = argparse.ArgumentParser(description="Quita la dominante cálida de imágenes generadas.")
    p.add_argument("entrada", help="Archivo o carpeta")
    p.add_argument("-o", "--salida", help="Archivo o carpeta de salida (por defecto, sufijo _neutro)")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--borde", type=float, default=4.0, help="Franja de referencia en %% (por defecto 4)")
    g.add_argument("--zona", help="Rectángulo neutro x,y,ancho,alto en píxeles")
    g.add_argument("--mundo-gris", action="store_true", help="Sin referencia: media de toda la imagen")
    p.add_argument("--fuerza", type=float, default=1.0, help="0 = nada, 1 = corrección completa")
    p.add_argument("--blancos", type=float, default=0.0,
                   help="0-1: además, neutraliza blancos pintados en crema (linos, camisas). Recomendado 0.8")
    args = p.parse_args()

    if os.path.isdir(args.entrada):
        salida = args.salida or args.entrada.rstrip("/\\") + "_neutro"
        os.makedirs(salida, exist_ok=True)
        archivos = [f for f in sorted(os.listdir(args.entrada)) if f.lower().endswith(EXTENSIONES)]
        for f in archivos:
            nombre, _ = os.path.splitext(f)
            procesar(os.path.join(args.entrada, f), os.path.join(salida, nombre + ".png"), args)
    else:
        nombre, _ = os.path.splitext(args.entrada)
        procesar(args.entrada, args.salida or nombre + "_neutro.png", args)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)
