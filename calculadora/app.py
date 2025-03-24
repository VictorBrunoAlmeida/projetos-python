import os 

#funções matemáticas
def somar_valores(valor1, valor2):
    return valor1 + valor2

def multiplicar_valores(valor1,valor2):
    return valor1 * valor2

def subtrair_valores(valor1, valor2):
    return valor1 - valor2

def dividir_valores(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Divisão por zero não é permitida, burro!"
    
def exponenciar_valores(valor1, valor2):
    return valor1 ** valor2

#dicionário de operações
operacoes = {"0":"Soma"
             ,"1":"Subtração"
             ,"2":"Multiplicação"
             ,"3":"Divisão" 
             ,"4":"Exponenciação"
             }

#função principal
def calculadora():
    while True:
        os.system("cls")
        
        print("Seja bem vindo a calculadora")
        print("Escolha a operação que deseja realizar")
        
        for chave, valor in operacoes.items():
            print(f"{chave} : {valor}")
        print("5 : Sair")
        escolha = input("digite o número da operação: ")

        #opção de sair
        if escolha == "5":
            print("vlw flw otario")
            break
    
        #validar se a escolha é válida
        if escolha not in operacoes.keys():
            print("Opção inválida, tente novamente")
            input("\nPressione Enter para continuar...")
            continue
            
        #validar se os valores são numéricos
        try: 
            valor1 = float(input("digite o primeiro valor: "))
            valor2 = float(input("digite o segundo valor: "))
        except ValueError:
            print("Você digitou um valor inválido, tente novamente")
            input("\nPressione Enter para continuar...")
            continue
        
        #executar a operação
        if escolha == "0":
            resultado = somar_valores(valor1, valor2)
        elif escolha == "1":
            resultado = subtrair_valores(valor1, valor2)
        elif escolha == "2":
            resultado = multiplicar_valores(valor1, valor2)
        elif escolha == "3":
            resultado = dividir_valores(valor1, valor2)
        elif escolha == "4":
            resultado= exponenciar_valores(valor1, valor2)
        
        #mostrar o resultado da operação
        print(f"O resultado da operação é: {resultado}")
        sair = input("\nPressione 'Enter' para continuar... ou 'S' para sair ")
        
        #verificar se o usuário deseja sair
        if sair == "S".lower().replace("s", "sair"):
            print("TMJ padrin")
            break
        
calculadora()
    

     

