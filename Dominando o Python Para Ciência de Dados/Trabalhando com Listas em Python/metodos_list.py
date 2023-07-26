lista = []

lista.append(1) # Adiciona elementos a lista
lista.append(2)
lista.append(3)

print(lista)

print("--------------------------")

#lista.clear() # Limpa toda a lista

l2 = lista.copy() # cria uma copia da lista original 
print(l2)

print("--------------------------")

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho")
cores.count("azul") #retora a quantidade de vezes que o elemento aparece
cores.count("verde")

print("--------------------------")

linguagens = ["PY", "C#", "PHP"]
linguagens.extend(["JV", "C", "C++"]) #uni duas listas
print(linguagens)

print("--------------------------")

print(linguagens.index("C")) # Retorna o indice da primeira ocorrencia do valor passado 

print("--------------------------")

linguagens.pop() # Remove o ultimo elemento da lista 
linguagens.pop(0) # Remove o valor do indiece indicado
print(linguagens)

print("--------------------------")

linguagens.remove("C") # Remove a primeira o ocorrencia do o valor passado
print(linguagens)

print("--------------------------")
linguagens.reverse() #inverte a ordem da lista
print(linguagens)

print("--------------------------")

linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort()  # ["c", "csharp", "java", "js", "python"] # ordena alfabeticamente a lista
print(linguagens)
print("\n")
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] # Ordena a lista e inverte a sua ordem
print(linguagens)
print("\n")
linguagens = ["python", "js", "c", "java", "csharp"] # Ordena a lista por tamanho das palavras
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)
print("\n")
linguagens = ["python", "js", "c", "java", "csharp"] # Ordena a lista por tamanho das palavras e inverte sua ordem
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
print("\n")

print("--------------------------")

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # Retorna o tamanho da lista

print("--------------------------")

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # # Ordena a lista por tamanho das palavras
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # Ordena a lista por tamanho das palavras e inverte sua ordem