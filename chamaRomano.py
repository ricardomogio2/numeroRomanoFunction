import numeroRomanoFunction

def mainPrograma():
    numeroEmRomano = input("Digite o numero romano a ser convertido: ").upper()
    print("O numero romano {} equivale a {}".format(numeroEmRomano, numeroRomanoFunction.numeroRomano(numeroEmRomano)))


if __name__ == '__main__' :
    mainPrograma()