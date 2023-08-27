# Modelo Relacional e Mapeamento Relacional com Banco de Dados

## Conceitos de Modelo Relacional: Tupla, Atributo e Relação 
- Modelo relacional são conjuntos de relações
- Tabelas X Arquivos. _Tabela_ é uma maneira estruturada de armazenar, _Arquivos_ é como efetivamente os dados são armazenados

### Tabelas
- Tupla -> É uma linha da tabela, uma instância
- Atributo -> A propiedade da relação
- Relação -> É a parte abstrata, a definição ou a descrição de uma tabela
- Os valores expostos dentro de uma **_tupla_** são **_atômicos_**(indivisiveis), e esses valores são separados por grupos que recebe uma nomeclatura, e são reconhecidos por **_Domínio_**, onde cada dominio possui caracteristicas próprias

### Relação X Arquivos X Tabelas
- Tabelas possuem estruturas bem definidas, na primeira linha os atributos relacionados a tabelas e nas outras as instâncias(tuplas)
- Arquivos possuem a visão de persistência em memória
- Relação se refere ao modelo, a parte mais abstrata

## Conceitos de Modelo Relacional: Conjunto de Tuplas
- Lista de tuplas -> possui uma ordenação onde se tem uma sequência, um elemento precede o outro
- Conjunto de tuplas -> Nível Abstrato, agregado de elementos. Não precisa saber a ordem de disposição dos atributos

## Conceitos de Modelo Relacional: Valores Nulos
- Precisa ser feito com cautela de maneira que interfira no desempenho do BD
- Cenários onde pode ser possível a criação de valores nulos: **Valores desconhecidos**, **Valores existente mas indisponpivel**, **Atributo não se aplica**, **Valor indefinido**

## Constrains do modelo relacional
- Inherete Model-based Constraints -> Características das relações
- Schema-base Constraints -> estão atreladas ao DDL
-  Application-base Constraints -> Fora do ambiente do SGBD

## SGBDs e Esquemas Relacionais
- SGBD é um subconjunto de relações
- 
