from time import sleep

def atuar(comando, objeto):
    sucesso = False

    # print("verificando se é um comando para o transponder")

    sleep(2)
    
    if comando in ["ativar"] and objeto == "transponder":        
        print("A atuação do transponder foi executada com sucesso.")
        sucesso = True

    return sucesso