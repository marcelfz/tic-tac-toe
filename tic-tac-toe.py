######################################################
# Programação Funcional / Programação I (2022/2)
# EP2 - Jogo da Velha
# Nome: Marcelo Ferraz de Araújo Costa Filho
# Matrícula:
######################################################

import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Marcelo Ferraz" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def aleatorio(tabuleiro):
    posicao = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if tabuleiro[posicao] == " ":
        return posicao
    else:
        return aleatorio(tabuleiro)


def jogada_computador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador 

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia: 
    DIGITE AQUI A ESTRATÉGIA USADA PELO COMPUTADOR PARA TENTAR VENCER O JOGADOR
    """
    if simboloComputador == "X":
        simboloJogador = "O"
    elif simboloComputador == "O":
        simboloJogador = "X"
    
    
    posicao = aleatorio(tabuleiro[:])

    if tabuleiro[1] == tabuleiro[2] == simboloComputador and tabuleiro[3] == " ":
        return 3
    elif tabuleiro[4] == tabuleiro[5] == simboloComputador and tabuleiro[6] == " ":
        return 6
    elif tabuleiro[7] == tabuleiro[8] == simboloComputador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[2] == tabuleiro[3] == simboloComputador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[5] == tabuleiro[6] == simboloComputador and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[8] == tabuleiro[9] == simboloComputador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[1] == tabuleiro[3] == simboloComputador and tabuleiro[2] == " ":
        return 2
    elif tabuleiro[4] == tabuleiro[6] == simboloComputador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[7] == tabuleiro[9] == simboloComputador and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[1] == tabuleiro[4] == simboloComputador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[2] == tabuleiro[5] == simboloComputador and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[3] == tabuleiro[6] == simboloComputador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[7] == tabuleiro[4] == simboloComputador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[8] == tabuleiro[5] == simboloComputador and tabuleiro[2] == " ":
        return 2
    elif tabuleiro[9] == tabuleiro[6] == simboloComputador and tabuleiro[3] == " ":
        return 3
    elif tabuleiro[7] == tabuleiro[1] == simboloComputador and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[8] == tabuleiro[2] == simboloComputador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[9] == tabuleiro[3] == simboloComputador and tabuleiro[6] == " ":
        return 6
    elif tabuleiro[7] == tabuleiro[3] == simboloComputador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[9] == tabuleiro[1] == simboloComputador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[1] == tabuleiro[5] == simboloComputador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[3] == tabuleiro[5] == simboloComputador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[9] == tabuleiro[5] == simboloComputador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[7] == tabuleiro[5] == simboloComputador and tabuleiro[3] == " ":
        return 3
    

    elif tabuleiro[1] == tabuleiro[2] == simboloJogador and tabuleiro[3] == " ":
        return 3
    elif tabuleiro[4] == tabuleiro[5] == simboloJogador and tabuleiro[6] == " ":
        return 6
    elif tabuleiro[7] == tabuleiro[8] == simboloJogador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[2] == tabuleiro[3] == simboloJogador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[5] == tabuleiro[6] == simboloJogador and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[8] == tabuleiro[9] == simboloJogador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[1] == tabuleiro[3] == simboloJogador and tabuleiro[2] == " ":
        return 2
    elif tabuleiro[4] == tabuleiro[6] == simboloJogador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[7] == tabuleiro[9] == simboloJogador and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[1] == tabuleiro[4] == simboloJogador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[2] == tabuleiro[5] == simboloJogador and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[3] == tabuleiro[6] == simboloJogador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[7] == tabuleiro[4] == simboloJogador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[8] == tabuleiro[5] == simboloJogador and tabuleiro[2] == " ":
        return 2
    elif tabuleiro[9] == tabuleiro[6] == simboloJogador and tabuleiro[3] == " ":
        return 3
    elif tabuleiro[7] == tabuleiro[1] == simboloJogador and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[8] == tabuleiro[2] == simboloJogador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[9] == tabuleiro[3] == simboloJogador and tabuleiro[6] == " ":
        return 6
    elif tabuleiro[7] == tabuleiro[3] == simboloJogador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[9] == tabuleiro[1] == simboloJogador and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[1] == tabuleiro[5] == simboloJogador and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[3] == tabuleiro[5] == simboloJogador and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[9] == tabuleiro[5] == simboloJogador and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[7] == tabuleiro[5] == simboloJogador and tabuleiro[3] == " ":
        return 3
    else:
        return posicao
    


def escolha_jogador(msg = "Você escolhe X ou O: "):

    """
    Parâmetros: 
    msg: mensagem do input 

    Retorno:
    Retorna a letra escolhida pelo usuário em maiúsculo
    """
    valor = input(msg)
    if valor == "X" or valor == "x":
        return "X"
    elif valor == "O" or valor == "o":
        return "O"
    else:
        print("Valor inválido")
        return escolha_jogador()


def jogada_jogador(tabuleiro, msg = "Você deve escolher um número de 1 a 9: "):

    """
    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    
    Retorno: 
    Retorna a posição decidida pelo jogador(um número)

    """
    try:
        opcao = int(input(msg))
        if tabuleiro[opcao] == " " and opcao > 0 and opcao < 10:
            return opcao
        else:
            print("opção inválida, tente novamente.")
            return jogada_jogador(tabuleiro)  
    except:
        print("opção inválida, tente novamente.")
        return jogada_jogador(tabuleiro)     
        

def verifica_empate(tabuleiro, i = 1):
    
    """
    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro

    Retorno: 
    retorna True se empatou e False se não empatou
    
    """

    if i < len(tabuleiro):
        if tabuleiro[i] == " ":
            return False
        else:
            return verifica_empate(tabuleiro, i + 1)
    else:
        return True 

def vitoria(t):
    """
    Parâmetro:
    tabuleiro: lista de tamanho 10 representando o tabuleiro   

    Retorno:
    Retorna o símbolo do ganhador se houver ganhadores, empate ou se o jogo continua 

    """


    if (t[1] == t[2] == t[3] == "X") or (t[4] == t[5] == t[6] == "X"):
        return "X"
    elif (t[7] == t[8] == t[9] == "X") or (t[1] == t[5] == t[9] == "X"):
        return "X"
    elif (t[3] == t[5] == t[7] == "X") or (t[3] == t[6] == t[9] == "X"):
        return "X"
    elif (t[2] == t[5] == t[8] == "X") or (t[1] == t[4] == t[7] == "X"):  
        return "X"
    
    elif (t[1] == t[2] == t[3] == "O") or (t[4] == t[5] == t[6] == "O"):
        return "O"
    elif (t[7] == t[8] == t[9] == "O") or (t[1] == t[5] == t[9] == "O"):
        return "O"
    elif (t[3] == t[5] == t[7] == "O") or (t[3] == t[6] == t[9] == "O"):
        return "O"
    elif (t[2] == t[5] == t[8] == "O") or (t[1] == t[4] == t[7] == "O"):  
        return "O"

    elif verifica_empate(t) ==  True:
        return "Empate"
    else:
        return "Continua"

def print_tabuleiro(tabuleiro):
    limpaTela()
    print(f" {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}")
    print("---|---|---")
    print(f" {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}")
    print("---|---|---")
    print(f" {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}")


def jogada(vez, computador, jogador, tabuleiro):
    """
    Parâmetros:
    Vez: representa o símbolo de quem é a vez de jogar(computador ou o player)
    computador: símbolo do computador
    jogador: símbolo do jogador
    tabuleiro: lista de tamanho 10 representando o tabuleiro 

    Retorno:
    Não retorna nada.

    """
    print_tabuleiro(tabuleiro[:])
    

    if vez == computador:
        opcao_computador = jogada_computador(tabuleiro[:], computador)
        tabuleiro[opcao_computador] = computador 
    elif vez == jogador:
        opcao_jogador = jogada_jogador(tabuleiro[:])
        tabuleiro[opcao_jogador] = jogador
    
    resultado = vitoria(tabuleiro[:])
    print_tabuleiro(tabuleiro[:])
    if resultado == computador:
        print("O computador ganhou.")
        jogar_novamente()
    elif resultado == jogador:
        print("Você ganhou.")
        jogar_novamente()
    elif resultado == "Empate":
        print("Deu velha")
        jogar_novamente()
    else:
        jogada("O" if vez == "X" else "X", computador, jogador, tabuleiro[:])
    
def jogar_novamente(msg = "Você quer jogar de novo [S/N]? "):
    """
    Parâmetros:
    msg: Pergunta se quer continuar
    
    """
    valor = input(msg)
    if valor == "S" or valor == "s":
        return main()
    elif valor == "N" or valor == "n":
        exit()
    else:
        print("Valor inválido")
        return jogar_novamente()


def main():
    """
    determina o símbolo do jogador e computador e também de quem vai jogar primeiro. 
    
    """
    limpaTela()
    simbolo_jogador = escolha_jogador()
    if simbolo_jogador == "X":
        simbolo_computador = "O"
    elif simbolo_jogador == "O":
        simbolo_computador = "X"
    
    t = [' '] * 10
    
    primeiro = random.choice(["X", "O"])
    jogada(primeiro, simbolo_computador, simbolo_jogador, t[:])


if __name__ == "__main__":
    main()
