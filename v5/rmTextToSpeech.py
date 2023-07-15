import json
import pyttsx3

# Leer archivo json con las preguntas y respuestas
with open('rmTextToSpeech.json', 'r') as f:
    preguntas = json.load(f)

# Crear variable contador
contador = 1

# Inicializar engine de pyttsx3
engine = pyttsx3.init()

# Definir voz de hombre latinoamericano
voices = engine.getProperty('voices')
voice_id = "spanish-latin-am"
for voice in voices:
    if voice.languages[0] == 'es-419' and voice.id == voice_id:
        engine.setProperty('voice', voice.id)
        break

# Iterar sobre las preguntas y crear archivo de audio para cada pregunta
for pregunta in preguntas:
    texto_pregunta = pregunta['pregunta']
    texto_respuesta = pregunta['respuesta']
    
    # Unir pregunta y respuesta
    texto_pregunta_respuesta = f"{texto_pregunta}. {texto_respuesta}"
    
    # Decir pregunta y respuesta con pyttsx3
    # engine.say(texto_pregunta_respuesta)
    
    # Guardar archivo de audio con el nombre secuencial
    nombre_archivo = f"pregunta_{contador}.mp3"
    engine.save_to_file(texto_pregunta_respuesta, nombre_archivo)
    
    # Incrementar contador
    contador += 1

# Cerrar engine de pyttsx3
engine.runAndWait()
