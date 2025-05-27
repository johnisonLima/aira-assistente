from time import sleep
import signal
import os

def atuar(comando, objeto):
    print("verificando se é um comando para a assistente")

    sleep(2)

    sucesso = False
    if comando in ["desativar", "desligar"] and objeto == "assistente":      

        os.kill(os.getpid(), signal.SIGINT)
  
        sucesso = True

    return sucesso