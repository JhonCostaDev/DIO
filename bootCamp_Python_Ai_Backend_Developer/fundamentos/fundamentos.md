# INTRODUÇÃO AO PYTHON 

## A ORIGEM 

Python nasceu em 1989 como um hobby do programador Guido Van Rossum. A ideia inicial era dar continuidade a linguagem ABC que era desenvolvida no centro de pesquisa holandês (CWI). 

## OS OBJETIVOS 

Python foi influenciada por ABC, que era uma linguagem pensada para iniciantes, devido a sua facilidade de aprendizagem e utilização. 

Os objetivos de Van Van Rossum para a linguagem python eram: 
* Uma linguagem fácil e intuitiva. 

* Código aberto para que todos possam contribuir. 

* Código tão inteligível quanto inglês. 

* Adequada para tarefas diárias e produtivas.

## LINHA DO TEMPO 

* Van Rossum inicia o desenvolvimento em 1989 e em fevereiro de 1991 é lançada a primeira versão pública 0.9.0 

* Em 1994 é lançada a versão 1.0 

* Em 1995 Van Rossum lança a versão 1.2, enquanto trabalhava no CWI. Com o vínculo encerrado com o centro de pesquisa, ele e sua equipe principal de desenvolvedores python mudaram-se para BeOpen.com, nas a BeOpen Python Labs. 

* Nos anos 2000 a segunda versão do python é publicada em outubro, nessa versão nasce a List Comprehensions e uma melhoria no coletor de lixo para remoção de referências cíclicas. 

* Em 2001 nasce a Python Software Foundation – PSF, que a partir da versão 2.1 possui todo o código, documentação e especificações da linguagem. 

* Em 2008 é lançada a versão 3.0, que resolveu muitos problemas de design da linguagem e melhorou a performance. Algumas mudanças foram muito profundas e dessa forma a versão 3.x não é retrocompatível. 

## ONDE SE DEVE UTILIZAR A LINGUAGEM PYTHON 

* Python é uma linguagem muito versátil 

* Tipagem dinâmica e forte. 

* Multiplataforma e multiparadigma. 

* Comunidade gigante e ativa. 

* Curva de aprendizado baixa. 

 

**Obs.:** Não é boa para desenvolvimento Mobile! 

# ETAPA 1 – CRIANDO O PRIMEIRO PROGRAMA 

## A RECEITA 

Programar consiste em informar ao computador uma sequência de rotinas que devem ser processadas. Imagine uma receita de bolo, precisamos saber os ingredientes e o modo de preparo. Seguindo corretamente as instruções, ao fim do processo teremos um bolo. 

## CRIANDO NOSSO ARQUIVO 

Para criar a nossa receita de bolo em python, precisamos criar um arquivo com extensão py. Com o arquivo criado podemos inserir nossos ingredientes e modo de preparo!  

## TIPOS DE DADOS 

### O QUE SÃO TIPOS: 

Os tipos servem para definir as características e comportamento de um valor (objeto) para o interpretador. Com esse tipo seremos capazes de realizar operações matemáticas. Esse tipo para ser armazenado em memória irá consumir 24 bytes. 

### TIPOS EM PYTHON (BUILT-IN) 
|   |   |
|---|---|
|Texto  |str   |
|Número   |int, float, complex   |
|Sequência   |List, tuple, range |
|Mapa | dict|
|Coleção| set, fronzenset|
|Booleano | bool|
|Binário | Bytes, bytearray, memoryview | 

## TIPOS NÚMERICO 

* **Números Inteiros**: São representados pela classe int e possuem precisão ilimitada. Exemplos válidos de inteiros: 1, 10, 100, -1, -10, -100 ... 99001823. 

* **Números de Ponto Flutuante**: São usados para representar os números racionais e sua implementação é feita pela classe float. São exemplos: 1.5, -10.543, 0.76 ... 999278.020. 

* **BOOLEANOS**: É usado para representar verdadeiro ou falso, e é implementado pela classe bool. Em python o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 (zero) representa verdadeiro e 0 (zero) representa falso. São exemplos: True e False. 

* **STRINGS**: Strings ou cadeia de caracteres são usadas para representar valores alfanuméricos, em python as strings são definidas utilizando a classe str. São exemplos válidos: “Python”, ‘Python’, ‘’’Python’’’, ‘p’. 

## USANDO O MODO INTERATIVO 

O interpretador python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na instantaneamente.  

### FUNÇÃO DIR E HELP 

**Dir**: sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. Exemplo: dir() - dir(100) 

Help: Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo: help() / help(100). 

[REPOSITÓRIO DA TRILHA DE PYTHON](https://github.com/digitalinnovationone/trilha-python-dio/tree/main/00%20-%20Fundamentos)

## VARIÁVEIS E CONSTANTES 

**VARIÁVEIS** 

Em linguagem de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois pelas nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

```python
age = 37
name = 'Goku'
print(f'My name is {name} and I'm {age} years old!')
# My name is Goku and I'm 37 years old!
```

## ALTERANDO OS VALORES DAS VARIÁVEIS 

No python, não precisamos definir o tipo de dados da variável, pois ele faz isso automaticamente. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor de uma variável basta fazer uma atribuição de um novo valor:  

```python
number = 5
print(number) # 5

number = 10
print(number) # 10
```

## CONSTANTES

Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável. 

### O PYTHON NÃO TEM CONSTANTES 

Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens como o Java e o C utilizamos **final e const**, respectivamente para declarar uma constante. Em python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letra maiúscula: 

```python
# Exemplo de Constantes em Python

ABS_PATH = "/home/user/Documents/project/pythonCourse"
DEBUG = True
STATES = ['CE','SP','RJ','MG','RS','GO','BA']
PY = 3,14159265358979323846
```

## BOAS PRÁTICAS 

* O padrão de nomes deve ser snake case.  
Ex: (valor_total = 35.5, taxa_juros = 5) 

* Escolher nomes sugestivos. 

* Nome de constantes todo em maiúsculo. 

### CONVERSÃO DE TIPOS 

Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente. Exemplo: Variáveis do tipo string que armazenam números e precisamos fazer alguma operação matemática com esse valor. 

//TODO: Melhorar essa definição!
 

### A estética 

Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina. 

### Utilizando espaços 

Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

# Estruturas Condicionais

## O que são?
A estrutura condicional permite o desvio de fluxo de controle, quando determindas expressões lógicas são atendidas.

### IF (Se)
No comando if, será testada uma expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do IF serão executadas.
Exemplo:

```python
saldo = 2000.0
saque = float(input("Informe o valor do saque:\n))

if saldo >= saque:
    print("Realizando saque")

if sado < saque:
    print("saldo insuficiente!")
```
-----------------------------------
### IF/ELSE (Se / então)
Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas **if e else**. Como sabemos se a expressão lógica testada no **if** for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do **else** será executado.

Exemplo:
```python
saldo = 2000.0
saque = float(input("Informe o valor do saque:\n))

if saldo >= saque:
    print("Realizando saque")

else:
    print("saldo insuficiente!")

```
---------------------------------
### IF/ELIF/ELSE (Se / então se/ então)
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorno verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, **porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código**.

Exemplo:

```python
opcao = int(input("Informe uma opção: [1] sacar \n [2] Extrato: \n))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque:\n"))
elif opcao == 2:
    print("Exibindo o extrato...")
else: 
    sys.exit("Opção inválida")
```

## IF ANINHADO

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

EXEMPLO:
```python
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!)
    else: 
        print("Saldo insuficiente!")
```

--------------------------------------------

## IF TERNÁRIO

Permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

EXEMPLO:
```python
status = "Sucesso" if saldo  >= saque else "Falha"
```

# O que são estruturas de Repétição?

São estruturas utilizadas para repetrir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.


## Comando FOR

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

```python
statement = "Apple"
for letter in texto:
   print(letter)
'''
A
p
p
l
e
'''

list = [1, 2, 3, 4, 5]

for iten in lista:
    print(iten)

'''
1
2
3
4
5
'''
```
## Função Range

Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:

i, i+1, i+2, i+3, i+4, ..., j-1

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional)


```python
print(list(range(4))) # [0, 1, 2, 3, 4, 5]
 

for number in range(11):
    print(number, end=", ")
print() 
   
# Tabuada 5
  
for number2 in range(0, 51, 5):
    print(number2, end=", ")
```

## Comando While
O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

Exemplo
```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))
    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")
else:
    print("Obrigado por usar nosso sistema!")
```
<br>


# MANIPULANDO STRINGS COM PYTHON 

Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento. 

## Etapa 1 – Conhecendo métodos úteis da classe string 

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar. 

Em algumas linguagens, manipular sequência de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples. 

Maiúscula, minúscula e título 

```python
curso = "Python"
print(curso.upper())
print(curso.center(14, "*"))

# Eliminando espaços em branco

curso = "   Python  "
print(curso.strip() +".")
print(curso.lstrip()+".")
print(curso.rstrip()+".")

print(curso.upper())
print(curso.lower())
print(curso.title())

print(".".join(curso))
# Junção e centralização
menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "*"))

```

# ETAPA 2 - INTERPOLAÇÃO DE VARIÁVEIS 

Em python 3 temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal (%), a segunda é utilizando o método format e a última é utilizando f strings. A primeira forma não é atualmente recomendada e seu uso em python 3 é raro. 

## OLD STYLE 

```python
nome = 'Pedro Vaz de Caminha'
idade = 59
profissao = 'Escrivão'

print("Olá, me chamo %s, tenho %d e trabalho como %s na armada real Portuguesa"%(nome, idade, profissao))

# Olá, me chamo Pedro Vaz de Caminha, tenho 59 e trabalho como Escrivão na armada real Portuguesa
```

## Método Format
```python
nome = 'Pedro Vaz de Caminha'
idade = 59
profissao = 'Escrivão'

print("Olá, me chamo {}, tenho {} e trabalho como {} na armada real Portuguesa".format(nome, idade, profissao))

# Olá, me chamo Pedro Vaz de Caminha, tenho 59 e trabalho como Escrivão na armada real Portuguesa
```

##  MÉTODO F-STRING 

```python
nome = 'Pedro Vaz de Caminha'
idade = 59
profissao = 'Escrivão'

print(f'Olá, me chamo {nome}, tenho {idade} e trabalho como {profissao} na armada real Portuguesa')

# Olá, me chamo Pedro Vaz de Caminha, tenho 59 e trabalho como Escrivão na armada real Portuguesa


PI = 3.14159
print(f'O valor de Pi é: {PI:.2f}') # O valor de Pi é: 3.14
print(f'O valor de Pi é: {PI:10.2f}') # O valor de Pi é:       3.14
```

## FATIAMENTO DE STRING 

É uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop, [step]]. 