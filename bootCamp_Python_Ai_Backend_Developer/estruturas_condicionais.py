# IF
MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

print("********* IF *************")
idade = int(input("Informe sua idade:\n"))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")
    
###############################################

# IF/ELSE
print("********* IF - ELSE *************")
idade2 = int(input("Informe sua idade:\n"))

if idade2 >= 18:
    print("Maior de idade, pode tirar a CNH")
    
else:
    print("Ainda não pode tirar a CNH")
    
#------------------------------------------------

print("********* ELIF *************")
idade3 = int(input("Informe sua idade:\n"))

if idade3 >= 18:
    print("Maior de idade, pode tirar a CNH")
    
elif idade3 == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")
    
