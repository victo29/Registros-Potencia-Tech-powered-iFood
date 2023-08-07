# Explorando a abordagem de um SGBD - isolamento, Auto-descrição, Compartilhamento e Visões

- Caracteristicas da abordagem BD:
* Isolamento
* Abstração
* Mútiplas visões
* Auto-descrição
* Compartilhamento
* Transação multiuser

## Natureza auto-descritiva da aboragem de BD
- Descrição das suas estruturas e regras
- Estrutura bem definida dos dados
- NoSQL não possuem esse tipo de estrutura
- Um SGBD pode possuir vários bancos de dados

## Isolamento entre Programa/Data e Abstração
- Separação dos dados do programa de aplicação
- Program-data independence

## Suporte à múltiplas visões dos dados
- Vão ter várias pessoas interessadas no mesmo dado
- É possível a partir das entidades transformar/criar uma visualização que mais agrade o que o serviço destinado pede

## Compartilhamento  de dados e Processamento de Transações Multiusuários
- Acesso simultâneo por mais de uma pessoa ao banco de dados
- Concurrency Control
- OLTP, Os sistemas OLTP registram as interações de negócios conforme elas ocorrem na operação diária da organização e dão suporte à consulta desses dados para criar inferências
- Atomicidade
-
## Abordagem de banco de dados - Quais são os Atores em Banco de Dados
- Dentre os atores do dia a dia podemos citar o Administrador, Designer(modelam o banco) e os Usuários finais
### Usuários finais
- Casuais: els buscam acessos ocasionais, diferentes informações e gerealmente utilizam de apis e de linguagens de mais alto nível
- Ingênuos: Canned Transactions(transações encapsuladas), raramente ocorre erros e a maioria dos usuários fazem parte desse grupo
-  Sofistacados: São pessoas que tem noção do sistema, pessoas que trabalham na área
- Standalone: São pessoas que tem os seus próprios BDs


## Vantagens de Utilizar a Abordagem de SGBDs
- Controle de redundância
- Restrição de acesso
- Storage - provê persistênca
- Storage - provê estrutura
- Backup e Recovery

### Controle de Redundância
- Previne a reduncância, inconsistência, updates desnecessários, desperdicio
- Desnormalização é quando em alguns casos é necessário a utilização da redundancia para dar mais desempenho a algumas ações

### Restrição de acesso
- Controla o acesso dos usuários de acordo com suas necessidades

### Backup e Recovery
- Recuperação de recursos
- Provendo interface Multi-user


## Ganhos em utilizar SGBDs
- Padronização
- Redução de tempo no desenvolvimento da aplicação
- Flexibilidade
- Disponibilidade de info atualizadas
- Economía com escalabilidade 

### Padronizção
- Facilita na manutenção
- Facilita o acesso aos dados
- Fácil para outras equipes se integrarem
- Facilita a leitura do banco

### Redução de tempo no desenvolvimento da aplicação
- Menor esforço para codificação

## Quando não usar SGBDs
- Em cenários curtos onde não são necessário a persistência de dados
- Acesso unário
- APP rigorosas em real time
- 