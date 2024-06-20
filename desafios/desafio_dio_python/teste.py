'''import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()'''
'''clientes = [{'cpf': '828300193919', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841', 'endereco':
    ['trvessa', '301', 'bom', 'fort', 'ceara']}]

print(clientes[0]['cpf'])
print(f"CPF: {clientes[0].get('cpf')}")

def func(a):
    if a == 'a':
        return True
    else:
        return False

print(func('a'))
'''


'''def verificar_cpf(list, cpf_number):
    print(cpf_number)
    if len(list) == 0:
        return False
    for cpf in list:
        if cpf == cpf_number:
            return False
        else:
            return True

lista = [1234,5667,123411]

result = verificar_cpf(lista, 5667)
print(result)
print(len(lista))

while True:
    try:
        nota = int(input("Informe a nota entre 0 e 10: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break'''

'''cpf = input('digite\n')

print(cpf.isdigit())'''

def recebe_cpf():
    while True:
        cpf = input('Digite os 11 dígitos do seu CPF (APENAS NÚMEROS):\n')
        sonumero = cpf.isdigit()
        numeros_cpf = len(cpf)
        print(numeros_cpf)
        if sonumero and not numeros_cpf < 11:
            return cpf
            break
        else:
            print("Entrada Inválida\nDigite apenas numeros")

aqui = recebe_cpf()
print(aqui)