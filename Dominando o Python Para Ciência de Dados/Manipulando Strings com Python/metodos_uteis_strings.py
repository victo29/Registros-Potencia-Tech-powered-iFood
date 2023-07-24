curso = "PytHoN"

print(curso.upper()) #Transforma todos em maiúscula

print(curso.lower()) #Transforma tudo em minúscula

print(curso.title()) #Transforma a primeira letra em maiúscula 

print(curso.strip()) #Remove os espaços em branco

print(curso.lstrip()) #remove os espaços em branco no final/esquerda

print(curso.rstrip()) #remove os espaços em branco no começo/direita

print(curso.center(10, "#")) #Centraliza e adiciona caracteres a uma string


for letra in curso:
    print(letra, end="-")
   
print()
print(".".join(curso)) #Junta caracteres a cada item de uma string

