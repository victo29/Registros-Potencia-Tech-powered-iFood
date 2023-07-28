numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"PY", "PHP", "PY"} # Outra maneira de utilizar o set
print(linguagens)  # {"PY", "PHP"}

print("--------------------------------------------")

numeros = {1, 2, 3, 2}

numeros = list(numeros) # Transforma o Set em list

print(numeros[0])

print("--------------------------------------------")

for indice, carro in enumerate(carros):  # Função enumerate
    print(f"{indice}: {carro}")
