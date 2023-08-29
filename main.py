import util
import classico
import os

def main():
    print("--- JOGO DA VELHA ---")
    input("Pressione qualquer tecla para começar: ")
    simbolo1 = input("Símbolo do jogador 1? ")
    simbolo2 = input("Símbolo do jogador 2? ")
    classico.start_game([simbolo1, simbolo2])


main()
'''tab1 = util.cria_tabuleiro()
util.render_tabuleiro(tab1)

util.atualiza_tabuleiro(tab1, 0,0, 'X')
util.atualiza_tabuleiro(tab1, 1,0, 'X')
util.atualiza_tabuleiro(tab1, 2,0, 'O')
util.atualiza_tabuleiro(tab1, 2,1, 'O')
util.atualiza_tabuleiro(tab1, 2,0, 'X')
util.atualiza_tabuleiro(tab1, 2,2, 'O')'''