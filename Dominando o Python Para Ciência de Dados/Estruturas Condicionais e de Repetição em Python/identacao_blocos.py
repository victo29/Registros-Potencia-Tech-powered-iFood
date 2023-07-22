def sacar(valor):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print(f"Seu saldo atual é: {saldo}")
        print("Valor Sacado")

    print("Obrigado por ser nosso cliente, tenha um bom dia")

sacar(600)

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Seu saldo atual é: {saldo}")


depositar(100)