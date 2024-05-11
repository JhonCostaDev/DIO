saldo_usuario = 10
saques_diario = 3
limite_por_saque = 500
registro_saques_depositos = ""

''''
def sacar():
	valor = float(input("Digite o valor do saque:\n"))
	if saques_diario == 0:
		print("Voce atingiu o limite maximo de saques por dia, tente novamente amanha!")
	elif valor > saldo_usuario:
		print("Saldo insuficiente")
	elif valor > limite_por_saque:
		print("Limite de saque diario(R$ 500,00) excedido!\nTente outro valor")
	else:
		saldo_usuario -= valor
		saques_diario -= 1
'''

menu = """
#############################
	Bem vindo ao
	Python Bank
#############################
Escolha uma das opcao abaixo

[1] - Sacar
[2] - Depositar
[3] - Extrato
[0] - Finalizar

#############################

"""
atendimento = True
while atendimento:
    operacao = input(menu)

    if operacao == "1":
        print("Sacar")
        valor = float(input("Digite o valor do saque:\n"))

        if saques_diario == 0:
            print("Voce atingiu o limite maximo de saques por dia, tente novamente amanha!")
        elif valor > saldo_usuario:
            print("Saldo insuficiente")
        elif valor > limite_por_saque:
            print("Limite de saque diario(R$ 500,00) excedido!\nTente outro valor")
        else:
            saldo_usuario -= valor
            saques_diario -= 1
            registro_saques_depositos += f"Saque: R${valor:.2f}\n"
            print(f"Saque no valor de {valor:.2f} Realizado!\nRetire o valor abaixo!")

            outra_operacao = input("""
Deseja Realizar outra operacao?
		[1]- SIM
		[0]-NAO
			""")

            if outra_operacao == "0":
                print("Obrigado por utilizar nossos servicos")
                atendimento = False
            else:
                continue


    elif operacao == "2":
        print("Deposito")
        deposito = float(input("Qual o valor R$ do depósito: \n"))

        if deposito < 0:
            print("Valor inválido")
            print("Tente Novamente!")

        saldo_usuario += deposito
        registro_saques_depositos += f"Depósito no valor de R${deposito:.2f}\n"
        print(f"Depósito no valor de R${deposito:.2f} realizado com sucesso!")

        outra_operacao = input("""
        Deseja Realizar outra operacao?
        		[1]- SIM
        		[0]-NAO
        			""")

        if outra_operacao == "0":
            print("Obrigado por utilizar nossos servicos")
            atendimento = False
        else:
            continue


    elif operacao == "3":
        print("Extrato")
        print(f"Últimas Movimentações\n{registro_saques_depositos}")

        print(f"Saldo atual é de: {saldo_usuario:.2f}")

        outra_operacao = input("""
                Deseja Realizar outra operacao?
                		[1]- SIM
                		[0]-NAO
                			""")

        if outra_operacao == "0":
            print("Obrigado por utilizar nossos servicos")
            atendimento = False
        else:
            continue

    elif operacao == "0":
        print("Obrigado por utilizar nossos servicos")
        atendimento = False

    else:
        print("Opcao invalida, Tente Novamente!")

print(registro_saques_depositos)
