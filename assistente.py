import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

def amelia_diz(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando_ativacao():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Aguardando palavra de ativação...")
        amelia_diz("Aguardando palavra de ativação...")
        while True:
            audio = reconhecedor.listen(fonte)
            try:
                texto = reconhecedor.recognize_google(audio, language="pt-BR").lower()
                print(f"Você disse: {texto}")
                if "ok amélia" in texto:
                    print("Assistente ativada!")
                    amelia_diz("Assistente ativada!")
                    return  
            except sr.UnknownValueError:
                continue

if __name__ == "__main__":
    ouvir_comando_ativacao()