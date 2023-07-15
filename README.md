<div align="right">
  
![Estado: Estable](https://img.shields.io/badge/Estado-Estable-brightgreen) 
![Versión: 3.3](https://img.shields.io/badge/Versión-3.3-blue) 
[![Autor: Lic. Ricardo MONLA](https://img.shields.io/badge/Autor-Lic.%20Ricardo%20MONLA-orange)](mailto:rmonla@gmail.com)

</div>

# rmTextToSpeech

El código lee un archivo JSON que contiene preguntas y respuestas. Luego, utiliza la biblioteca gTTS para convertir cada pregunta y respuesta en archivos de audio en formato mp3. Los archivos de audio se guardan con nombres secuenciales.

## archivo.json
~~~json
[
    {
        "pregunta": "¿Qué es la inteligencia artificial",
        "respuesta": "La inteligencia artificial (IA) es una rama de la informática que busca desarrollar algoritmos y sistemas que puedan realizar tareas que requieren inteligencia humana, como la toma de decisiones, el reconocimiento de patrones, el aprendizaje y la resolución de problemas."
    },
    {
        "pregunta": "¿Cómo está afectando la IA al mercado laboral?",
        "respuesta": "La IA está cambiando el mercado laboral al automatizar tareas repetitivas y procesos complejos. Esto puede llevar a la eliminación de algunos trabajos, pero también puede crear nuevos empleos en áreas relacionadas con la IA, como la programación, la ingeniería de datos y la ciberseguridad."
    }
]
~~~

## archivo.py
~~~python
# Copyright (c) 2023 Lic. Ricardo MONLA, rmonla@gmail.com
# Este código está licenciado bajo la licencia de código libre. 


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
    
    # Concatenar pregunta y respuesta
    texto_pregunta_respuesta = f"{texto_pregunta}. {texto_respuesta}"

    # Crear objeto gTTS con la pregunta y respuesta concatenadas
    tts_pregunta_respuesta = gTTS(text=texto_pregunta_respuesta, lang='es')

    # Guardar archivo de audio con el nombre secuencial
    nombre_archivo = "pregunta_{:02d}.mp3".format(contador)
    tts_pregunta_respuesta.save(nombre_archivo)
    
    # Incrementar contador
    contador += 1
~~~
