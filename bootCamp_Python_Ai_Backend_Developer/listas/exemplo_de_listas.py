# DECLARAÇÃO DE LISTAS


frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

legumes = []

#letras = list("Python")

numeros = list(range(10))

carro = ["Chevette", "Alcool", "PMG6543", "Ceará", 1986, True]
# TODO: SEPARAR MATRIZ POR TIPOS NUMERICOS E ORDENAR

'''
# ACESSO DIRETO 
print(frutas[0]) # laranja
print(frutas[3]) # pêra

# ACESSO INDICES NEGATIVOS 
print(frutas[-1]) # GOIABA
print(frutas[-3]) # UVA
'''
# TODO: SEPARAR MATRIZ POR TIPOS NUMERICOS E ORDENAR

# LISTAS ANINHADAS -  BIDIMENSIONAIS / TABELAS

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]
abc = matriz[0][1] + matriz[1][0] + matriz[2][2]
print(abc) # abc



# FATIAMENTO

palavra = "Fatiamento"
letras = list(palavra)

print(letras[2 :]) # ['t', 'i', 'a', 'm', 'e', 'n', 't', 'o']
print(letras[: 2]) # ['F', 'a']
print(letras[1 : 3]) # ['a', 't']
print(letras[0 : 3 : 2]) # ['F', 't']
print(letras[::]) # ['F', 'a', 't', 'i', 'a', 'm', 'e', 'n', 't', 'o']
print(letras[:: -1]) # ['o', 't', 'n', 'e', 'm', 'a', 'i', 't', 'a', 'F']


print("#"* 50)
# COMANDO FOR

motos = ["Titan", "Intruder", "YBR", "Virago", "Yes", "Fan", "Falcon",]

#for moto in motos:
    #print(moto)
    
# Enumerate
for indice, moto in enumerate(motos):
    print(f"{indice + 1}: {moto}")



