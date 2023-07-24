## Identação e blocos
- Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina
- Em python não se tem caracteres que limitam o espaço
- Para iniciar o bloco se utiliza o caractere ":"

## Estruturas condicionais
- Permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas
- "if" O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas
- "else" Utilizado para criar uma estrutura condicional com dois desvios. Caso a expressão lógica testada no if for falsa então o bloco de código do else será executado.
- "elif" utilizado em cenários onde é necessário mais de dois desvios. O elif é composto por uma nova expressão lógica que será testada e caso retorne verdadeiro o bloco de código será executado

 ### If aninhado
- Podemos criar estruturas aninhadas, ou seja, estruturas dentro de estruturas

### if ternario 
- Permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida

## Estruturas de repetição
- São estruturas utilizadas para repitir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

### Comando for
- é usado para percorrer um objeto iterável. Faz sentido usar o "for" quando sabemoss o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável
- Função range, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio para um fim. Ela recebe 3 argumentos: stop, start e step opcional

### Comando while
- Faz sentido utilizar o while quando não sabemos o número exato de vezes que nosso bloco de código deve ser xecutado
