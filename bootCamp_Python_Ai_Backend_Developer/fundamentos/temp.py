# statement = "Apple"
# for letter in statement:
#    #print(letter)
   
#print(list(range(6)))
# for number in range(0, 51, 5):
#     print(number, end=", ")
# Multipli table 9
# count = 0
# for i in range(0, 91, 9):
    
#     print(f'9 X {count} = {i}')
#     count += 1

# opcao = -1
# while opcao != 0:
#     opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))
#     if opcao == 1:
#         print("Sacando ...")
#     elif opcao == 2:
#         print("Exibindo o extrato ...")
# else:
#     print("Obrigado por usar nosso sistema!")

# curso = "Python"
# print(curso.upper())
# print(curso.center(14, "*"))
# print(curso.upper())
# print(curso.lower())
# print(curso.title())

# print(".".join(curso))

nome = 'Pedro Vaz de Caminha'
idade = 59
profissao = 'Escrivão'

#print("Olá, me chamo %s, tenho %d e trabalho como %s na armada real Portuguesa"%(nome, idade, profissao))

#print("Olá, me chamo {}, tenho {} e trabalho como {} na armada real Portuguesa".format(nome, idade, profissao))

print(f'Olá, me chamo {nome}, tenho {idade} e trabalho como {profissao} na armada real Portuguesa')

PI = 3.14159
print(f'O valor de Pi é: {PI:.2f}') # O valor de Pi é: 3.14
print(f'O valor de Pi é: {PI:10.2f}') # O valor de Pi é:       3.14