from time import sleep

def atuar(comando, objeto):
    sucesso = False

    # print("verificando se é um comando para as luzes de pouso")

    sleep(2)
    
    if comando in ["ativar", "desativar", "ligar", "desligar"] and objeto == "luzes de pouso":           
        print("A atuação das luzes de pouso foi executada com sucesso.")     
        sucesso = True

    return sucesso