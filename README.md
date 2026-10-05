# PainPeko-Subs

Plantilla y guía para transcribir y traducir audio automáticamente usando **faster-whisper** en **Google Colab**, con flujo de sincronización de subtítulos en **Aegisub** y exportación final con **Handbrake**.

Creado y documentado por **PainPeko**.

---

## 🎯 Qué hace esto

Convierte un archivo de audio en subtítulos sincronizados (`.srt`), listos para editar y quemar en video. Todo el proceso corre en la nube (Colab), sin necesidad de instalar nada pesado en tu computadora.

## 🛠️ Herramientas usadas

- **[Google Colab](https://colab.research.google.com/)** — ejecuta faster-whisper para la transcripción/traducción.
- **[Aegisub](https://aegisub.org/)** — edición y sincronización fina de subtítulos.
- **[Handbrake](https://handbrake.fr/)** — para quemar los subtítulos en el video final.

## 🚀 Cómo usarlo

1. Abrí `template_transcripcion_traduccion_v2.py` en Google Colab (subilo como notebook nuevo).
2. Activá la GPU: `Entorno de ejecución > Cambiar tipo de entorno de ejecución > GPU`.
3. Corré las celdas en orden:
   - Instalar librerías.
   - Subir tu archivo de audio.
   - Elegir la tarea (transcribir, traducir a inglés, o transcribir forzando español).
   - Ejecutar y descargar el `.srt` generado.
4. Importá el `.srt` en Aegisub para ajustar tiempos y estilo.
5. Usá Handbrake para incrustar los subtítulos en el video final.

Guía completa paso a paso en [`docs/guia.md`](docs/guia.md).

## 📄 Licencia

Este proyecto está bajo licencia **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**.
Podés usar, modificar y compartir este método libremente — solo pedimos que **cites la fuente/autoría original**.

## 📬 Contacto

Dudas o sugerencias: Discord `@pekopain_` · [PainPeko en YouTube](https://www.youtube.com/channel/UCAUEhquiC1FEghYyyfkxidQ)

## 📺 Video tutorial

_(próximamente)_
