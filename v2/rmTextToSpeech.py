from gtts import gTTS
import json

# Leer archivo json con las preguntas y respuestas
with open('rmTextToSpeech.json', 'r') as f:
    preguntas = json.load(f)

# Crear variable contador
contador = 1

# Iterar sobre las preguntas y crear archivo de audio para cada pregunta
for pregunta in preguntas:
    texto_pregunta = pregunta['pregunta']
    texto_respuesta = pregunta['respuesta']
    
    # Crear objeto gTTS con la pregunta
    tts_pregunta = gTTS(text=texto_pregunta, lang='es')

    # Guardar archivo de audio con el nombre secuencial
    nombre_archivo = f"pregunta_{contador}.mp3"
    tts_pregunta.save(nombre_archivo)
    
    # Incrementar contador
    contador += 1
