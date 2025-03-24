import os

#locadora de carros



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

# resposta = ["sim", "nao"]
carros_alugados = []
while True:
    os.system("cls")

    print("="*40)
    print("seja bem vindo a locadora de carros")
    print("="*40)

    print("O que deseja fazer?")
    escolha = input("0- Mostrar opções de carro | 1 - alugar um carro | 2 - devolver um carro | 3 - sair: ")

    os.system("cls")
    if escolha == "0":
        print("carros disponiveis:\n")
        if carros:
            for i, carro in enumerate(carros):
                print(
                    f" {carro['marca']} {carro['modelo']} - R$ {carro['valor_diario']} / dia")
        else:
            print("Nenhum carro disponível no momento.")
        input("\nPressione Enter para voltar ao menu...")

    # alugar carro
    elif escolha == "1":
        for i, carro in enumerate(carros):
            print(
                f"[{i}] - {carro['marca']} {carro['modelo']} - R$ {carro['valor_diario']} / dia")



        # selecionar o carro, dias e calcular valor total
        try:
            codigo_do_carro = int(input("\n===>Escolha o código do carro: "))
            if 0 <= codigo_do_carro < len(carros):
                dias = int(input("===>Por quantos dias deseja alugar? "))
                carro_selecionado = carros[codigo_do_carro]
                valor_total = carro_selecionado["valor_diario"] * dias

                print(
                    f"\nVocê escolheu o {carro_selecionado['marca']}{carro_selecionado['modelo']} por {dias} dias")
                print(
                    f"O aluguel totalizaria R${valor_total}. Deseja alugar?")
                confirmar = str(input("(Sim) | (Não) ")).strip().lower()

                if confirmar == "sim":
                        carros_alugados.append(carros.pop(codigo_do_carro))
                        print("carro alugado com sucesso!!")
                else:
                    print("\noperação cancelada")
                    
            else:
                print("código inválido")
        except ValueError:
            print("Você digitou um valor inválido, tente novamente")
            
            
        continuar  = input("\nDeseja continuar? (sim | não)").strip().lower()
        if continuar == "sim":
            continue
        elif continuar == "não":
            print("Obrigado por utilizar o nosso sistema!")
            break  
        else:
            print("Opção inválida, tente novamente")
    
        
    # devolver carro
    elif escolha == "2":
        if carros_alugados:
            print("\nsegue a lista de carros alugados. Qual você deseja devolver?")
            for i, carro in enumerate(carros_alugados):
                print(f"[{i}] {carro['marca']}{carro['modelo']}")
            try:
                codigo_devolucao= int(input("Escolha o código do carro que deseja devolver\n"))
                if 0 <= codigo_devolucao < len(carros_alugados):
                    carro_devolvido = carros_alugados.pop(codigo_devolucao)
                    carros.append(carro_devolvido)
                    print("Obrigado por devolver o carro")
                else:
                    print("código inválido")
            except ValueError:
                print("Você digitou um valor inválido, tente novamente")
        else:
            print("não há carros alugados no momento para devolver")
        
        continuar  = input("\nDeseja continuar? (sim | não)\n").strip().lower()
        if continuar == "não":
            print("Obrigado por utilizar o nosso sistema!")
            break  
        elif continuar == "sim":
            continue
        else:
            print("Opção inválida, tente novamente")
 
    #caso o usuário não queria continuar
    elif escolha == "3":
        print("Obrigado por utilizar o nosso sistema")
        break
    
    else:
        print("Opção inválida, tente novamente")
    
        continuar  = input("\nDeseja continuar? (sim | não)").strip().lower()
        if continuar == "sim":
            continue
        elif continuar == "não":
            print("Obrigado por utilizar o nosso sistema!")
            break  
        else:
            print("Opção inválida, tente novamente")
    
   
    
            
    
        
                
    

        
        
        
        


    