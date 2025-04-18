import os
import locale

carros = [
    {"marca": "chevrolet", "modelo": "Tracker", "valor_diario": 120},
    {"marca": "chevrolet", "modelo": "Onix", "valor_diario": 90},
    {"marca": "chevrolet", "modelo": "Spin", "valor_diario": 150},
    {"marca": "Hyundai ", "modelo": "Tucson", "valor_diario": 120},
    {"marca": "Hyundai ", "modelo": "HB20", "valor_diario": 85},
    {"marca": "Fiat", "modelo": "Uno ", "valor_diario": 60},
    {"marca": "Fiat", "modelo": "Mobi ", "valor_diario": 70},
    {"marca": "Fiat", "modelo": "Pulse", "valor_diario": 30}
]

carros_alugados = []

print("="*40)
print("seja bem vindo a locadora de carros")
print("="*40)

def formatar_moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Define o locale para o Brasil
    return locale.currency(valor, grouping=True, symbol=True)  # Formata o valor como moeda brasileira

#mostrar lista de carros
def mostrar_lista_carros(lista_de_carros):
    for i, carro in enumerate(lista_de_carros):
        print(
                f" [{i}]{carro['marca']} {carro['modelo']} - R$ {carro['valor_diario']} / dia")
        
mostrar_lista_carros(carros)

while True:
    os.system("cls")
    print("="*40)
    print("bem vindo à locadora de carros")
    print("="*40)
    print("O que deseja fazer?")
    print("0- Mostrar lista de carros | 1- alugar um carro | 2- devolver um carro")
    escolha = int(input("Digite o número da opção: "))
    
    os.system("cls")
    if escolha == 0: 
       mostrar_lista_carros(carros)
    
    #alugarde carro
    elif escolha == 1:
        mostrar_lista_carros(carros)
    
        try:
            print("escolha o código do carro que deseja alugar: ")
            cod_carro = int(input())
            if 0 <= cod_carro < len(carros):
                dias = int(input("por quantos dias você deseja alugar o carro?"))
                valor_aluguel = carros[cod_carro]["valor_diario"] * dias
                valor_aluguel_formatted = formatar_moeda(valor_aluguel)  # Formata o valor como moeda brasileira
                os.system("cls")
        
                print(f"você escolheu o carro {carros[cod_carro]['marca']}{carros[cod_carro]['modelo']} por {dias} dias")
                print(f"o aluguel totalizaria {valor_aluguel_formatted} reais. Gostaria de alugar?")
        
                confirma = input("(sim) | (não) ").strip().lower()
                
                while confirma not in ["sim", "não"]:
                    print("comando inválido, digite novamente")
                    confirma = input("(sim) | (não) ").strip().lower()
                    
                        
                if confirma == "sim":
                    carros_alugados.append(carros.pop(cod_carro))
                elif confirma == "não":
                    print("operação cancelada")
                       
            else:
                print("código inválido. tente novamente")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
      
    
    #devolver carro
    elif escolha == 2:
        if len(carros_alugados) == 0:
            print("não há carros para devolver")
        elif len(carros_alugados) > 0:
            print("segue a lista de carros alugados:")
            mostrar_lista_carros(carros_alugados)  
                 
            try:
                cod_devolver = int(input("Digite o código do carro que deseja devolver: "))
                if 0 <= cod_devolver < len(carros_alugados):
                    carro_devolvido = carros_alugados.pop(cod_devolver)
                    carros.append(carro_devolvido)
                    print(f"Obrigado por devolver o carro {carro_devolvido['marca']} {carro_devolvido['modelo']}.")
                else:
                    print("Código inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
            
    
    #continuar ou cancelar operação
    print("")
    print("===================")
    continuar = input("Deseja continuar? (sim|não)").strip().lower()
    while continuar not in ['sim', 'não']:
        print("comando inválido, tente novamente")
        continuar = input("Deseja continuar? (sim|não)").strip().lower()
    if continuar == "sim":
        continue 
    elif continuar == "não":
      print("obrigado pro utilizar o nosso sistema")
      break  
        
  
    
        
    
    
    