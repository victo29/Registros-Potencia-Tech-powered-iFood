# Arquitetura de Banco de Dados
## Arquitetura: Modelos, Esquemas e instâncias
- ***Abstração***: é retirar do contexto informações que não são ecssenciais
- ***Classificação***: está atrelada a estrutura que o dado possui. Ex:

- - ***Modelo de dados Físico*** está relacionada a implementação do sistema. Trata como as informações vão ser persistidas, requisitos de um sistema


- - ***Modelo de dados Conceitual***, está relacionado ao modelo entidade relacionamento. Entidade, atributos e relacionamentos


- - ***Modelo representacional***, Define a estrutura do banco. define as Constrains e as operações

##  Esquema, Instâncias e Estados de um BDs
- ***Esquema*** é uma descrição concisa do BD, o que se tem de objetos e atributos relacionados e como eles se interagem. Dentro de um esquema as entidadades e os objetos são denominados ***construct***(construtores)
- A cada modificação no sistema existe uma modificação de estado
- Meta dados possuem: Descrição do esquema, Construtores e Constrains

## Three-Schema Architecture
- Seu objetivo é promover um isolemento que uma modificação em um determinado esquema não afete um esquema subsequente
- Dividia em:
- - ***External Level***: São os usuários
- - ***Conceptual Level***: está relacionado ao modelo de implementação, entidades, opreações de usuário, constrains, relacionamento. Atrelado ao modelo relacional, está relacionada a experiência do usuário, define como os dados será acessados
- - ***Internal Level***: Está relacionada a disposição dos arquivos, como os arquivos serão persistidos, está atrelado ao modelo físico
- Não é explicitamente nem completamente que essa arquitetura é suportada pelos SGBDs atuais, utilizada mais para fins de estudo
- Pode ser dividida em física e lógica, sendo lógica o External level e Conceptual level, e, a física o Internal level e Conceptual level

## Linguagens para SGBD
- O modelo relacional possui a linguagem SQL
- DDL(Data Definition Language) é uma linguagem de definição de conteúdo
- Aguns SGBDs existem uma sepração explicita entre o Desing e o DBA. Quando se trata de persistência física e etc, podemos está utilizando a SDL. Quando se trata aos viewrs podemos utilzar VDL
- DML a partir dela se pode inserir, atualiar, recuperar e consumir dados

## Interfaces SGBDs
- Web Clients - Requisições e Estrutura
- App Mobile - Bancos, reservas  (Menu limitado pelo app)
- Forms - Voltados para Naive com transações canned (preenchimento total ou parcial)
- GUI - Menus e Forms (manipulando o diagrama)
- NLI - Busca pela palavra reservada e conteúdo (interpreta a linguagem natural)
- Pesquisa Keyword - Indíces|Hacking functions 
- Speech input/output - Speech como input e resposta (contexto limitado)
### Interfaces
- Naive - Transações re rotina e repetitivas 
- DBA - Comando com nível de privilégio

## Ambientes e utilities de SGBD
- Um SGBD é um software modularizado, onde ele é composto por outros programas que o auxiliam a entregar seu resultado final
### Utilites - Gerenciamento 
- Loading: Reformatar os dados, puxar as informações do HD
- Backup: Backup. Um utilitário de backup cria uma
cópia de segurança do banco de dados, normalmente copiando o banco de dados inteiro
para fita ou outro meio de armazenamento
em massa.
- Reoraginazação do storage: reorganizar o armazenamento do banco de dados para transformalo mais performatico
- Monitoramento: Esse utilitário
monitora o uso do banco de dados e oferece estatísticas ao DBA. O DBA usa as estatísticas para tomar decisões se deve ou não reorganizar arquivos ou se deve incluir ou remover índices para melhorar o desempenho.


      