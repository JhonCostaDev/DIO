# Compreention v1
numeros = [1, 30, 21, 2, 9, 65, 34]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)

# Compreention v2

pares2 = [numero for numero in numeros if numero % 2 == 0]

print(pares2)
print("$" * 50)
# Modificando valores

numeros2 = [1, 30, 21, 2, 9, 65, 34]

quadrado = []

for numero in numeros2:
    quadrado.append(numero ** 2)
    
print(quadrado)

quadrado2 = [numero ** 2 for numero in numeros2]

print(quadrado2)





'''
for indice, numero in enumerate(numeros):
    print(numeros[indice])

print(numeros)


'''