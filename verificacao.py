# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# for i, voice in enumerate(voices):
#     print(f"{i}: {voice.name} - {voice.id}")


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Exibe e seleciona a voz correta
for voice in voices:
    if 'pt-br' in voice.languages or 'brazil' in voice.name.lower():
        print(f"Nome: {voice.name}, ID: {voice.id}, Idioma: {voice.languages}")
        engine.setProperty('voice', voice.id)  # <- aqui está o ID real da voz
        break

engine.say("Olá, tudo bem? Eu estou falando em português.")
engine.runAndWait()

print(engine.getProperty('driverName'))  # Exibe o mecanismo ativo (sapi5, nsss, espeak, etc.)

# sudo apt install espeak-ng