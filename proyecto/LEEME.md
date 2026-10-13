# Salverna · Paquete de proyecto

Todo lo que hace falta para programar el juego. **Orden de lectura:**

1. [`canon/CANON.md`](<canon/CANON.md>): mundo, elenco, calendario, secretos y reglas de estilo.
2. [`sistemas/SISTEMAS.md`](<sistemas/SISTEMAS.md>): mecánicas con fórmulas y parámetros.
3. [`datos/ESQUEMA.md`](<datos/ESQUEMA.md>): formato de los datos, variables y condiciones.
4. `datos/`: los datos en YAML. Su exportación a JSON está en `datos/json/` y es lo que debe cargar el motor.
5. `guion/`: versión legible de los textos, en ES y EN, para revisar sin abrir los datos.
6. Arte e interfaz: `../diseno/` (especificación de pantallas v3, componentes, tamaños e inventario de imágenes) y el archivo de Figma «JUEGO» (marcos v4).

## Herramientas

```
pip install pyyaml pillow numpy
python herramientas/compilar_datos.py        # valida, exporta a JSON y genera el guion
python herramientas/corregir_tono.py img.png --solo-blancos 0.85
```

## Estado

Ver [`../produccion/PLAN-MAESTRO.md`](<../produccion/PLAN-MAESTRO.md>). Semana 1 escrita como porción vertical, pendiente de revisión del usuario.
