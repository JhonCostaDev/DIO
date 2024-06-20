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
'''
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
print(aqui)'''
#def criar_conta():



clientes = [
    {'cpf': '828300193919', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841',
     'endereco': ['trvessa', '301', 'bom', 'fort', 'ceara']}
]


'''cpf = input('digite\n')
def verificar_cpf(list, cpf_number):
    print(cpf_number)
    if len(list) == 0:
        #return False
        print('zero')
    for cpf in list:
        if cpf.get('cpf') == cpf_number:
            #return False
            print('ja existe')
        else:
            #return True
            print('nao tem')

ja_cliente = verificar_cpf(clientes, cpf)

if ja_cliente:
verificar_cpf(clientes, cpf)
'''
'''contas = [{'agencia': '0001', 'conta': 0, 'saldo': 0, 'cpf': '82830019399'}]

print(contas[0].get('conta'))
contas[0]['conta'] = 1
print(contas[0].get('conta'))'''

'''clientes = [
    {'cpf': '82830019399', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841', 'endereco': ['trvessa', '301', 'bom', 'fort', 'ceara']},
    {'cpf': '12345678901', 'nome': 'João da Silva', 'data_nasc': '15/05/1980', 'telefone': '(11) 98765-4321', 'endereco': ['Av. das Palmeiras, 456', '456', 'jardim', 'sao pulo', 'sp']},
    {'cpf': '98765432109', 'nome': 'Maria Oliveira', 'data_nasc': '20/03/1995', 'telefone': '(21) 98765-4321', 'endereco': ['Rua das Flores, 123', '123', 'copacabana', 'rio de janeiro', 'rj']},
    {'cpf': '54321098765', 'nome': 'Carlos Santos', 'data_nasc': '10/11/1988', 'telefone': '(31) 98765-4321', 'endereco': ['Rua dos Pinheiros, 789', '789', 'bnanas', 'belo horizonte', 'MG']}
]

contas = [{'agencia': '0001', 'conta': 1, 'saldo': 0, 'cpf': '12345678901'},
          {'agencia': '0001', 'conta': 1, 'saldo': 0, 'cpf': '98765432109'},
          {'agencia': '0001', 'conta': 1, 'saldo': 0, 'cpf': '54321098765'}]'''

def clientes_cadastrados(lista_clientes, lista_contas):
    numero_clientes = len(lista_clientes)
    numero_contas = len(lista_contas)
    print(numero_contas)
    print(numero_clientes)
    if numero_clientes > 0 and numero_contas == 0:
        print('Nenhum dos clientes cadastrados tem uma conta ativa')
    elif numero_clientes == 0 or numero_contas == 0:
        print('Ainda não temos contas nem clientes cadastrados')
    else:
        for cliente in  lista_clientes:
            for conta in lista_contas:
                if cliente.get('cpf') == conta.get('cpf'):
                    print(f"""
                    Nome: {cliente.get('nome')}
                    CPF: {cliente.get('cpf')}
                    Conta: {conta.get('conta')}
                    Saldo: R$ {conta.get('saldo'):.2f}
""")



clientes = [
{'cpf': '82830019399', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841', 'endereco': ['trvessa', '301', 'bom', 'fort', 'ceara']},
{'cpf': '12345678901', 'nome': 'João da Silva', 'data_nasc': '15/05/1980', 'telefone': '(11) 98765-4321', 'endereco': ['Rua das Flores, 123', '123', 'bom', 'sao paulo', 'sp']},
{'cpf': '98765432109', 'nome': 'Maria Oliveira', 'data_nasc': '20/03/1995', 'telefone': '(21) 98765-4321', 'endereco': ['Av. das Palmeiras, 456', '456', 'santa', 'Rio de Janeiro', 'Rio de Janeiro']},
{'cpf': '54321098765', 'nome': 'Carlos Santos', 'data_nasc': '10/11/1988', 'telefone': '(31) 98765-4321', 'endereco': ['Rua dos Pinheiros, 789', '789', 'otabio', ' Belo Horizonte', 'MG']}
]

contas = [
{'agencia': '0001', 'conta': '001', 'saldo': 1490, 'cpf': '82830019399'},
{'agencia': '0001', 'conta': '002', 'saldo': 4678, 'cpf': '12345678901'},
{'agencia': '0001', 'conta': '003', 'saldo': 16421, 'cpf': '98765432109'},
{'agencia': '0001', 'conta': '004', 'saldo': 300, 'cpf': '54321098765'}
]
'''clientes = []
contas = []'''
clientes_cadastrados(clientes, contas)