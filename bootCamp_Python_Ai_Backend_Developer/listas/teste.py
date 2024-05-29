# O QUE ISSO FAZ?

#num = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

#print(num)
#numeros = list(range(10))

# frutas = ["laranja", "maçã", "cereja", "uva", "pêra", "goiaba", "melância", "morango"]
# frutasVerdes = []
# #frutasVerdes = frutas[4:7]

# frutasVerdes.append(frutas[4])
# frutasVerdes.append(frutas[5])
# frutasVerdes.append(frutas[6])
# print(type(frutasVerdes))
# print(frutasVerdes)
# # essa atribuição transformará a variável frutasVerdes2 em uma tupla
# frutasVerdes2 = frutas[3], frutas[4], frutas[5]
# print(type(frutasVerdes2))
# print(frutasVerdes2)
# frutasVerdes2 = list(frutasVerdes2)
# print(type(frutasVerdes2))
# print(frutasVerdes2)

#print(frutasVermelhas)

# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "c"],
# ]
# abc = []
# abc = matriz[0][1], matriz[1][0], matriz[2][2]

# print(type(abc))

# minha_lista = [1, 2, 3]
# minha_outra_lista = minha_lista
# minha_outra_lista2 = minha_lista[:1]

# print(type(minha_outra_lista))
# print(type(minha_outra_lista2))

# minhasFrutas = frutas[1:5]
# print(type(minhasFrutas))
# print(minhasFrutas)
#----------------------------------------------------------
#OPERADOR IN
# estados = ['Ce','Pe','Rj','Sp']
# print("Ce" in estados) # True
# print("Rs" in estados) # False

#--------FATIAMENTO------------------------------------------
# linguagem = "Python"
# linguagem = list(linguagem)

# print(linguagem[2:])    #['t', 'h', 'o', 'n']
# print(linguagem[:2])    #['P', 'y']
# print(linguagem[1:3])   #['y', 't']
# print(linguagem[:3:2])  #['P', 't']
# print(linguagem[::])    #['P', 'y', 't', 'h', 'o', 'n']
# print(linguagem[::-1])  #['n', 'o', 'h', 't', 'y', 'P']

estados = ['Ce','Pe','Rj','Sp']

# for indice, estado in enumerate(estados):
#     print(f'{indice}: {estado}')
# i = 0
# while(i < len(estados)):
#     print(f'{i + 1} : {estados[i]}')
#     i +=1
 #   COMPREHENSION
# ao_quadrado = []
# for numero in range(1, 11):
#     ao_quadrado.append(numero**2)
    
# print(ao_quadrado)

# ao_quadrado2 = [numero ** 2 for numero in range(1, 11)]
# print(ao_quadrado2)

#APPEND

# lista = []
# lista.append(125)
# lista.append("Python")
# lista.append(True)

# print(lista)
# #lista.clear()
# lista2 = lista.copy()
# print(lista2)

# COunt
# cores = ["azul", "verde", "azul", "amarelo", "vermelho", "vermelho"]

# print(cores.count("azul"))

#EXTEND

# letras1 = ['a', 'b', 'c', 'd']
# letras2 = ['d', 'e', 'f']

# letras1.extend(letras2)

# print(letras1.index('g'))

# Pop
# frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]

# frutas.remove("uva")
# print(frutas)

#REVERSE
# linguagem = list("Python")

# linguagem.reverse()
# print(linguagem)

#SORT
# letras = ['h', 'c', 'd', 'g', 'i', 'm',]
# letras.sort()
# print(letras)
# letras.sort(reverse=True)
# print(letras)

# linguagens = ["Python", "Java", "JavaScript", "Pascal", "Assembly", "C"]
# linguagens.sort(key=lambda x:len(x))
# print(len(linguagens))

# FUNÇÃO SORTED
numbers = [34, 1, 85, 9, 42, 23, 10, 45, 76, 11, 89, 5, 35, 57]

print(sorted(numbers))
print(numbers)