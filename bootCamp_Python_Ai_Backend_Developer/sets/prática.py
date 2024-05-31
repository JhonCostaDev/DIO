# numeros = [5, 19, 8, 5, 43, 10, 19, 43]
# print(numeros)

# numeros = set(numeros)
# print(numeros)

# carros_populares = {
#     "Volkswagen Polo",
#     "Chevrolet Onix",
#     "Hyundai HB20",
#     "Chevrolet Onix Plus",
#     "Fiat Mobi",
#     "Fiat Argo",
#     "Renault Kwid",
#     "Fiat Cronos",
#     "Peugeot 208",
#     "Hyundai HB20S"
# }
# carros_populares = list(carros_populares)
# print(type(carros_populares)) # <class 'set'>

# print(carros_populares[0]) #TypeError: 'set' object is not subscriptable

# for carro in carros_populares:
#     print(carro)


# UNION

# a = {1, 3, 5}
# b = {2, 4, 5}

# ab = a.union(b)

# print(ab) #{1, 2, 3, 4, 5}

# vogais = {"a", "e", "i", "o", "u"}
# consoantes = {"b", "c", "d", "f", "g"}

# letras = vogais.union(consoantes)
# print(letras) # {'b', 'f', 'o', 'e', 'u', 'i', 'c', 'd', 'a', 'g'}

# INTERSECTION

# frutas1 = {"laranja", "maçã", "uva", "pêra", "goiaba"}
# frutas2 = {"Tangerina", "maçã", "banana", "pêra", "tomate"}

# frutas_repetidas = frutas1.intersection(frutas2)
# #print(frutas_repetidas) #{'maçã', 'pêra'}

# frutas_different = frutas1.difference(frutas2)
# print(frutas_different)
# frutas_different2 = frutas2.difference(frutas1)
# print(frutas_different2)

# ISSUBSET

# a = {2, 9, 12}
# b = {1, 2, 5, 7, 9, 12, 25}

# print(a.issubset(b)) # True
# print(b.issubset(a)) # False

# print(a.issuperset(b))

# ISDISJOINT

# lista = {"molho", "milho", "ovos", "arroz"}
# carrinho = {"água", "arroz", "carne"}
# print(lista.isdisjoint(carrinho))

# carrinho.add("Biscoito")
# print(carrinho)
# carrinho.clear()
# print(carrinho)

# COPY

# roupas_sujas = {"boné", "Camiseta", "tênis"}
# roupas_limpas = roupas_sujas.copy()

# print(roupas_limpas) # {'tênis', 'Camiseta', 'boné'}
# #não garante a ordem
 
# DISCARD

# lista = {"molho", "milho", "ovos", "arroz"}
# lista2 = lista.pop()

# print(lista2) # {'milho', 'arroz', 'ovos'}


# numeros = {1, 2, 5, 7, 9, 12, 25}
# print(numeros.pop())

# REMOVE
lista = {"molho", "milho", "ovos", "arroz"}
# lista.remove("feijão")
# print(lista) # {'milho', 'arroz', 'molho'}

print(len(lista)) # 4
print("ovos" in lista)