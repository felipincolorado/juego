# Herramientas

## corregir_tono.py — quitar el tono amarillo de imágenes generadas

Mide la dominante cálida en una zona que debería ser neutra (por defecto, la franja del borde de una imagen generada sobre fondo gris #808080) y la elimina de toda la imagen.

```
pip install pillow numpy
python herramientas/corregir_tono.py imagen.png --borde 4
python herramientas/corregir_tono.py carpeta/ -o carpeta_neutro/ --borde 4
python herramientas/corregir_tono.py mapa.png --zona x,y,ancho,alto
python herramientas/corregir_tono.py imagen.png --mundo-gris --fuerza 0.6
python herramientas/corregir_tono.py personaje.png --borde 4 --blancos 0.85   (además, blancos crema → blancos neutros)
python herramientas/corregir_tono.py personaje_sin_fondo.png --solo-blancos 0.85   (personajes que ChatGPT ya entrega sin fondo)
```

`--blancos` actúa sólo sobre píxeles claros y poco saturados (camisas, linos, encajes): corrige el «blanco crema» que pinta ChatGPT sin tocar piel ni colores.

Informa del índice de amarillo antes y después. Conserva la transparencia. Ver `diseno/ENCARGOS-ELENCO-TANDA-2.md` §2.
