def cria_tabuleiro():
    tabuleiro = [['_', '_', '_'],
                 ['_', '_', '_'],
                 ['_', '_', '_']]
    return tabuleiro


def render_tabuleiro(tabuleiro):
    print(str(tabuleiro[0]))
    print(str(tabuleiro[1]))
    print(str(tabuleiro[2]))
    print()


def atualiza_tabuleiro(tabuleiro, linha, coluna, simbolo):
    if check_free(tabuleiro, linha, coluna):
        tabuleiro[linha][coluna] = simbolo
        render_tabuleiro(tabuleiro)
        #tem_vencedor(tabuleiro, simbolo)
    else:
        print("Posição Ocupada \n")

    return tabuleiro


def check_free(tabuleiro, linha, coluna):
    return True if tabuleiro[linha][coluna] == '_' else False


def tem_vencedor(tabuleiro, simbolo):
    if (tabuleiro[0][0] == tabuleiro[2][0] != '_' and tabuleiro[1][0] == tabuleiro[0][0] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[0][1] == tabuleiro[2][1] != '_' and tabuleiro[1][1] == tabuleiro[0][1] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[0][2] == tabuleiro[2][2] != '_' and tabuleiro[1][2] == tabuleiro[0][2] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[0][0] == tabuleiro[0][1] != '_' and tabuleiro[0][0] == tabuleiro[0][2] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[1][0] == tabuleiro[1][1] != '_' and tabuleiro[1][2] == tabuleiro[1][0] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[2][0] == tabuleiro[2][1] != '_' and tabuleiro[2][2] == tabuleiro[2][0] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[0][0] == tabuleiro[1][1] != '_' and tabuleiro[2][2] == tabuleiro[0][0] != '_'):
        print(simbolo + " vencedor")
        return True
    elif (tabuleiro[0][2] == tabuleiro[1][1] != '_' and tabuleiro[2][0] == tabuleiro[1][1] != '_'):
        print(simbolo + " vencedor")
        return True
