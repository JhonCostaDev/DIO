def menu_inicial():
    return input("""
        Python bank
        Digite a opção desejada:
        [1] - Acessar nossos serviços
        [2] - Cadastrar novo usuário
        [3] - Cadastrar nova conta
        [4] - Visualizar contas Cadastradas
        [0] - Sair
                """)

def menu_servicos():
    return input("""
        Python bank
        Digite a opção desejada:
        [1] - Saque
        [2] - Depósito
        [3] - Visualizar Extrato
        [0] - Voltar ao menu principal
                """)

def cadastrar_usuario(cpf_number):
    print("Cadastrar usuário")
    nome = input("Digite seu nome\n")
    data_nasc = input("Digite sua data de nascimento no formato(dia/mes/ano) APENAS NÚMEROS:\n")
    telefone = input('Digite seu telefone no formato (00-0.0000-0000) APENAS NÚMEROS:\n')

    logradouro = input("Digite seu endereço(Nome da rua):\n")
    numero_casa = input("Digite o número da residência APENAS NÚMEROS:\n")
    bairro = input('Digite o nome do bairro:\n')
    cidade = input("Digite o nome da cidade: \n")
    estado = input("Digite o nome do Estado: \n")

    cliente = {
        'cpf': cpf_number,
        'nome': nome,
        'data_nasc': data_nasc,
        'telefone': telefone,
        'endereco': [logradouro, numero_casa, bairro, cidade, estado]
    }
    return cliente

def recebe_cpf():
    while True:
        cpf = input('Digite os 11 dígitos do seu CPF (APENAS NÚMEROS):\n')
        e_numero = cpf.isdigit()
        quant_numeros_cpf = len(cpf)
        if e_numero and quant_numeros_cpf == 11:
            return cpf
            break
        else:
            print("Entrada Inválida\nDigite apenas numeros")
            print("Tentar Novamente? ")
            tentar_novamente = input("1 - Sim\n0 - Não\n")
            if tentar_novamente == '0':
                break


def verificar_cpf(list, cpf_number):
    print(cpf_number)
    cpf_ja_cadastrato = False
    if len(list) == 0:
        return False
    for cpf in list:
        if cpf['cpf'] == cpf_number: #if cpf.get('cpf') == cpf_number:
            cpf_ja_cadastrato = True

    return cpf_ja_cadastrato

def criar_conta(cpf_number, list):
    contas_na_lista = len(list)
    conta = {
        'agencia': '0001',
        'conta': '00' + str(contas_na_lista + 1),
        'saldo': 0,
        'cpf': cpf_number
    }

    return conta


def clientes_cadastrados(lista_clientes, lista_contas):
    numero_clientes = len(lista_clientes)
    numero_contas = len(lista_contas)

    if numero_clientes > 0 and numero_contas == 0:
        print('Nenhum dos clientes cadastrados tem uma conta ativa')
    elif numero_clientes == 0 or numero_contas == 0:
        print('Ainda não temos contas nem clientes cadastrados')
    else:
        for cliente in lista_clientes:
            for conta in lista_contas:
                if cliente.get('cpf') == conta.get('cpf'):
                    print(f"""
                        Nome: {cliente.get('nome')}
                        CPF: {cliente.get('cpf')}
                        Conta: {conta.get('conta')}
                        Saldo: R$ {conta.get('saldo'):.2f}
    """)


def sacar():
    print("Sacar")


def depositar():
    print("depositar")


def visualizar_extrato():
    print("Extrato")


def main():
    clientes = [
        {'cpf': '82830019399', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841',
         'endereco': ['trvessa', '301', 'bom', 'fort', 'ceara']},
        {'cpf': '12345678901', 'nome': 'João da Silva', 'data_nasc': '15/05/1980', 'telefone': '(11) 98765-4321',
         'endereco': ['Rua das Flores, 123', '123', 'bom', 'sao paulo', 'sp']},
        {'cpf': '98765432109', 'nome': 'Maria Oliveira', 'data_nasc': '20/03/1995', 'telefone': '(21) 98765-4321',
         'endereco': ['Av. das Palmeiras, 456', '456', 'santa', 'Rio de Janeiro', 'Rio de Janeiro']},
        {'cpf': '54321098765', 'nome': 'Carlos Santos', 'data_nasc': '10/11/1988', 'telefone': '(31) 98765-4321',
         'endereco': ['Rua dos Pinheiros, 789', '789', 'otabio', ' Belo Horizonte', 'MG']}
    ]
    #clientes = []
    #contas = []
    contas = [
        {'agencia': '0001', 'conta': '001', 'saldo': 1490, 'cpf': '82830019399'},
        {'agencia': '0001', 'conta': '002', 'saldo': 4678, 'cpf': '12345678901'},
        {'agencia': '0001', 'conta': '003', 'saldo': 16421, 'cpf': '98765432109'},
        {'agencia': '0001', 'conta': '004', 'saldo': 300, 'cpf': '54321098765'}
    ]
    opcao_menu_principal = menu_inicial()

    while opcao_menu_principal != '0':
        if opcao_menu_principal == '1':
            opcao_menu_servicos = int(menu_servicos())

            if opcao_menu_servicos == 1:
                sacar()
            elif opcao_menu_servicos == 2:
                depositar()
            elif opcao_menu_servicos == 3:
                visualizar_extrato()
            elif opcao_menu_servicos == 0:
                opcao_menu_principal = int(menu_inicial())
            else:
                print("Opcao invalida, tente novamente")

        elif opcao_menu_principal == '2':
            cpf = recebe_cpf()
            if cpf == None:
                opcao_menu_principal = int(menu_inicial())
            else:
                cadastrar = verificar_cpf(clientes, cpf)
                print(cadastrar)
                if cadastrar == False:
                    clientes.append(cadastrar_usuario(cpf))
                    print('Cliente Cadastrado com Sucesso')
                    opcao_menu_principal = int(menu_inicial())
                else:
                    print('Cliente já Cadastrado')
                    opcao_menu_principal = int(menu_inicial())

        elif opcao_menu_principal == '3':
            cpf = recebe_cpf()
            if cpf == None:
                opcao_menu_principal = menu_inicial()
            else:
                cadastrar = verificar_cpf(clientes, cpf)
                print(cadastrar)
                if cadastrar == True:
                    contas.append(criar_conta(cpf, contas))
                    print('Conta Criada com Sucesso')
                    opcao_menu_principal = menu_inicial()
                else:
                    print('CPF ainda não cadastrado')
                    opcao_menu_principal = menu_inicial()

        elif opcao_menu_principal == '4':
            clientes_cadastrados(clientes, contas)
            opcao_menu_principal = menu_inicial()
        else:
            print('Opção Inválida')
            opcao_menu_principal = menu_inicial()
    print(clientes)
    print(contas)
    print("Obrigado por utilizar nossos serviços")


main()
