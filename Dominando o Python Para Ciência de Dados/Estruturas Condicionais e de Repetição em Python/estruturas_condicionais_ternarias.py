saldo = 1000
saque = int(input("Digite o valor do seu saque: "))


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")