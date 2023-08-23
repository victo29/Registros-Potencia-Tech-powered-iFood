# Modelo de Entidade Relacionamento com Banco de Dados

## Modelo ER: Tipos de Entidades, Chaves e Atributos
- Faz parte do projeto conceitual
- Os elementos principais são entidades, relacionamentos e atributos
- As estruturas são representadas a partir de um DER(Diagrama entidade relacionamento)

### Diagrma ER
- Raras modificações
- Facilidade de manipular
- Esquema ER do banco de dados
- Facilidade no mapeamento


## Atributos
- Propiedades das entidades
- Características/Descrição das entidades
- Atributos relacionados as instâncias
- Atributos podem ser:
1. Atômicos
2. Compostos
3. Multivalorados
4. Armazenados e derivados
5. Nulos
6. Complexos 

### Atributos Atômicos x Compostos
- Atribustos atômicos são smples, de somente uma informação
- Atributos Compostos são formados por outros atributos, são compostos por mais de uma elemento.

### Atributo Multivalorado
- São compostos por vários valores iguais
- Está associado a valores

### Atributos Armazenados X Derivados
- Os armazenados sçao atributos que dificilmente vão se modificar. Por exempro data de nascimento.
- É um tipo de atributo cujo valor pode ser obtido de outros atributos ou relacionamentos

### Atributos nulos
- São atributos que podem ser opcional, onde podem se apresentar como nulos
- UNKNOW é um item faltante

### Atributos complexos
- Estão associados a estrutura
- São compostos por outros atributos como os multivalorados e os compostos


## Entidades
- Um conjunto de entidades corresponde a uma instância
- o esquema é definido pelo tipo de entidade
- Entidades <=> Objetos
- Componente básico
- Existencia independente
- Possui atributos
- Todos os objetos que existem no contexto(mini mundo)

### Entidade Fraca
- São entidades que dependem da existência de outras para existirem
- Não possuem uma chave obrigatoria
- Exclusão em cascata. Se uma entidade deixar de existe a outra deixa também

## Relacionamentos
- São classificados por grau(binario, ternario)
- Auto relacional ou não
- Cardinalidade
- Defino o  papel de cada entidade, trazndo significado 

### Auto relacionamento
- é a forma utilizada para representar associações entre objetos da mesma classe, ou seja, quando temos a ocorrência de uma entidade que está associada com outras ocorrências da mesma entidade

### Constrains - Cardinalidade
- Corresponde ao número máximo de instãncias que participam de um determinado relacionamento(1:1 , N:N, 1:N.......)

### Constrains - Participação
- Vão está associada a uma constrains de classificação total e parcial
- Pelo menos uma instancia participando daquele relacionamento
- Determina que a participação é obrigatória

### Atributos de relacionamento
- Quando um atributo está relacionado a mais de uma entidade

## Tipos de Entidades Fracas
- Dependem de outra entidade para estarem existindo

## Notações
- Entidades: classes/objetos são representadas por retângulos
- Relacionamentos: agregações são representados por losângulos
- Atributos: propiedadeselementares são representados por uma elipse

- Relacionamentos _FRACOS_:  são representados por losângulos com uma doble line
- Entidades _FRACAS_:  são representados por retângulos com uma doble line
- Chave _PARCIAL_: Linha pontilhada
- Chave principal: Linha continua
- Dependência de existência: ||
- Atributo derivado: Pontilhado

## Relacionamento N-ário
- A cima de três relacionamentos
- Reflere a relação de três instâncias
- 





 