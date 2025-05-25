def atuar(comando, objeto):
    print("verificando se é um comando para as luzes de pouso")

    if objeto in ["luzes de pouso"]:
        print(f"{comando.capitalize()} {objeto}")
        return True
    
    return False