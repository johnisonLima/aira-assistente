from time import sleep

def atuar(comando, objeto):
    sucesso = False

    print("verificando se é um comando para as luzes de emergência")

    sleep(2)
    
    if comando in ["ativar", "desativar", "ligar", "desligar"] and objeto == "luzes de emergência":        
        sucesso = True

    return sucesso