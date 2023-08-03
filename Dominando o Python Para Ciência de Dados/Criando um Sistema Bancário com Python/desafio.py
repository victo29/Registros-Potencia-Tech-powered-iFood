import textwrap
menu = """
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extratro
[nc] Nova Conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=>
"""
def saque(*,valor_saque, saldo,extrato,num_saques,LIMITE_SAQUES, limite):
        if num_saques < LIMITE_SAQUES:
            if valor_saque <= limite and valor_saque > 0:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque de R${valor_saque: .2f} \n"
                    num_saques += 1
                    print("Saque realizado com sucesso!")
                    return saldo, extrato, num_saques
                else:
                    print("Você não possui saldo suficiente")
                    return saldo, extrato, num_saques
            else:
                print("O valor do saque não é compativel")
                return saldo, extrato, num_saques
        else:
            print("Você não possui mais saques disponiveis por hoje")
            return saldo, extrato, num_saques       


def deposito(saldo,valor_deposito,extrato,/):
    if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito: .2f} \n"
            return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato


def exibir_extrato(saldo,extrato):
        print("\n######## EXTRATO ########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"SALDO ATUAL R$ {saldo: .2f}")
        print("##########################")              


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            
            saldo, extrato = deposito(saldo,valor_deposito,extrato)
        
        elif opcao == "s":
            valor_saque = int(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = saque(valor_saque = valor_saque, saldo = saldo, extrato = extrato, num_saques = numero_saques, LIMITE_SAQUES= LIMITE_SAQUES, limite= limite)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
                criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

         

