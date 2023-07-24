# while True:
#     opcao = int(input("Informe um número: "))

#     if opcao == 10:
#         break # para a execução
#     print(opcao)


for numero in range(100):
    if numero%2 == 0:
        continue #pula a execução
    
    print(numero, end= " ")