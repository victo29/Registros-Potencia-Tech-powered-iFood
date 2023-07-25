menu = """
[d] Depositar
[s] Sacar
[e] Extratro
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito: .2f} \n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque <= limite and valor_saque > 0:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque de R${valor_saque: .2f} \n"
                    numero_saques += 1
                else:
                    print("Você não possui saldo suficiente")
            else:
                print("O valor do saque não é compativel")
        else:
            print("Você não possui mais saques disponiveis por hoje")    
    
    elif opcao == "e":
        print("\n######## EXTRATO ########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"SALDO ATUAL R$ {saldo: .2f}")
        print("##########################")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

