# Programa orientada a objetos - POO

Conhecer o paradgma de programação orientada a objetos.
A linguagem de programação python já é nativamente orientada a objetos

## PARADIGMA DE PROGRAMAÇÃO
Um paradigma de programação é um estilo e programação. Não é uma linguagem, e sim a forma como você soluciona os problemas através do código.

### Exemplo:
Problema: Beber água
* solução 1: Usar um copo para beber água.
* Solução 2: Usar uma garrafa para beber água.

### Exemplos de paradigmas
* Imperativo ou procedural
* Funcional
* Orientado a eventos

## PROGRAMAÇÃO ORIENTADA A OBJETOS
O paradigma de programação orientada a bojetos, estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender **POO** são: **Classes e Objetos**.

Para entender melhor, classes estão diretamente ligada a programação orientada a objetos, que nada mais é que uma abstração de como lidar-mos com certos tipos de problemas em nosso código, criando e usando objetos de uma forma mais complexa, a partir de estruturas **"moldes"**


## OS CONCEITOS DE CLASSES E OBJETOS

Uma classe define as características e comportamentos de um objeto, porém nao conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem características e comportamentos que foram definidos nas classes.

Uma classe dentro das linguagens de programação nada mais é do que um objeto que ficará reservado ao sistema tanto para indexação quanto para uso de sua estrutura, é como se criássemos uma espécie de molde de onde podemos riar uma série de objetos a partir desse molde.

Assim podemos inserir diversos outros objetos dentro dessas classes de forma que que fiquem **instanciáveis**, modularizando, oferecendo uma complexa, mas muito eficiente maneira de se trabalhar com objetos.

Para Python toda variável é um objeto, a forma como lhe instanciamos e/ou irá fazer com que o interpretador trate com mais ou menos privilégios dentro do código.

Em resumo, uma classe será uma estrutura molde que poderá comportar dados dento de si, assim como servir de molde para criação de novas variáveis externas.

## DEFININDO UMA CLASSE
Em python podemos manualmente definir uma classe respeitando sua sintaxe adequada, hhá uma maneira correta de identificar tal tipo de objeto para que o interpretador a reconheça e trabalhe com ela.

**Quando temos uma função dentro de uma classe ela é chamadad de método** dessa classe, que pode executar qualquer coisa.

Quando definimos uma classe manualmente, começamos criando um construtor para ela, uma função que ficará reservada ao sistema e será chamada sempre que uma instância dessa classe for criada/usada para que o interpretador crie e use a instância da variável que usa essa classe corretamente.
### Exemplo de Classe:

```python

class Usuario:  # Defnição classe Usuário
    def __init__(self, nome, idade):    # Construtor
        self.nome = nome                #
        self.idade = idade
    
    def boas_vindas(self):              # Método da classe Usuario
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario_1 = Usuario('jhon', 31)
usuario_1.boas_vindas()
```
```python

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Au-au")

    def dormir(self):
        self.acordado = False
        print("Zzzzz")

```

### MANIPULAÇÃO: ALTERANDO DADOS DE UMA INSTÂNCIA
#### Manipulação direta

```python
usuario_1.nome = 'Tiririca'
usuario_1.idade = 50

usuario_1.boas_vindas() # Usuário: Tiririca, Idade: 50
### Exemplo de Objeto:

```
#### Manipulação Via Funções setattr() delattr()

```python
setattr(usuario_1, 'nome', 'Homem-Aranha')

delattr(usuario_1, 'idade')
setattr(usuario_1, 'idade', 100)
usuario_1.boas_vindas() # Usuário: Homem-Aranha, Idade: 100


```
```python

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

print(cão_2.acordado)

cao_2.dormir()

print(cão_2.acordado)

        
```

## PRIMEIRO PROGRAMA POO
João tem uma bicicleta e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe:
* Cor
* Modelo
* Ano
* Valor

da bicicleta vendida. Uma bicicleta pode:
* Buzinar
* Parar
* Correr

Adicione esses comportamentos!

## CONSTRUTORES E DESTRUTORES

### Conhecendo os Métodos \__init__ e \__del__

## Método Construtor
O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome
**\__init__**.

```python
class Cadastro_cliente:
    def __init__(self, cpf, nome, data_nasc, telefone, email ):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.email = email
```

## Método Destrutor
O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++, porque o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome **\__del__**.

```python
class Cadastro_cliente:
    def __del__(self):
        print("Destruindo a instância")

cliente = Cadastro_cliente()
del cliente

```

## APLICANDO RECURSIVIDADE
O termo recursividade em linguagens de programação se refere quando um determinado objeto ou função chamar ele mesmo dentro da execução de um bloco de código exectado sobre si um incremento.


### Exemplo contando até 10 recursivamente.

```python
def contar_a_dez(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    contar_a_dez(maximo, atual + 1)

contar_a_dez(10, 1)
```

## HERANÇA em POO

Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai(base)

### BENEFÍCIOS DA HERANÇA
* Representa bem o srelacionamentos do mundo real.
* Forcene reutilização de código, não precisamos escrever o mesmo código repetidadmente. Para além de permitir adicionar mais recursos a uma classe sem modificá-la.
* É de natureza transitiva, o que significa que, se  classe B herdar da Classe A, todas as subclasses de B herdarão automaticamente da classe A.

### Herança Simples
Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.
#### Exemplo
```python
class A:
    pass

class B(A):
    pass
```
### Herança Múltipla
Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla. 
#### Exemplo
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

## Python MRO
