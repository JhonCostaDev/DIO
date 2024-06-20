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

def cadastrar_usuario(cpf_number):
	print("Cadastrar usuário")
	nome = input("Digite seu nome\n")
	data_nasc = input("Digite sua data de nascimento:\n")
	telefone = input('Digite seu telefone:\n')

	cliente = {
		'cpf' : cpf_number,
		'nome' : nome,
		'data_nasc' : data_nasc,
		'telefone' : telefone
	}
	return cliente



def verificar_cpf(list, cpf_number):
	for cpf in list:
		print(cpf)


def criar_conta():
	print("Cadastrar conta")


#def repetir():

def sacar():
	print("Sacar")

def depositar():
	print("depositar")

def visualizar_extrato():
	print("Extrato")



def main():
	clientes = []
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
			cpf = input('Digite o seu CPF:\n')
			verificar_cpf(clientes, cpf)

			clientes.append(cadastrar_usuario(cpf))
			#print(clientes)
			break
		elif opcao_menu_principal == 3:
			criar_conta()
			break

	print("Obrigado por utilizar nossos serviços")

	

main()