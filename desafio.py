
saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saques = 0
MAXIMO_SAQUES = 3


while True:

    menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
    opcao = input(menu).lower() 


    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))


        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite_saque_diario:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_saque_diario:.2f}.")
        elif numero_saques >= MAXIMO_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")

        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
