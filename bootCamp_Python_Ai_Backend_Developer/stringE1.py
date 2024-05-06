#Maiúscula, Menúsculas e Título
nome = "jhon"
print(nome.upper())
print(nome.lower())
print(nome.title())

sentence = "the book is on the table!"
print(sentence.upper())
print(sentence.lower())
print(sentence.title())

# Eliminando espaços em branco

curso = "   Python  "
print(curso.strip() +".")
print(curso.lstrip()+".")
print(curso.rstrip()+".")

# Junção e centralização

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "*"))

#join
print(".".join(menu))

numbers = "123456789"
intNumbers = ", ".join(numbers)

print(intNumbers)



