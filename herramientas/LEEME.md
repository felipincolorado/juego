# Herramientas

## corregir_tono.py — quitar el tono amarillo de imágenes generadas

Mide la dominante cálida en una zona que debería ser neutra (por defecto, la franja del borde de una imagen generada sobre fondo gris #808080) y la elimina de toda la imagen.

```
pip install pillow numpy
python herramientas/corregir_tono.py imagen.png --borde 4
python herramientas/corregir_tono.py carpeta/ -o carpeta_neutro/ --borde 4
python herramientas/corregir_tono.py mapa.png --zona x,y,ancho,alto
python herramientas/corregir_tono.py imagen.png --mundo-gris --fuerza 0.6
```

Informa del índice de amarillo antes y después. Conserva la transparencia. Ver `diseno/ENCARGOS-ELENCO-TANDA-2.md` §2.
