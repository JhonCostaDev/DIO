# append - Adicionar ao último posição da lista
lista = []

lista.append(1)
lista.append("Python")
lista.append(["laranja", "maçã", "uva", "pêra", "goiaba"])

print(lista)

# Copy - cria uma cópia exata da lista em outro local de memória.

lista_copy = lista.copy()
print(lista_copy)
# CLEAR - limpar a lista

lista_copy.clear()
print(lista)
print(lista_copy)

# .count - Utilizado para contar quantas vezes determinado objeto aparece em uma lista

cores = ["azul", "verde", "azul", "amarelo", "vermelho", "vermelho"]

print(cores.count("azul"))
print(cores.count("verde"))
print(cores.count("amarelo"))
print(cores.count("vermelho"))

# .externd - juntar listas

linguagens = ["Python", "Java", "JavaScript"]
linguagens_baixo_nivel = ["Pascal", "Assembly", "C"]

linguagens.extend(linguagens_baixo_nivel)

print(linguagens)

# .index - exibe o indice na lista da primeira ocorrencia de um item passado por argumento

print(linguagens.index("Pascal"))
print("#" * 50)
# .pop() - quando passado sem argumento, remove o ultimo item da lista, com argumento numérico, remove o item do indice passado

#TODO Buscar solução para remoção de itens iguais
cores2 = ["azul", "verde", "azul", "amarelo", "vermelho", "vermelho", "vermelho"]
print(cores2)
cores2.pop() # vermelho
cores2.pop(3) # amarelo

print("#" * 50)

# REMOVE - Remove um item da lista passado por argumento, remove sempre a primeria ocorrência do item passado por argumento.

cores2.remove("vermelho")
print(cores2)



# REVERSE - ESPELHAMENTO DA LISTA.

print(linguagens)

linguagens.reverse()

print(linguagens)

#SORT - ORDENAMENTO

numbers = [34, 1, 85, 9, 42, 23, 10, 45, 76, 11, 89, 5, 35, 57]
print(numbers)
numbers.sort()
print(numbers)

linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)