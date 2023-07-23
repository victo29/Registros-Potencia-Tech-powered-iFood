tipo_conta = int(input("Digite [1] para conta normal e [2] para conta universitária:\n"))

conta_normal = False
conta_universitaria = False

if tipo_conta == 1:
    conta_normal = True
    conta_universitaria = False
else:
    conta_normal = False
    conta_universitaria = True


saldo = 2000.0
saque = float(input("Informe o seu saque: "))
cheque_especial = 1000.0

if conta_normal:
    if saldo >= saque:
        print("Realizando saque!")
    elif saque <= (saldo + cheque_especial):
        print("Realizando saque com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Realizando saque!")
    else:
        print("Saque não realizado!")




# opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extrato: "))

# if opcao == 1:
#     valor =float(input("Informe a quantia que deseja sacar: "))
# elif opcao == 2:
#     print("Exibindo extrato......")
# else:
#     print("Opção errada")




# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Realizando saque!")
# else:
#     print("Saldo insuficiente!")




# if saldo < saque:
#     print("Saldo insuficiente!")

