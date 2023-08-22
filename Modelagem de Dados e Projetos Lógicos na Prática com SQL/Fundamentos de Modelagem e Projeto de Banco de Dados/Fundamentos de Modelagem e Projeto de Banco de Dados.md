# Fundamentos de Modelagem e Projeto de Banco de Dados
## Discursando sobre as características de um Banco de Dados
### Relembrando
- Gerência de dados 
- Isolamento data/program
- integridade e Consistência
- Segurança
- Views
- Recuperação
- Recovery
- Concorrência

## Mundo Fechado
- Afirmação em cima de um predicado. Toda informação contida no SGBD eu consigo utilizala para responder minhas perguntas, o que está fora do meu domínio eu não posso responder e consequentemente é Falsa
- Preoposição que está relacionada a lógica de predicados
### Mini-mundo
- É um pedaço do mundo real que se está querendo modelar
- O banco de dados vai ser o modelo lógico que representa e armazena o mini-mundo
- O conteitor de mundo fechado etá atrelado a mini-mundo

## Algebra Relacional
- O predicado é a parte da oração que contém o verbo e que traz informações sobre o sujeito. Um determinado criterio relacionado ao sujeito que vai ser a base para queries mais complexas
- Linguagem formal para consulta/extração de dados
- Quando se usa a algebra relacional estamos criando ações utilizando operações que serão direcionadas ao SGBD e o SGBD vai está retornando
 
### Processo
- Projeto Conceitual:  projeto de alto nível onde vai definir os requisitos do sistema. O que vai acontecer
- Projeto Lógico: modelar e criar um diagrama onde vai representar o contexto. indica o como estruturar
- Projeto Físico: Escolhe o tipo de modelo, a estrutura. indica como implementar
- Validação: observair se corresponde as expectativas e se responde as perguntas necessárias
- Produção
- Manutenção 

## Como implementar um BD?
- Entender o contexto e requisitos
- Visualizar quais são os perfils de acesso
- Entender o que se quer representar
- Definir a arquitetura, funcionalidades e modelo
- Conceitual => Lógico => Físico

## Desing de BDs - Projeto Conceitual
- Podemos utilizar a linguagem textual e também a Gráfica
- 1° Coleta de dados e análise
- Definição do Esquema Conceitual - MER ou UML
- Observar se a modelagem responde as perguntas necessárias

## Processo
- ***Projeto coneitual*** - indica o que vai ter
- ***Projeto lógico*** - indica o como estruturar
- ***Projeto Físico*** - indica como implementar

## Projeto lógico 
- Descrição do modelo conceitual
- Definição das estruturas para a organização dos dados
- Vai definir o modelo do SGBD
- Determina as caracteristicas do SGBD

## Projeto Físico
- Descrição do modelo lógico
- Diretamente ligado ao SGBD
- Estrutura e índices
- Organizaçãp e Caminhos de Arquivos
- Segurança, performance