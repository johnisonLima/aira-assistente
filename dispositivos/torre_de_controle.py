from time import sleep

def atuar(comando, objeto):
    sucesso = False

    # print("verificando se é um comando para a torre de controle")

    sleep(2)
    
    if comando in ["acionar"] and objeto == "torre de controle":        
        print("A atuação da torre de controle foi executada com sucesso.")
        sucesso = True

    return sucesso