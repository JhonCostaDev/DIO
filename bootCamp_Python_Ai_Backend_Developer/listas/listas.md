# LISTAS
Uma listas refere-se a uma coleção de dados que estão normalmente relacionados.

Listas em python podem armazenar de maneira sequêncial qualquer tipo de objeto.

Pode-se criar listas usando o construtor **list**, a função **range** ou colocando valores separados por vírgula dentro de colchetes.

## Listas são mutáveis
Listas são objetos mutáveis, podendo ter seus elementos alterados.

Listas podem ser declaradas das seguintes formas:

**Exemplos de declaração de listas**

```python
#Lista declarada já com seus elementos
frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

#Lista declarada vazia
legumes = []

#Lista declarada através do construtor list, nesse caso o python reconece uma string como um iterável, então o construtor list atribui cada letra de uma string a uma posição na lista
letras = list("Python")

# Lista declarada através do construtor list e da funçao range, que criará uma lista com o números de 0 a 9.
numeros = list(range(10))

#Lista contendo elementos de diferentes tipos
carro = ["Chevette", "Alcool", "PMG6543", "Ceará", 1986, True]
```


## ACESSO DIRETO

Valores individuais em uma lista são acessíveis através de seus índices, e os indices de uma lista sempre se iniciam em **0 (zero)**.

Quando o operador de colchete aparece ao lado esquerdo de uma atribuição, ele identifica o elemento da lista que será atribuido:

```python
frutas = []

frutas[0] = "laranja"   # laranja é atribuido a primeira posição da lista.
frutas[1] = "tomate"      # tomate é atribuida a segunda posição da lista.
frutas[1] = "maçã"      # tomate é substituído por maçã na segunda posição da lista.
```
```python
frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

frutas[0] # laranja //primeiro elemento 
frutas[2] # uva     //terceiro elemento
frutas[-1] # goiaba //indice negativo, sempre o último elemento.
```

Pode-se também atribuir a uma lista, ou parte dela a uma variável.

```python
frutas = ["laranja", "maçã", "uva", "pêra", "goiaba", "melância", "morango"]

minhas_frutas = frutas # "laranja", "maçã", "uva", "pêra", "goiaba", "melância", "morango"
frutas_verdes = [3:7] # "pêra", "goiaba", "melância"
```

Índices em listas funcionam da mesma forma que os índices de um String:
* Qualquer expressão de números inteiros pode ser usada como índice.
* Se tentar ler ou escrever um elemento que não existe, o programa retornará um **indexError**.
* Se um índice tiver um valor negativo, ele conta de trás para frente, a partir do final da lista.

## Listas Aninhadas

Podemos também criar listas aninhadas, que são estruturas bidimensionais(tabelas) e acessar seus elementos através dos índices de linhas e colunas.

```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]
letras = []
numeros = []

letras[0] = matriz[0][1]    # a
letras[1] = matriz[1][0]    # b
letras[2] = matriz[2][-1]   # c

print(letras) # ["a", "b", "c"]

numeros[0] = matriz[0][0]    # 1
numeros[1] = matriz[0][-1]   # 2
numeros[2] = matriz[1][1]    # 3
numeros[3] = matriz[1][2]    # 4
numeros[4] = matriz[2][1]    # 5
numeros[5] = matriz[2][0]    # 6

print(numeros) #[1, 2, 3, 4, 5, 6]
```
## OPERAÇÕES COM LISTAS
### Operador **IN**
 Retorna um boolean que testa se um elemento está em determinada lista:
```python
estados = ['Ce','Pe','Rj','Sp']
print("Ce" in estados) # True
print("Rs" in estados) # False
```
## FATIAMENTO / Slice

Além do acesso direto, podemos extrair um conjunto de valores de uma lista, passando o índice inicial e/ou final para acessar o conjunto. Pode-se ainda informar quantas posições/passo deve-se correr pela lista.

```python
linguagem = "Python"
linguagem = list(linguagem)

print(linguagem)        #['P', 'y', 't', 'h', 'o', 'n']
print(linguagem[2:])    #['t', 'h', 'o', 'n']
print(linguagem[:2])    #['P', 'y']
print(linguagem[1:3])   #['y', 't']
print(linguagem[:3:2])  #['P', 't']
print(linguagem[::])    #['P', 'y', 't', 'h', 'o', 'n']
print(linguagem[::-1])  #['n', 'o', 'h', 't', 'y', 'P']
```
## Iterar uma lista
A forma mais comum de iterar através de uma lista é utilizando a estrutura de repetição **for**:

```python
estados = ['Ce','Pe','Rj','Sp']

for estado in estados:
    print(estado)
'''
Ce
Pe
Rj
Sp
'''
```
Podemos ainda utilizar a o looping **for** com a estrutura **enumerate** que retornará os indices:

```python
estados = ['Ce','Pe','Rj','Sp']

for indice, estado in enumerate(estados):
    print(f'{indice}: {estado}')
'''
0: Ce
1: Pe
2: Rj
3: Sp
'''
```
## LIST COMPREHENSIONS
List Comprehension foi concebida na **PEP 202** e é uma forma concisa de criar e manipular listas. Oferece uma sintaxe mais curta quando deseja-se criar uma nova lista aplicando alguma modificação nos elementos de uma lista já existente.
Sua sintaxe básica é:
```python
[expressão for item in lista]
```

Como exemplo vamos criar uma lista com números de 1 a 10 elevados ao quadrado:
```python
#método tradicional
ao_quadrado = []
for numero in range(1, 11):
    ao_quadrado.append(numero**2)
print(ao_quadrado) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#  comprehensions
ao_quadrado = [numero ** 2 for numero in range(1, 11)]
print(ao_quadrado) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## MÉTODOS DE LISTAS

### .append
Adiciona um novo elemento ao final de uma lista:
```python
lista = []
lista.append(125)
lista.append("Python")
lista.append(True)

print(lista) # [125, 'Python', True]
```

### .clear
Limpa uma lista
```python
lista = [125, 'Python', True]
print(lista) # [125, 'Python', True]

lista.clear()
print(lista) #[]
```

### .copy
Copia uma lista
```python
lista = [125, 'Python', True]
lista2.copy(lista)
print(lista2) #[125, 'Python', True]
```

### .count
Retorna o número de vezes em que um elemento passado como argumento aparece em uma lista.
```python
cores = ["azul", "verde", "azul", "amarelo", "vermelho", "vermelho"]
print(cores.count("azul")) # 2
```

### .extend
Recebe uma lista como argumento e adiciona todos os elementos. Não elimina valores duplicados.

```python
letras1 = ['a', 'b', 'c', 'd']
letras2 = ['d', 'e', 'f']

letras1.extend(letras2)
print(letras1)  #['a', 'b', 'c', 'd', 'd', 'e', 'f']
```

### .index
Retorna a posição na lista da primeira ocorrência de um elemento passado por argumento. Se o elemento buscado não estiver na lista, retorna um erro de valor(ValueError: is not in list)
```python
letras1 = ['a', 'b', 'c', 'd']
letras2 = ['d', 'e', 'f']


print(letras1.index("c"))  # 2
print(letras1.index("g"))  # ValueError: 'g' is not in list
```

### .pop
Remove o último elemento da lista. Também pode remover um elemento pelo seu índice.

```python
frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

frutas.pop() # Remove "goiaba"
frutas.pop() # Remove "pêra"
frutas.pop(0) # Remove "laranja"
```

### .remove
Remove o elemento passado como argumento. Também retorna ValueError se o elemento passado não estiver na lista

```python

frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

frutas.remove("uva")
print(frutas) # ['laranja', 'maçã', 'pêra', 'goiaba']
```
### .reverse

Semelhante ao slice, realiza o espelhamento da lista

```python
linguagem = list("Python")

linguagem.reverse()
print(linguagem) # ['n', 'o', 'h', 't', 'y', 'P']
```
### .sort
Realiza o ordenamento de uma lista.
```python
letras = ['h', 'c', 'd', 'g', 'i', 'm',]
letras.sort()
print(letras) #['c', 'd', 'g', 'h', 'i', 'm']
letras.sort(reverse=True)
print(letras) # ['m', 'i', 'h', 'g', 'd', 'c']

# Ordenamento por tamanho da string

linguagens = ["Python", "Java", "JavaScript", "Pascal", "Assembly", "C"]
linguagens.sort(key=lambda x:len(x))
print(linguagens) # ['C', 'Java', 'Python', 'Pascal', 'Assembly', 'JavaScript']

```

### len( )
Retorna o tamanho de uma lista.
```python
linguagens = ["Python", "Java", "JavaScript", "Pascal", "Assembly", "C"]

print(len(linguagens)) # 6
```

### Função sorted( )
A função sorted () também permite ordenar arrays em Python. A diferença em relação ao método sort () é que a função sorted () cria uma nova lista ordenada, deixando o array original inalterado. Essa função é útil quando precisamos preservar o array original ou quando queremos ordenar uma sequência que não seja um array.

```python
numbers = [34, 1, 85, 9, 42, 23, 10, 45, 76, 11, 89, 5, 35, 57]

print(sorted(numbers)) # [1, 5, 9, 10, 11, 23, 34, 35, 42, 45, 57, 76, 85, 89]
print(numbers)
```