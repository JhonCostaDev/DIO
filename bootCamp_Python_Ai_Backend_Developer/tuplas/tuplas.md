# Tuplas
Uma tupla é uma sequência de valores. Esses valores podem ser de qualquer tipo e podem também ser indexados por números inteiros fazendo com que as tuplas sejam muito semelhantes as listas. A principal caracteristica que difere uma tupla de uma lista é que tupla são imutáveis, ou seja, não podem ter seus elementos alterados. Uma tupla é uma lista de valores separados por vígula:

```python
myTyple = 1, 2, 5, 8,12, 3, 27

print(type(myTyple)) # <class 'tuple'>
```
Embora não seja necessário, é comum colocar tuplas entre parênteses:

```python
myTyple = (1, 2, 5, 8,12, 3, 27)

print(type(myTyple)) # <class 'tuple'>
```
Um exemplo onde é bastante útil o uso de tuplas, é quando em um programa necessitamos armazenar  os nomes de cada mês do ano:
```python
meses_do_ano = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez",)
```
Para se criar uma tupla com um único elemento, é preciso incluir uma vírgula no fina:
```python
language1 = ("Python",)
language2 = "Python",
language3 = "Python"

print(type(language1)) # <class 'tuple'>
print(type(language2)) # <class 'tuple'>
print(type(language3)) # #<class 'str'>
```
Podemos também criar uma tupla com a função build-in **tuple**. Sem argumentos cria uma tupla vazia:

```python
frutas = tuple()
print(frutas) # ()
```

Se os argumentos forem uma sequência (string, lista ou tupla), o resultado é uma tupla com os elementos da sequência:

```python
console = 'xbox'
console = tuple(console)
print(console) # ('x', 'b', 'o', 'x')
```

A maior parte dos operadores de lista também funciona em tuplas. E o acesso aos elementos também pode ser feito através dos índices.
```python
console = 'xbox'
console = tuple(console)
print(console[2]) # o
```
Funcionando como listas, podemos fazer fatiamento

```python
console = 'xbox'
console = tuple(console)
print(console[1:-1]) # ('b', 'o')
```
Porém, se tentar-mos alterar um dos elementos de uma tupla, o programa exibirá uma mensagem de erro:
```python
console = 'xbox'
console = tuple(console)
console[0] =  "X"
'''
console[0] =  "X"
~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
```

Mas observe: Como tuplas são imutáveis, você não pode alterar os elementos, mas pode substituir uma tupla por outra:
```python
console = 'xbox'
console = tuple(console)
print(console) # ('x', 'b', 'o', 'x')

letra = "X",
console = letra + console[1:]
print(console) #('X', 'b', 'o', 'x')
```
A instrução acima faz uma nova tupla e então atribui (X) a console.

### Comparações

Os operadores relacionais funcionam com tuplas e outras sequências; o Python começa comparando o primeiro elemento de cada sequência. Se forem iguais, vai para os próximos elementos, e assim por diante, até que encontre elementos que sejam diferentes. Os elementos subsequentes não são considerados (mesmo se forem muito grandes)

```python
a = 1,2,3
b = 0,4,5
print(a < b)  # False

a = 1,2,3
b = 4,5
print(a < b) # True
```

## Tuplas com valores de retorno

Uma função só pode retornar um valor, mas se o valor for uma tupla, o efeito é o mesmo que retornar valores múltiplos. Por exemplo, se quiser-mos dividir dois números inteiros e calcular o quociente e o resto, não é eficiente calcular **(x/y)** e depois **(x%y)**. É melhor calcular ambos ao mesmo tempo.

A função build-in **divmod** toma dois argumentos e devolve uma tupla de dois valores: o quociente e o resto. Você pode guardar o resultado como uma tupla:

```python
divmod(7, 3)
print(divmod(7, 3)) #(2,1)

quociente, resto = divmod(7, 3)
print(quociente) # 2
print(resto)     # 1
```

## Função que retorna uma tupla
As funções **max** e **min** são funções build-in que encontram os maiores e menores elementos de uma sequência. Abaixo criaremos uma função que calcula ambos e retorna uma tupla de dois valores.

```python
def min_max(tupla):
    return min(tupla), max(tupla)

numeros = (1, 30, 21, 2, 9, 65, 34,)

menor, maior = min_max(numeros)

print(menor) # 1
print(maior) # 65
```

## Função Zip
É uma função built-in que recebe duas ou mais sequências e devolve uma lista de tuplas onde cada tupla contém um elemento de cada sequência. 
Exemplo:
```python
letras = "abcdef"
numeros = [1,2,3,4,5,6]

for pares in zip(letras, numeros):
    print(pares)

'''Resultado...
('a', 1)
('b', 2)
('c', 3)
('d', 4)
('e', 5)
('f', 6)
'''
```

Um **objeto zip** e um tipo de iterador, ou seja, qualquer objeto que se repete por uma sequência. Iteradores são semelhantes a listas de certa forma, mas, ao contrário de listas, não é possível usar um índice para selecionar um elemento de um iterador.

Se quiser usar operadores de lista e métodos, você pode usar um objeto zip para fazer uma lista:

```python
letras = "abcdef"
numeros = [1,2,3,4,5,6]

lista = list(zip(letras, numeros))
print(lista) #[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
```
O resultado é uma lista de tuplas, neste exemplo, cada tupla contém um caractere da string e o elemento correspondente da lista.

Se a sequências não forem do mesmo tamanh, o resultado tem o comprimento da mais curta:

### Oservação
A maioria dos métodos abordados em listas também funcionam em tuplas!