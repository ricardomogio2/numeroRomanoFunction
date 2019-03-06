def numeroRomano(numeroInput):
    numeroU = numeroInput.upper()

    listaNumeroStr = list(numeroU)
    posicao = 0
    soma = 0
    numerosPrimarios = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for posicao in range(0, len(listaNumeroStr)):
        if posicao == 0:
            soma += numerosPrimarios.get(listaNumeroStr[posicao])
        if posicao > 0:
            if numerosPrimarios.get(listaNumeroStr[posicao]) <= numerosPrimarios.get(listaNumeroStr[posicao - 1]):
                soma += numerosPrimarios.get(listaNumeroStr[posicao])
            elif numerosPrimarios.get(listaNumeroStr[posicao]) > numerosPrimarios.get(listaNumeroStr[posicao - 1]):
                soma -= 2 * numerosPrimarios.get(listaNumeroStr[posicao - 1])
                soma += numerosPrimarios.get(listaNumeroStr[posicao])

    return soma
