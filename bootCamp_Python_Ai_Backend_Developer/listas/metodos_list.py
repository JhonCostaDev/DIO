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
linguagens_baixo_nivel = ["Pascal", "assembly", "C"]

linguagens.extend(linguagens_baixo_nivel)

print(linguagens)

# .index - exibe o indice na lista da primeira ocorrencia de um item passado por argumento

print(linguagens.index("Pascal"))

# .pop() - quando passado sem argumento, remove o ultimo item da lista, com argumento numérico, removo o item do indice passado
 




