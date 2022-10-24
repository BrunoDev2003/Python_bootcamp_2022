menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

deposito = 0
sacar = 0
saldo = 0
limite = 200
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("qual valor que deseja depositar?"))
        if saldo < 0:
            print("Saldo insuficiente")
            break
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"

    elif opcao == "s":
        sacar = float(input("qual valor que deseja sacar?"))
        if saldo < 0:
            print("Saldo insuficiente")
            break

        elif saldo > 500:
            print("Limite total atingido!")
        
        else:
            saldo == sacar
            limite_saques = numero_saques + limite_saques
        
    elif opcao == "e":
        print("Extrato")
        print("R$" + f"{deposito:.2f}\n" )
        print("R$" + f"{sacar:.2f}\n" )


    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente")