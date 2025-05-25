def atuar(comando, objeto):
    if objeto == "transponder no modo 7700":
        print(f"{comando.capitalize()} {objeto}")
        return True
    return False