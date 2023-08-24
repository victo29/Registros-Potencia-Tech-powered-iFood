# Modelo Relacionamento de Entidade Aprimorado com Banco de Dados
## Modelo Enchanced ER
- Novos conceitos semânticos, desenvolvidos fora da área de BDs
- Diagrama ERR
- Entidades => Objeto

## Classes superclasses e Herança
- Generalização e Especialização
- Categoria ou Union Type
- Herança: Atributo e relacionamento

### Subclasse e Subtipo
- São classes que herdam um comportamento e estado específico de uma classe mãe
- A classe mãe possui comportament e estado  gerais
- Subclasses dependem do contexto do BD
- As instâncias das superclasses e subclasses representam a mesma coisa no mundo real
- Atributos e Relacionamentos especificos relacionados a algumas subclasses

## Herança
- Princípio próprio da programação orientada a objetos(POO) que permite criar uma nova  classe a partir de uma já existente
- Reutilização de código 
- Agregar atributos e métodos

## Especialização e Generalização
- _Especialização_ está relacionado a subclasses, desmembrar uma entidade em outras mais específicas. Gera subclasses
- _Generalização_ inverso da especialização, propiedades comuns entre as  entidades. Gera superclasses

## Constraints de Generalização e Especialização 
- Regras que determinam as diretrizes na definição de subclasses
### Generalização
- Predicated-defined (condição) uma condição definida pelo predicado
- Attribute-defined Specialization Especialização definida por atributo, enconra as subclasses a partir de um atributo específico de uma subclasse
- User-defined Definição feita pelo usuário

### Especialização
- Disjointness constraint (conjuntos disjuntos) não permite sobreposição de papeis, não permite que os dados relacionados a uma entidade seja colocado em mais de uma entidade
- Overlapping permite que haja uma sobreposição, um dado pode mais de um papel
- Completeness constraint: Total ou parcial. 
_Total_,é quando o dados ele é obrigatoriamente tem que está relacionado a alguma das subclasses.
_Parcial_, significa que não o dado pode ou não está relacionado a alguma das subclasses

### Regras
- Exclusão em cascata
- Entidade em superclasse => predicated-defined (definir o predicado)
- Entidade em superclasse com total - 