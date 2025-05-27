from inicializador_modelos import *
from transcritor import *
from nltk import word_tokenize, corpus
from threading import Thread

import pyaudio
import wave
import numpy as np
import secrets
import os
import json
import random
import re

import pyttsx3

from dispositivos import luzes_puoso
from dispositivos import luzes_emergencia
from dispositivos import piloto_automatico
from dispositivos import assistente
from dispositivos import combustivel
from dispositivos import torre_de_controle
from dispositivos import transponder

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
    
    palavras_de_parada.discard('de')

    configuracao = None

    if iniciado:
        try:
            with open(CONFIG, "r", encoding="utf-8") as arquivo:
                configuracao = json.load(arquivo)

                arquivo.close()
        except Exception as e:
            print(f"Erro carregando a configuração: {str(e)}")

            iniciado = False

    return iniciado, processador, modelo, gravador, palavras_de_parada, configuracao

def clara_diz(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def obter_intensidade_audio(dados):
    if not dados:
        return 0.0

    audio_array = np.frombuffer(dados, dtype=np.int16)

    if audio_array.size == 0:
        return 0.0
    
    audio_array = audio_array.astype(np.float32)

    rms = np.sqrt(np.mean(audio_array ** 2))

    return rms

def capturar_fala_quando_houver_som(gravador):
    gravacao = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM, input=True, frames_per_buffer=AMOSTRAS)

    try:
        while True:
            dados = gravacao.read(AMOSTRAS, exception_on_overflow=False)
            volume = obter_intensidade_audio(dados)

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
    gravacao = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM, input=True, frames_per_buffer=AMOSTRAS)

    fala = []
    blocos_silenciosos = 0

    try:
        # print("Esperando som...")

        while True:
            dados = gravacao.read(AMOSTRAS, exception_on_overflow=False)
            volume = obter_intensidade_audio(dados)

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
        gravacao.stop_stream()

def escutar_comando_ativacao():
    iniciado, processador, modelo, gravador, palavras_de_parada, configuracao = iniciar()

    if not iniciado:
        return

    clara_diz("Aguardando palavra de ativação...")
    print("Pressione Ctrl+C para parar.")

    try:
        while True:
            if detectar_ativacao(gravador, modelo, processador, configuracao):
                while True:
                    processar_comando_usuario(gravador, modelo, processador, palavras_de_parada, configuracao)
                    # clara_diz("Aguardando próximo comando...")  
    except KeyboardInterrupt:
        print("Interrompido pelo usuário.")

def detectar_ativacao(gravador, modelo, processador, configuracao):
    fala = capturar_fala_com_silencio(gravador)

    ativar_assistente = configuracao["ativar_assistente"]

    gravado, arquivo_fala = gravar_fala(fala, gravador)

    if not gravado:
        return False

    transcricao = transcrever_fala(carregar_fala(arquivo_fala), modelo, processador)
    print(f"Você disse: {transcricao}")
    
    os.remove(arquivo_fala)

    if ativar_assistente in transcricao.lower():
        clara_diz("Assistente ativada!")
        return True
    
    return False

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
   
def remover_palavras_de_parada(transcricao, palavras_de_parada):
    comando = []

    tokens = word_tokenize(transcricao)
    for token in tokens:
        if token not in palavras_de_parada:
            comando.append(token)

    return comando

def validar_comando(comando, acoes):
    comando_str = " ".join(comando).lower()

    for acao in acoes:
        nome_acao = acao["nome"].lower()

        for objeto in acao["objetos"]:
            nome_objeto = objeto.lower()

            padrao = fr"\b{nome_acao}\b\s+\b{nome_objeto}\b"

            if re.search(padrao, comando_str):
                return True, nome_acao, nome_objeto

    return False, None, None

def validar_modo(comando, modos):
    comando_str = " ".join(comando).lower()

    for modo in modos:
        nome_modo = modo["nome"].lower()
        
        padrao = fr"\b{nome_modo}\b"

        if re.search(padrao, comando_str):
            acoes = modo.get("acoes", [])
            return True, nome_modo, acoes

    return False, None, []

def responder_execucao_invalida(configuracao):
    respostas = configuracao.get("execucao_invalida", [])
    if respostas:
        resposta_escolhida = random.choice(respostas)
        return resposta_escolhida["resposta"]
    
    return "Desculpe, não entendi."

def processar_comando_usuario(gravador, modelo, processador, palavras_de_parada, configuracao):
    fala = capturar_fala_com_silencio(gravador)

    gravado, arquivo_fala = gravar_fala(fala, gravador)

    if not gravado:
        return
    
    carregar_audio_processado = carregar_fala(arquivo_fala)

    transcricao = transcrever_fala(carregar_audio_processado, modelo, processador)
    comando = remover_palavras_de_parada(transcricao, palavras_de_parada)

    print(f"Você disse: {transcricao}")
    print(f"Comando de voz: {comando}")
    os.remove(arquivo_fala)

    executar_acao_ou_modo(comando, configuracao)

def executar_atividade(acao, objeto, atuadores):   
    for atuador in atuadores:
        atuacao = Thread(target=atuador["atuacao"], args=[acao, objeto])
        atuacao.start()

def configurar_atuadores():
    atuadores = []

    atuadores.append({
        "nome": "luzes de puoso",
        "atuacao": luzes_puoso.atuar
    })
    atuadores.append({
        "nome": "luzes de emergência",
        "atuacao": luzes_emergencia.atuar
    })
    atuadores.append({
        "nome": "piloto automático",
        "atuacao": piloto_automatico.atuar
    })
    atuadores.append({
        "nome": "assistente",
        "atuacao": assistente.atuar
    })
    atuadores.append({
        "nome": "combustível",
        "atuacao": combustivel.atuar
    })    
    atuadores.append({
        "nome": "torre de controle",
        "atuacao": torre_de_controle.atuar
    })
    atuadores.append({
        "nome": "transponder",
        "atuacao": transponder.atuar
    })
    return atuadores

def executar_acao_ou_modo(comando, configuracao):
    atuadores = configurar_atuadores()
    
    acao_valido, acao, objeto = validar_comando(comando, configuracao["acoes"])

    modo_valido, nome_modo, acoes_do_modo = validar_modo(comando, configuracao["modos"])

    if acao_valido:
        clara_diz(f"Executando ação: {acao} {objeto}")
        executar_atividade(acao, objeto, atuadores)

    elif modo_valido:
        clara_diz(f"{nome_modo} ativado. Executando as seguintes ações:")
        for acao in acoes_do_modo:
            nome_acao = acao["nome"]
            objeto = acao["objetos"]
            clara_diz(f"{nome_acao} {objeto}")
    else:
       clara_diz(responder_execucao_invalida(configuracao))

if __name__ == "__main__":    
    escutar_comando_ativacao()
