conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b) # uni o conjunto A  com o conjunto B
print(resultado)

print("--------------------------------------------")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b) # Retorna os valores iguais entre dois conjuntos
print(resultado)

print("--------------------------------------------")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)
                                                    # Retorna tudo que se tem em um conjunto que NÃO tem no outro
resultado = conjunto_b.difference(conjunto_a)
print(resultado)

print("--------------------------------------------")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b) # Retorna todos os elementos diferentes entre os conjuntos
print(resultado)

print("--------------------------------------------")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)                                        # Retorna True se todos os elementos de um conjunto estiver em outro

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)                                        # Retorna False se nem todos os elementos de um conjunto estiver em outro

print("--------------------------------------------")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)                                                # Faz a verificação contraria ao "issubset"

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

print("--------------------------------------------")

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)                                        # Retorna True se os conjuntos não tem ligação nenhuma
                                                            
resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)                                        # Retorna False se os conjuntos tem ligação 

print("--------------------------------------------")
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}      # Adiciona o elemento passado caso ele não exista ainda no conjunto
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)