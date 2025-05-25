def atuar(comando, objeto):
    print("verificando se é um comando para as luzes de emergência")

    if objeto in ["luzes de emergência"]:
        print(f"{comando.capitalize()} {objeto}")
        return True
    
    return False