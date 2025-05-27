from time import sleep

def atuar(comando, objeto):
    print("verificando se é um comando para o piloto automático")

    sleep(2)

    sucesso = False
    if comando in ["ativar", "desativar", "ligar", "desligar"] and objeto == "piloto automático":        
        sucesso = True

    return sucesso