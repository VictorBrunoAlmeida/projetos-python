import os 
import random


move_list = ["pedra", "papel", "tesoura"]
player_count = 0 
computer_count = 0

def main_print():
    print("================================================================")
    print("PLACAR:")
    print(f"você: {player_count}")
    print(f"computador: {computer_count}")
    print("\n")
    print("Escolha o seu lance: ")
    print("1- pedra | 2- papel | 3- tesoura")
    
def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [1, 2, 3]:
                raise
            return move_list[player_move - 1]
        
        except Exception as e: 
            print(e)
            
def select_winner(p_move, c_move):
    global player_count, computer_count
    
    if p_move == "papel":
        if c_move == "pedra":
            player_count += 1
            return "p"
    
        elif c_move == "tesoura":
            computer_count += 1
            return "c"
        
        else:
            return "d"
            

    if p_move == "tesoura":
        if c_move == "papel":
            player_count += 1
            return "p"
    
        elif c_move == "pedra":
            computer_count += 1
            return "c"
        
        else:
            return "d"
        
    if p_move == "pedra":
        if c_move == "tesoura":
            player_count += 1
            return "p"
    
        elif c_move == "papel":
            computer_count += 1
            return "c"
        
        else:
            return "d"
            
again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)
    
    print("=========================")
    print(f"sua jogada: {player_move.upper()}")
    print(f"jogada do computador: {computer_move.upper()}")
    
    if winner == "p":
        print("Você ganhou!")
    elif winner == "c":
        print("Você perdeu!")
    else:
        print("Empatou!")
        
    while True:
        print("quer jogar novamente? 0 - Sim | 1 - Não")
        
        try:    
            next = int(input())
            if next == 0:
                break
            elif next == 1:
                again = 0
                break
        except Exception as y:
                print("comando inválido, tente novamente")
            
    
    os.system("cls")