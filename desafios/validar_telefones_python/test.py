#def valida_telefone(telefone):
import re

text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""

'''cadastro = re.split("\n+", text)

#[re.split(":? ", entry, 3) for entry in entries]
print([re.split(":? ", entry, 4) for entry in cadastro])
#print(nome)
for person in cadastro:
    print(person)

tel = '(88) 98888-8888'
print(tel)
tel_formatado = re.split(" ", tel, 3)
print(tel_formatado)'''

import re

# Padrão para números de telefone com 8 ou 9 dígitos (DDD + 8 ou 9 números)
pattern = r"^\([1-9]{2}\) (?:[2-8]|9[0-9])[0-9]{3}-[0-9]{4}$"

# Exemplo de uso
telefone = "(11) 98765-4321"
if re.match(pattern, telefone):
    print("Número de telefone válido!")
else:
    print("Número de telefone inválido.")