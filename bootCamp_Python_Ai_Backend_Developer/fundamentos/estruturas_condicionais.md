# Estruturas Condicionais e de Repetição

## Indentação e Blocos

### A estética
Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

### Bloco de comando
As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves.

### Utilizando espaços
Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

## Estruturas Condicionais

### O que são?
A estrutura condicional permite o desvio de fluxo de controle, quando determindas expressões lógicas são atendidas.

### IF
NO comando if, será testada uma expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do IF serão executadas.
Exemplo:

saldo = 2000.0
saque = float(input("Informe o valor do saque:\n))

if saldo >= saque:
    print("Realizando saque")

if sado < saque:
    print("saldo insuficiente!")

-----------------------------------
### IF/ELSE
Para criar uma estrutura condicional com dois devios, podemos utilizar as palavras ereservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.

Exemplo:

saldo = 2000.0
saque = float(input("Informe o valor do saque:\n))

if saldo >= saque:
    print("Realizando saque")

else:
    print("saldo insuficiente!")

---------------------------------
### IF/ELIF/ELSE
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorn verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

Exemplo:


opcao = int(input("Informe uma opção: [1] sacar \n [2] Extrato: \n))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque:\n"))
elif opcao == 2:
    print("Exibindo o extrato...")
else: 
    sys.exit("Opção inválida")


## IF ANINHADO

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

EXEMPLO:

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


--------------------------------------------

## IF TERNÁRIO

Permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

EXEMPLO:

status = "Sucesso" if saldo  >= saque else "Falha"


