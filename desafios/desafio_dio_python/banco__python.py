def menu_inicial():
    return input("""
        Python bank
        Digite a opção desejada:
        [1] - Acessar nossos serviços
        [2] - Cadastrar novo usuário
        [3] - Cadastrar nova conta
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


#O campo endereço deve ser uma string com o formato: logradouro, numero - bairro - cidade / UF.
def cadastrar_usuario(cpf_number):
    print("Cadastrar usuário")
    nome = input("Digite seu nome\n")
    data_nasc = input("Digite sua data de nascimento:\n")
    telefone = input('Digite seu telefone:\n')

    logradouro = input("Digite seu endereço(Nome da rua):\n")
    numero_casa = input("Digite o número da residência:\n")
    bairro = input('Digite o bairro:\n')
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
    if len(list) == 0:
        return False
    for cpf in list:
        if cpf.get('cpf') == cpf_number:
            return True
        else:
            return False

def criar_conta():
    conta = {
        'agencia': '0001',
        'conta': 0
    }
    return conta 


# def repetir():

def sacar():
    print("Sacar")


def depositar():
    print("depositar")


def visualizar_extrato():
    print("Extrato")


def main():
    clientes = [{'cpf': '828300193919', 'nome': 'jhon', 'data_nasc': '98-938-2341', 'telefone': '83841903841',
                 'endereco': ['trvessa', '301', 'bom', 'fort', 'ceara']}]
    #clientes = []
    contas = []

    opcao_menu_principal = int(menu_inicial())

    while opcao_menu_principal != 0:
        if opcao_menu_principal == 1:
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


        elif opcao_menu_principal == 2:
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

        elif opcao_menu_principal == 3:
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

    print(clientes)
    print("Obrigado por utilizar nossos serviços")


main()
