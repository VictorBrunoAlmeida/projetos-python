# Bem vindo ao jogo de Papel, Pedra ou Tesoura

# ========================================
# PLACAR:
# Você: 0
# Computador: 0
# ========================================

# Escolha seu lance:
# 0 - Papel | 1 - Pedra | 2 - Tesoura

# Sua jogada: PAPEL
# Jogada do computador: PEDRA
# Você venceu!

# Jogar novamente? 0 - SIM | 1 - NÃO

import random
import os
import time


def limpar_tela():
    os.system("cls")
    
def escolha_computador():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def escolha_jogador():
    escolha = input("Escolha uma das opções: (0 - Pedra) (1 - papel) (2 - tesoura) ")
    while True:
        if escolha not in ["0", "1", "2"]:
            print("Opção inválida, tente novamente")
            escolha = input("Escolha uma das opções: (0 - Pedra) (1 - papel) (2 - tesoura) ")
            continue
        elif escolha == "0":
            return "você escolheu pedra"
        elif escolha == "1":
            return "você escolheu papel"
        elif escolha == "2":
            return "você escolheu tesoura"
             
def determinar_vencedor(escolha_jogador, escolha_computador):
    if escolha_computador == escolha_jogador:
        return "empate"
    elif (escolha_computador == "pedra" and escolha_jogador == "papel") or (escolha_computador == "papel" and escolha_jogador == "tesoura") or (escolha_computador == "tesoura" and escolha_jogador == "pedra"):
        return "jogador!"
    else:
        return "computador!"
    
def jogar_novamente():
    while True:
        resposta = input("você quer continuar? (0 - SIM) | (1- NÃO)")
        if resposta == "0":
            return True
        elif resposta == "1":
            return False 
        else: 
            print("opção inválida, tente novamente")
        
def exibir_placar(placar_jogador, placar_computador):
    print("==========================================")
    print(f"PLACAR: ")
    print(f"Você: {placar_jogador}")
    print(f"Computador: {placar_computador}")
    print("==========================================")
    
def exibir_resultado_final(placar_jogador, placar_computador):
    limpar_tela()
    print("# ========================================")
    print("# PLACAR FINAL:")
    print(f"# Você: {placar_jogador}")
    print(f"# Computador: {placar_computador}")
    print("# ========================================")
    
    if placar_computador > placar_jogador:
        print("Você perdeu!")
    elif placar_computador < placar_jogador:
        print("Você venceu!")
    else:
        print("O jogo terminou em empate!")
        
    print("obrigado por jogar!!")
    
placar_jogador = 0
placar_computador = 0
jogando = True

while jogando:
    limpar_tela()
    print("==========================================")
    print("BEM VINDO AO JOGO DE PAPEL, PEDRA OU TESOURA!")
    print("==========================================")
    
    jogada_jogador = escolha_jogador()
    jogada_computador = escolha_computador()
    
    print(f"sua jogada: {jogada_jogador.upper()}")
    print(f"jogada do computador: {jogada_computador.upper()}")
    
    resultado = determinar_vencedor(jogada_jogador, jogada_computador)
    
    if resultado == "jogador":
        print("você venceu")
        placar_jogador += 1
    elif resultado == "computador":
        print("você perdeu")
        placar_computador += 1
    else:
        print("empate!")
       
 
    jogando = jogar_novamente()
    

exibir_resultado_final(placar_jogador, placar_computador)
    




    
  
    
  




