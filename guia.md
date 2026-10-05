# Guía de transcripción y subtitulado

Esta guía documenta el flujo completo para generar subtítulos a partir de un archivo de audio, usando herramientas gratuitas: **Google Colab** (con faster-whisper), **Aegisub** y **Handbrake**.

## Herramientas

- **[Google Colab](https://colab.research.google.com/)** — para ejecutar faster-whisper y transcribir/traducir el audio.
- **[Aegisub](https://aegisub.org/)** — para editar y sincronizar los subtítulos.
- **Editor de video** (Kdenlive, DaVinci Resolve, u otro) — para armar el video final con el audio.
- **[Handbrake](https://handbrake.fr/)** — para quemar los subtítulos en el video.

---

## 1. Preparación del archivo

Si el audio que vas a subtitular ya tiene un guion/transcripción disponible en su fuente original, podés saltar directo al paso 3 (edición en Aegisub) usando ese texto como base.

Si no hay guion disponible, seguí con el paso 2.

## 2. Transcripción y traducción con Whisper (Google Colab)

1. Abrí el notebook `template_transcripcion_traduccion_v2.py` en Google Colab.
2. Activá la aceleración por GPU: `Entorno de ejecución > Cambiar tipo de entorno de ejecución > GPU`.
3. Corré la celda de instalación de librerías (solo una vez por sesión).
4. Subí tu archivo de audio con el botón de carga.
5. Elegí la tarea:
   - **transcribe**: pasa el audio a texto en el mismo idioma original (recomendado, más preciso).
   - **translate**: traduce el audio directamente a inglés.
   - **transcribe_es**: transcribe forzando español (puede fallar más en audios con ruido o voces superpuestas; si falla, mejor transcribir en el idioma original y traducir el texto por separado con un traductor de texto).
6. Ejecutá la celda de transcripción. El resultado se guarda como `.srt` en la carpeta `audio_transcription/`.
7. Descargá el `.srt` generado.

> 💡 Tip: si necesitás traducir el texto ya transcripto a otro idioma, podés pasarlo por un modelo de traducción de texto (DeepL, o un LLM) en vez de traducir el audio directamente — suele dar mejores resultados en audios difíciles.

## 3. Edición y sincronización en Aegisub

1. Instalá Aegisub desde su [sitio oficial](https://aegisub.org/).
2. Abrí tu video: `Video > Abrir video...`
3. Cargá el audio por separado para mayor precisión: `Audio > Abrir archivo de audio...`
4. Importá el archivo `.srt` generado en el paso anterior.
5. Ajustá los tiempos de cada línea según la onda de audio visible en la interfaz.
6. Editá el texto y el estilo (fuente, tamaño, color) según prefieras.
7. Guardá el archivo final en `.srt` o `.ass`.

## 4. Armado del video

1. Importá tu imagen/video base y el audio en tu editor de video.
2. Sincronizá el audio con la imagen.
3. Agregá efectos de fade si querés (opcional).
4. Exportá el video final.

## 5. Exportación con subtítulos incrustados (Handbrake)

1. Abrí Handbrake y hacé clic en "Abrir fuente", seleccionando el video exportado en el paso anterior.
2. Agregá los subtítulos en una pista separada: importá el archivo `.srt`/`.ass` y activá la opción **"Burn into video"** para que queden quemados en el video final.
3. Exportá el resultado.

---

## Consejos generales

- Guardá siempre una copia de seguridad del notebook antes de modificarlo, para no perder la plantilla original.
- Para audios con mucho ruido de fondo o voces superpuestas, la transcripción en el idioma original suele ser más confiable que traducir directo con Whisper — después podés traducir el texto ya limpio con otra herramienta.
- Revisá siempre la transcripción automática antes de darla por buena: los modelos de reconocimiento de voz pueden cometer errores, especialmente con acentos, jerga o audio de baja calidad.
