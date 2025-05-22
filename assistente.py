from inicializador_modelos import *
from transcritor import *
from nltk import word_tokenize, corpus

import pyaudio
import wave
import audioop
import secrets
import os
import json
import time

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

CAMINHO_AUDIO_FALA = "temp/"
CONFIG = "config.json"
FORMATO = pyaudio.paInt16
CANAIS = 1
AMOSTRAS = 1024
LIMIAR_VOLUME = 500 
DURACAO_MAX = 5
IDIOMA_CORPUS = "portuguese" 

def iniciar():
    gravador = pyaudio.PyAudio()

    iniciado, processador, modelo = iniciar_modelo(MODELO)
    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))

    configuracao = None

    if iniciado:
        try:
            with open(CONFIG, "r", encoding="utf-8") as arquivo:
                configuracao = json.load(arquivo)

                arquivo.close()
        except Exception as e:
            print(f"erro carregando a configuração: {str(e)}")

            iniciado = False

    return iniciado, processador, modelo, gravador

def capturar_fala_quando_houver_som(gravador):
    gravacao = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM,
                           input=True, frames_per_buffer=AMOSTRAS)

    try:
        while True:
            dados = gravacao.read(AMOSTRAS, exception_on_overflow=False)
            volume = audioop.rms(dados, 2)

            if volume > LIMIAR_VOLUME:
                # print("Som detectado! Gravando...")
                fala = [dados]

                for _ in range(0, int(TAXA_AMOSTRAGEM / AMOSTRAS * DURACAO_MAX) - 1):
                    fala.append(gravacao.read(AMOSTRAS, exception_on_overflow=False))

                return fala 
    finally:
        gravacao.stop_stream()
        gravacao.close()

def capturar_fala_com_silencio(gravador, max_silencio=30):
    stream = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM,
                           input=True, frames_per_buffer=AMOSTRAS)

    fala = []
    blocos_silenciosos = 0

    try:
        # print("Esperando som...")

        while True:
            dados = stream.read(AMOSTRAS, exception_on_overflow=False)
            volume = audioop.rms(dados, 2)

            if volume > LIMIAR_VOLUME:
                fala.append(dados)
                blocos_silenciosos = 0 
            else:
                if fala:  
                    blocos_silenciosos += 1
                    fala.append(dados)

            if fala and blocos_silenciosos >= max_silencio:
                break

        return fala

    finally:
        stream.stop_stream()

def gravar_fala(fala, gravador):
    gravado, arquivo = False, f"{CAMINHO_AUDIO_FALA}{secrets.token_hex(32)}.wav"

    try:
        wav = wave.open(arquivo, "wb")
        wav.setnchannels(CANAIS)
        wav.setsampwidth(gravador.get_sample_size(FORMATO))
        wav.setframerate(TAXA_AMOSTRAGEM)
        wav.writeframes(b''.join(fala))
        wav.close()

        # print("Áudio salvo:", arquivo)
        gravado = True
    except Exception as e:
        print(f"Erro ao gravar áudio: {e}")
        return
    
    return gravado, arquivo

def carregar_fala(caminho_audio):
    audio, amostragem = torchaudio.load(caminho_audio)
    if audio.shape[0] > 1:
        audio = torch.mean(audio, dim=0, keepdim=True)

    adaptador_amostragem = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)
    audio = adaptador_amostragem(audio)

    return audio.squeeze()
   
def clara_diz(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def escutar_comando_ativacao():
    iniciado, processador, modelo, gravador = iniciar()

    if iniciado:
        clara_diz("Aguardando palavra de ativação...")
        print("Pressione Ctrl+C para parar.")

        while True:
            try:
                # fala = capturar_fala_quando_houver_som(gravador)
                fala = capturar_fala_com_silencio(gravador)
                gravado, arquivo_fala = gravar_fala(fala, gravador)

                if gravado:
                    transcricao = transcrever_fala(carregar_fala(arquivo_fala), modelo, processador)
                    print(f"Você disse: {transcricao}")
                    os.remove(arquivo_fala)

                    if "oi clara" in transcricao.lower():
                        clara_diz("Assistente ativada!")                        
                        break

            except KeyboardInterrupt:
                print("Interrompido pelo usuário.")
                break

if __name__ == "__main__":    
    escutar_comando_ativacao()
