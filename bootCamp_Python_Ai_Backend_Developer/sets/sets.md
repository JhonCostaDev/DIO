# Conjuntos / Sets
 Um set é uma coleção que não possui elementos repetidos, usado para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável. São bastantes úteis quando se precisa garantir que não haverá itens duplicados na sua coleção.

```python
numeros = [5, 19, 8, 5, 43, 10, 19, 43]  
print(numeros) # [5, 19, 8, 5, 43, 10, 19, 43]

numeros = set(numeros)
print(numeros) # {5, 8, 10, 43, 19}
```
**OBS**
Set não garante a ordem de origem

## Acessando os Dados
Conjuntos / sets em python não suportam indexação e nem fatiamento, ou seja, não é possível acessar seus elementos como feito comumente com listas e tuplas. Para realizar a minupulação de elemtos em um objeto set, deve-se primeiro convertê-lo para uma lista.

```python
carros_populares = {
    "Volkswagen Polo",
    "Chevrolet Onix",
    "Hyundai HB20",
    "Chevrolet Onix Plus",
    "Fiat Mobi",
    "Fiat Argo",
    "Renault Kwid",
    "Fiat Cronos",
    "Peugeot 208",
    "Hyundai HB20S"
}
print(type(carros_populares)) # <class 'set'>
print(carros_populares[0]) #TypeError: 'set' object is not subscriptable

carros_populares = list(carros_populares)
print(carros_populares[0])  # Chevrolet Onix Plus


#Embora seja possível iterar pelos elementos de um set com **for in**:

for carro in carros_populares:
    print(carro)
```

```python
carros
```
## Métodos da classe Set

### .union
Mescla um set a outro

```python
a = {1, 3, 5}
b = {2, 4, 5}

ab = a.union(b)

print(ab) #{1, 2, 3, 4, 5}

vogais = {"a", "e", "i", "o", "u"}
consoantes = {"b", "c", "d", "f", "g"}

letras = vogais.union(consoantes)
print(letras) # {'b', 'f', 'o', 'e', 'u', 'i', 'c', 'd', 'a', 'g'}
```

### .intersection
Cria um set com a interseção de outros dois sets, ou seja, os elementos que se repetem nos dois conjuntos.
```python
frutas1 = {"laranja", "maçã", "uva", "pêra", "goiaba"}
frutas2 = {"Tangerina", "maçã", "banana", "pêra", "tomate"}

frutas_repetidas = frutas1.intersection(frutas2)
print(frutas_repetidas) #{'maçã', 'pêra'}
```

### .difference
Cria um set com tudo presente em um conjunto que não está no outro.

```python
frutas1 = {"laranja", "maçã", "uva", "pêra", "goiaba"}
frutas2 = {"Tangerina", "maçã", "banana", "pêra", "tomate"}

frutas_different = frutas1.difference(frutas2)
print(frutas_different) # {'goiaba', 'uva', 'laranja'}

frutas_different2 = frutas2.difference(frutas1)
print(frutas_different2) # {'banana', 'tomate', 'Tangerina'}
```
### .issubset
Retorna um **boolean** se todos os elementos de um set estiverem em outro set.
```python
a = {2, 9, 12}
b = {1, 2, 5, 7, 9, 12, 25}

print(a.issubset(b)) # True
print(b.issubset(a)) # False
```

### .issuperset
O contrário de issubset
```python
a = {2, 9, 12}
b = {1, 2, 5, 7, 9, 12, 25}

print(a.issubset(b)) # True
print(a.issuperset(b)) # False
```
### .isdisjoint
Quando nenhum elemento de um set está no outro
```python
lista = {"molho", "milho", "ovos"}
carrinho = {"água", "arroz", "carne"}
print(lista.isdisjoint(carrinho)) # True

#------------------------------------------
lista = {"molho", "milho", "ovos", "arroz"}
carrinho = {"água", "arroz", "carne"}
print(lista.isdisjoint(carrinho))# False
```

### .add
Adiciona um elemento a um set se ele já não existir no mesmo.
```python
carrinho = {"água", "arroz", "carne"}

carrinho.add("Biscoito") 
print(carrinho) # {'arroz', 'água', 'carne', 'Biscoito'}
```

### .clean
Limpa um set
```python
carrinho = {"água", "arroz", "carne"}

print(carrinho) # set()
```

### .copy
Copia um set

```python
roupas_sujas = {"boné", "Camiseta", "tênis"}
roupas_limpas = roupas_sujas.copy()

print(roupas_limpas) # {'tênis', 'Camiseta', 'boné'}
#não garante a ordem
```

### .discard
Remove um elemento do set 
```python
lista = {"molho", "milho", "ovos", "arroz"}
lista.discard("molho")

print(lista) # {'milho', 'arroz', 'ovos'}
```
### .pop
Exclusivamente em set, remove o primeiro elemento de um conjunto!
Remove um elemento do set 
```python
numeros = {1, 2, 5, 7, 9, 12, 25}
print(numeros.pop()) # 1
```

### .remove
Remove o elemento passado por argumento
```python
lista = {"molho", "milho", "ovos", "arroz"}
lista.remove("ovos")
print(lista) # {'milho', 'arroz', 'molho'}
# Obs: Se o elemento não existir, o programa retorna um erro
lista.remove("feijão")
#KeyError: 'feijão'
```
### len()
Retorna o numeros de elementos do set
```python
lista = {"molho", "milho", "ovos", "arroz"}

print(len(lista)) # 4
```

### in
Verifica se um elemento está no set
```python
lista = {"molho", "milho", "ovos", "arroz"}
print("ovos" in lista) # True
```