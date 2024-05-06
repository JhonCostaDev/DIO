'''
number = int(input("Type a number\n"))


print(number)
print(number)
print(number)
print(number)


texto = input("Informe um texto:\n")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

# Função Range

print(list(range(4)))
print("=" * 50) 
# Utilizando Range com FOR

for number in range(11):
    print(number, end=", ")
print()    
# Tabuada 5
print("=" * 50)  
for number2 in range(0, 51, 5):
    print(number2, end=", ")

'''

# COMANDO WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))
    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")
else:
    print("Obrigado por usar nosso sistema!")