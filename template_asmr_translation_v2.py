# -*- coding: utf-8 -*-
"""Template_Transcripcion_Traduccion_v2.ipynb

Plantilla actualizada para transcripción y traducción de audio usando
faster-whisper (más rápido que openai/whisper original) sobre Google Colab.

Autor: [tu nombre/alias acá]
"""

from google.colab import drive
drive.mount('/content/drive')

"""
# 🎬 Plantilla de transcripción y traducción de audio (v2)

---

**🚨 Antes de correr nada:** activá la aceleración por GPU en
`Entorno de ejecución > Cambiar tipo de entorno de ejecución > GPU`
"""

#@title ⚙️ 1. Instalar librerías (correr una sola vez por sesión)
!pip install -q faster-whisper stable-ts

"""## 📁 2. Subir el archivo de audio

Corré esta celda y usá el botón para subir tu archivo (.mp3, .wav, etc.)
directamente desde tu computadora — no hace falta escribir el nombre a mano.
"""

from google.colab import files

uploaded = files.upload()
audio_filename = list(uploaded.keys())[0]
print(f"Archivo cargado: {audio_filename}")

"""## ⚙️ 3. Elegí la tarea

- **transcribe**: pasa el audio a texto en el MISMO idioma original (recomendado, más preciso).
- **translate**: traduce el audio directamente a inglés.
- **transcribe_es**: transcribe forzando salida en español (Whisper suele fallar más acá con audios con susurros o ruido; si falla, mejor transcribir en el idioma original y traducir el texto aparte).
"""

task_mode = "transcribe" #@param ["transcribe", "translate", "transcribe_es"]
model_size = "large-v3" #@param ["medium", "large-v2", "large-v3"]

"""## ▶️ 4. Ejecutar transcripción/traducción

Genera el archivo .srt en la carpeta `audio_transcription/`.
"""

if task_mode == "transcribe":
    !stable-ts "{audio_filename}" --task transcribe --model {model_size} --output_dir audio_transcription --output_format srt

elif task_mode == "translate":
    !stable-ts "{audio_filename}" --task translate --model {model_size} --output_dir audio_transcription --output_format srt

elif task_mode == "transcribe_es":
    !stable-ts "{audio_filename}" --task transcribe --language es --model {model_size} --output_dir audio_transcription --output_format srt

print("\n✅ Listo. Revisá la carpeta 'audio_transcription' en el panel de archivos de la izquierda.")

"""## 📄 5. Ver el resultado rápido en pantalla (opcional)"""

import os

srt_name = os.path.splitext(audio_filename)[0] + ".srt"
srt_path = os.path.join("audio_transcription", srt_name)

if os.path.exists(srt_path):
    with open(srt_path, encoding="utf-8") as f:
        print(f.read())
else:
    print("No se encontró el .srt esperado, revisá el nombre del archivo en la carpeta audio_transcription/")

"""## 🎙️ (Opcional) Grabar audio directo desde el navegador

Si preferís grabar en vivo en vez de subir un archivo, corré esta celda.
Requiere permiso de micrófono en el navegador.
"""

#@title 🎙️ Grabar audio (opcional)
from IPython.display import HTML, Audio
from google.colab.output import eval_js
from base64 import b64decode
from scipy.io.wavfile import read as wav_read, write as wav_write
import io
import ffmpeg

AUDIO_HTML = """
<script>
var my_div = document.createElement("DIV");
var my_btn = document.createElement("BUTTON");
var t = document.createTextNode("Press to start recording");
my_btn.appendChild(t);
my_div.appendChild(my_btn);
document.body.appendChild(my_div);

var base64data = 0;
var reader;
var recorder, gumStream;
var recordButton = my_btn;

var handleSuccess = function(stream) {
  gumStream = stream;
  recorder = new MediaRecorder(stream);
  recorder.ondataavailable = function(e) {
    var url = URL.createObjectURL(e.data);
    var preview = document.createElement('audio');
    preview.controls = true;
    preview.src = url;
    document.body.appendChild(preview);
    reader = new FileReader();
    reader.readAsDataURL(e.data);
    reader.onloadend = function() {
      base64data = reader.result;
    }
  };
  recorder.start();
};

recordButton.innerText = "Recording... press to stop";
navigator.mediaDevices.getUserMedia({audio: true}).then(handleSuccess);

function toggleRecording() {
  if (recorder && recorder.state == "recording") {
      recorder.stop();
      gumStream.getAudioTracks()[0].stop();
      recordButton.innerText = "Saving the recording... pls wait!"
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var data = new Promise(resolve=>{
  recordButton.onclick = ()=>{
    toggleRecording();
    sleep(2000).then(() => {
      resolve(base64data.toString());
    });
  }
});
</script>
"""

def get_audio():
    display(HTML(AUDIO_HTML))
    data = eval_js("data")
    binary = b64decode(data.split(',')[1])

    process = (
        ffmpeg
        .input('pipe:0')
        .output('pipe:1', format='wav')
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=True, overwrite_output=True)
    )
    output, err = process.communicate(input=binary)

    riff_chunk_size = len(output) - 8
    q = riff_chunk_size
    b = []
    for i in range(4):
        q, r = divmod(q, 256)
        b.append(r)
    riff = output[:4] + bytes(b) + output[8:]

    sr, audio = wav_read(io.BytesIO(riff))
    return audio, sr

# Para usar: descomentar las siguientes líneas
# audio, sr = get_audio()
# wav_write('record.wav', sr, audio)
# audio_filename = 'record.wav'
# (después volvé a correr el paso 4 con este nuevo audio_filename)
