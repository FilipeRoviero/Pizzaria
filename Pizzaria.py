def cardapio():
    print("-" * 11 + "Bem-vindo a Pizzaria do Filipe Roviero Ronca" + "-" * 11)
    print("-" * 29 + "Cardápio" + "-" * 29)
    print("-" * 66)
    print("-" * 3 + "|   Tamanho   |   Pizza Salgada(PS)   |   Pizza Doce(PD)   |" + "-" * 3)
    print("-" * 3 + "|      P      |      R$ 30.00         |      R$ 34.00      |" + "-" * 3)
    print("-" * 3 + "|      M      |      R$ 45.00         |      R$ 48.00      |" + "-" * 3)
    print("-" * 3 + "|      G      |      R$ 60.00         |      R$ 66.00      |" + "-" * 3)
    print("-" * 66)
    
cardapio() #Printa o menu na tela

valor = 0

while True:
    sabor = input("Escreva o sabor desejado (PS/PD): ")
    if sabor == "PS":
        tamanho = input("Escreva o tamanho da pizza (P/M/G): ")
        if tamanho == "P":
            valor += 30 #Incrementa ao valor final do pedido, o mesmo se repete em todos os tamanhos
            print(f'Você pediu uma pizza salgada tamanho P: R${valor:.2f}') #Printa o tamanho solicitado e o valor adicionado, o mesmo se repete em todos os tamanhos
        elif tamanho == "M":
            valor += 45
            print(f'Você pediu uma pizza salgada tamanho M: R${valor:.2f}')
        elif tamanho == "G":
            valor += 60
            print(f'Você pediu uma pizza salgada tamanho G: R${valor:.2f}')
        else:
            print("Tamanho inválido! Por favor tente novamente!")
            continue #Caso digite um tamanho que não exista ele retorna ao começo do loop

    elif sabor == "PD": #Esta parte segue a mesma lógica para pedir a pizza salgada, somente alterando os valores
        tamanho = input("Escreva o tamanho da pizza (P/M/G): ")
        if tamanho == "P":
            valor += 34
            print(f'Você pediu uma pizza doce tamanho P: R${valor:.2f}')
        elif tamanho == "M":
            valor += 48
            print(f'Você pediu uma pizza doce tamanho M: R${valor:.2f}')
        elif tamanho == "G":
            valor += 66
            print(f'Você pediu uma pizza doce tamanho G: R${valor:.2f}')
        else:
            print("Tamanho inválido! Por favor tente novamente!")
            continue #Caso digite um tamanho que não exista ele retorna ao começo do loop

    else:
        print("Sabor inválido! Por favor tente novamente!")
        continue #Caso digite um sabor que não existe ele retorna ao começo do loop

    repetir = input("Deseha mais alguma coisa? (S/N): ")
    if repetir == "S":
        continue #Se o usuário digitar "S" retorna ao começo do loop mantendo o valor da pizza anteriormente selecionada
    elif repetir == "N":
        print(f'Valor total a ser pago: R${valor:.2f}')
        break #Se o usuário não deseja pedir mais nada ele printa o valor final da compra e encerra o programa