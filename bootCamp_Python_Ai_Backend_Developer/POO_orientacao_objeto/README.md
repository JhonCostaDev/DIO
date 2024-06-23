# Programa orientada a objetos - POO

Conhecer o paradgma de programação orientada a objetos.

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


## OS CONCEITOS DE CLASSES E OBJETOS

Uma classe define as características e comportamentos de um objeto, porém nao conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem características e comportamentos que foram definidos nas classes.
### Exemplo de Classe:

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

### Exemplo de Objeto:

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


