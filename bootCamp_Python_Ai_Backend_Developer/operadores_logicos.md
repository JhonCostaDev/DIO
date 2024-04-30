# Operadores Lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.

Exemplo:
op_comparacao + op_logico + op_comparacao ...

# E / AND (and)

Retorna True se  duas ou mais expressões lógicas forem verdadeiras.
ex:
a = 5
b = 8

print(a < b and a <= 5)
>>> True


# OU / OR (or)

Retorna True se uma das expressões lógicas for verdadeiras.
ex:
a = 5
b = 8

print(a == 5 or a > b)
>>> True

# Operador de Negação NOT (not)

Retorna o inverso da operação lógica

ex

a = 5
b = 8

print(not a > b)
>>> True

# Parênteses como precedencia de Operadores lógicos

Comparações lógicas dentro de parênteses tem precedencia sobre as demais comparações. As comparações de mesma precedencia, são executadas da esquerda para direita.

ex:

a = 5
b = 8
c = 10

print()


