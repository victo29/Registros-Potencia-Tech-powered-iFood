nome = "Victor"
idade = 16
profissao = "Programador"
linguagem = "Python"
# Old style
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

print("-------------------------")

# Método format
dados = {"nome": "Victor", "idade": "16"}
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {name}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(name=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Nome: {nome}, Idade: {idade}.".format(**dados))
print("-------------------------")

# Método f style
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
PI = 3.14159
print(f"Valor de PI: {PI: .2f}") #Faz com que apareça somente a quantidade de casas decimais definidas
print(f"Valor de PI: {PI: 10.2f}") #o número a frente define uma quantidade de espaços
