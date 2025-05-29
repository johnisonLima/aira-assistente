from time import sleep

def atuar(comando, objeto):
    # print("verificando se é um comando para o combustível")

    sleep(2)

    sucesso = False

    if comando in ["checar nível de", "verificar nível de"] and objeto == "combustível":           
        print("A atuação do combustível foi executada com sucesso.")    
        sucesso = True

    return sucesso