# myTyple = 1, 2, 5, 8,12, 3, 27

# print(type(myTyple))

# language = "Python"
# language2 = "Python",

# print(type(language)) # <class 'tuple'>

# frutas = tuple()
# print(frutas)

# console = 'xbox'
# console = tuple(console)
# #console[0] =  "X"

# letra = "X",
# console = letra + console[1:]
# print(console) # 

# meses_do_ano = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez",)

# for mes in meses_do_ano:
#     print(mes)

# a = 1,2,3
# b = 0,4,5
# print(a < b) 

# name = 'antonio luiz'

# firstName, secondName = name.split(' ')
# print(firstName)
# print(secondName)

#TUPLAS COM VALORES DE RETORNO

# divmod(7, 3)
# print(divmod(7, 3)) #(2,1)

# quociente, resto = divmod(7, 3)
# print(quociente) # 2
# print(resto)     # 1

#FUNÇÃO MIN-MAX

# def min_max(tupla):
#     return min(tupla), max(tupla)

# numeros = (1, 30, 21, 2, 9, 65, 34,)

# menor, maior = min_max(numeros)

# print(menor) # 1
# print(maior) # 65

# ZIP

letras = "abcdef"
numeros = [1,2,3,4,5,6]

# for pares in zip(letras, numeros):
#     print(pares)

lista = list(zip(letras, numeros))
print(lista)