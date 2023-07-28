frutas = ["laranja", "maca", "uva"]

print(frutas[0]) #acessando os dados atráves do índice
print(frutas[-1]) #acessando os dados atráves do índice negativo

## frutas = []

letras =  list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, "São Paulo", True]

print("----------------------------------------")

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) ## [1, "a", 2]
print(matriz[0][0])## 1
print(matriz[0][1]) ## a
print(matriz[1][-1]) ## 4
print(matriz[-1][-1]) ## c

print("----------------------------------------")

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"] - ponto de inicio
print(lista[:2])  # ["p", "y"] - ponto de parada
print(lista[1:3])  # ["y", "t"] - ponto de inicio e ponto de parada
print(lista[0:3:2])  # ["p", "t"] - ponto de inicio e ponto de parada e step
print(lista[::])  # ["p", "y", "t", "h", "o", "n"] - sem argumentos exibe todos
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"] - exibe ao contrario

print("----------------------------------------")

for frutas in frutas:
    print(frutas)


print("----------------------------------------")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero% 2 == 0:
        pares.append(numero) # Adiciona novos valores a lista
print(pares)

quadrado = []
# quadrado = [numero ** 2 for numero in numeros]

for numero in numeros:
    if numero % 2 == 0:
        quadrado.append(numero**2)
print(quadrado)

print("----------------------------------------")




