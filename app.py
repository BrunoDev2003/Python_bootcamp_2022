menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""


saldo = 0
limite = 200
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        input("qual valor que deseja depositar?")
        if saldo < 0:
            print("Saldo insuficiente")
            break
        else:
            saldo += extrato 

    elif opcao == "s":

        print("Sacar")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        print("Operação inválida, por favor selecione novamente")
        break