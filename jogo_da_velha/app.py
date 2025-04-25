import os
import random


#resetar o game
def reset():
    
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],     
    ]
    return board
    
    
#printar o jogo a cada jogada
def print_board(board): 
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    


#pegar a jogada do usuario
def get_user_move(board):
    try:
        #pedir ao usuario a jogada
        linha = int(input("digite a linha que deseja jogar (1, 2 ou 3) "))
        coluna = int(input("digite a coluna que deseja jogar(1, 2 ou 3) "))
        
        
        #converter os valores de 1-3 para 0-2
        linha -= 1
        coluna -= 1
        
        #verificar se as coordenadas estão dentro do tabuleiro no intervalor de 0-2
        if linha < 0 or linha > 2 or coluna < 0 or coluna >2 :
            print("Posição invalida, os intervalos devem estar entre 1-3")
            return get_user_move(board)# retorna a função para uma nova entrada do usuário
        
        #verifica se a posição está vazia
        
        if board[linha][coluna] != " ":
            print("posição já está ocupada! marque uma opção que não está ocupada")
            return get_user_move(board) #retorna a função para uma nova entrada do usuário
        
        #retornar as coordenadas corretas
        return linha, coluna
    except Exception as e:
        print("Entrada inválida, tente novamente")
        return get_user_move(board) #retorna a função para uma nova entrada do usuário


#realizar o movimento do usuario 
def make_move(board, linha, coluna, simbolo):
    #coloca o simbolo na posição indicada
    board[linha][coluna]= simbolo  
    
    #retorna o tabuleiro atualizado
    return board
    

#pegar a jogada do computador
def computer_move(board, simbolo_computador, simbolo_jogador):
    # 1. Verifica se pode vencer na próxima jogada
    # 2. Bloqueia o jogador caso ele possa vencer na próxima jogada
    # 3. Tenta ocupar o centro se estiver disponível
    # 4. Tenta ocupar os cantos disponíveis
    # 5. Escolhe qualquer posição disponível
    
    #percorre linha e coluna e verifica quais estão vazias e adiciona na lista
    for linha in range(3):
        for coluna in range(3):
            if board[linha][coluna] == " ":
                #tenta a jogada
                board[linha][coluna] = simbolo_computador 
                #verifica se a função retorna o simbolo do computador
                if check_winner(board) == simbolo_computador:
                    
                    board[linha][coluna]= " "
                    return (linha, coluna)
            
                board[linha][coluna]= " "
     # 2. Bloqueia o jogador caso ele possa vencer na próxima jogada
    for linha in range(3):
        for coluna in range(3):
            if board[linha][coluna] == " ":   
                board[linha][coluna] = simbolo_jogador
                if check_winner(board) == simbolo_jogador:          
                    
                    board[linha][coluna] = " "
                    return(linha, coluna)
                
                board[linha][coluna]= " "
        
    # 3. Tenta ocupar o centro se estiver disponível
    if board[1][1] == " ":
        return (1, 1)
    
  # 4. Tentar ocupar os cantos
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    cantos_disponiveis = [canto for canto in cantos if board[canto[0]][canto[1]] == " "]
    if cantos_disponiveis:
        return random.choice(cantos_disponiveis)
            
     # 5. Ocupar qualquer lado disponível
    lados = [(0, 1), (1, 0), (1, 2), (2, 1)]
    lados_disponiveis = [lado for lado in lados if board[lado[0]][lado[1]] == " "]
    if lados_disponiveis:
        return random.choice(lados_disponiveis)
            
    return None              
    
   
#verificar se há um vencedor
def check_winner(board):
    
    #verificar os valores das linhas
    for linha in range(3):
        if board[linha][0] == board[linha][1] == board[linha][2] and board[linha][0] != " ":
            return board[linha][0] #retorna o simbolo vencedor 
        
    #verificar os valores das colunas
    for coluna in range(3):
        if board[0][coluna] == board[1][coluna] == board[2][coluna] and board[0][coluna] != " ":
            return board[0][coluna] #retorna o simbolo vencedor
        
    #verificar os valores da diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0] #retorna o simbolo vencedor
    
    #verificar os valores da diagonal 
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2] #retorna o simbolo vencedor
    
    #se nenhuma condição de vitória for encontrada
    return None
    
    
def check_tie(board):

    #verificar se todos os espaços estão ocupados
    for linha in range(3):
        for coluna in range(3):
            if board[linha][coluna] == " ":
                return False #retorna False se ainda existem espaços vazios
    return True #retorna True se todos os espaços estão ocupados

def quem_comeca():
    #retorna True se o jogador começa e false se o computador começa
    return random.choice([True, False])

#iniciar o jogo
def play_game():
    #inicializar o tabuleiro( precisa guardar o valor retornado)
    board = reset()
    
    #definir os simbolos do jogador e do computador
    simbolo_jogador = "X"
    simbolo_computador = "O"
    
    #determinar quem começa:
    vez_jogador = quem_comeca()
    if vez_jogador == True:
        print("Você começa!!")
    else:
        print("O computador começa!!")
        
   # Aguardar input do usuário antes de iniciar o jogo
    input("\nPressione Enter para iniciar o jogo...")
             
    #controlar se o jogo está ativo;
    jogo_ativo = True
    
    #loop principal do jogo
    while jogo_ativo:
        # Limpar a tela antes de mostrar o tabuleiro atualizado
        os.system("cls" if os.name == "nt" else "clear")
        
        # Reimprime o título do jogo a cada vez
        print("===========================")
        print("JOGO DA VELHA")
        print("===========================")
        print("Você (X) vs Computador (O)")
        print()
        
        
        print_board(board)#exibe o tabuleiro a cada jogada
      
       
        #definir a vez do jogador
        if vez_jogador:
            print("sua vez (X)")
            linha,coluna = get_user_move(board)
            board = make_move(board, linha, coluna, simbolo_jogador)
         
        #vez do computador   
        else:
            print("vez do computador (O)")
            posicao = computer_move(board, simbolo_computador, simbolo_jogador)
            if posicao:
                linha, coluna = posicao
                board = make_move(board, linha, coluna, simbolo_computador)
                
        #verificar se há um vencedor ou se há um empate
        vencedor = check_winner(board)
        if vencedor:
            print_board(board)
            if vencedor =="X": 
                print("Você venceu!")
            elif vencedor =="O":
                print("O computador venceu!")
            jogo_ativo = False
        
        elif check_tie(board):
            print_board(board)
            print("Empate!")
            jogo_ativo = False
            
        else:
            #só muda de jogador de o jogo continuar
            vez_jogador = not vez_jogador
            
        #Jogar novamente
    try:
        jogar_novamente = input("Deseja jogar novamente? (s/n)")
        if jogar_novamente.lower() == "s":
            play_game()
        else:
            print("Obrigado por utilizar o nosso jogo!")
    except Exception as e:
            print("Entrada inválida, tente novamente")

            

    
            
def main():
    print("===========================")
    print("bem-vindo ao jogo da velha")
    print("===========================")
    print("Você será (X) e o computador será (O)")
    play_game()

if __name__ == "__main__":
    main()
        
        
            
        
        
        
    