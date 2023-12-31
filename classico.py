import util

def start_game(simbolos):
    print(simbolos[0] + " Jogador 1 \n" + simbolos[1] + " Jogador 2 \n")
    tabuleiro = util.cria_tabuleiro()
    util.render_tabuleiro(tabuleiro)
    jogada(0, simbolos, tabuleiro)

def jogada(round, simbolos, tabuleiro):
    print("Turno do jogador " + str(round + 1))
    linha = out_of_bounds(int(input("Linha: ")))
    coluna = out_of_bounds(int(input("Coluna: ")))
    new_tab = util.atualiza_tabuleiro(tabuleiro, linha, coluna, simbolos[round])
    if util.tem_vencedor(new_tab, simbolos[round]):
        exit()
    novo_round = muda_round(round)
    jogada(novo_round, simbolos, new_tab)


def muda_round(round):
    if round == 0:
        round += 1
    else:
        round -= 1
    return round

def out_of_bounds(numero):
    if numero > 2:
        return 2
    elif numero < 0:
        return 0
    else:
        return numero