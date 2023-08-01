# Funções
- É um bloco de código identificado por nome e pode receber uma lista de parâmetros, esses parâmetros podem não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estrturada
 
## Retornando valores
- Para retornar um valor, utilizamos a palavra reservada return. Toda função python retorna None por padrão.Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor. 

## Args e Kwargs
- Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe valores como tupla e dicionário respectivamente.

## Parâmetros especiais
- Por padrão, argumentos podem ser passados para uma função Python tanto por posição qunato explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedoor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome

## Objetos de primeira classe
- Em python tudo é objeto, dessa forma funções também são objetos o que tornam objetos de primeira classe. Com isso podem atribuir  funções a variáveis,passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, e etc) e usar como valor de retorno para uma função(closures).

## Escopo local e escolo global
- Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações açli feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave "global", que informa ao interpretados que a variável que está sendo manipulado no escopo local é global. ESSA NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA.

- Ao passar objetos imutaveis a umfa função se atentar em criar uma copia do objeto origem para que não altere o valor do original, caso queira que o valor não altere