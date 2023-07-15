from gtts import gTTS
import json

# Leer archivo json con el texto
with open('rmTextToSpeech.json', 'r') as f:
    texto = json.load(f)['texto']

# Crear objeto gTTS con el texto
tts = gTTS(text=texto, lang='es')

# Guardar archivo de audio
tts.save('audio.mp3')
