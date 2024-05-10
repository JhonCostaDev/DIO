saldo_conta = 0
saque_diario = 0
menu = """
    **********************
        Bem Vindo ao 
        
        PYTHON BANK
        
        Escolha umas das opções abaixo:
        
        [1] - Sacar
        [2] - Depositar
        [3] - Extrato
        [0] - Sair
        
    *********************
"""
while True:
    escolha = input(menu)
    
    if escolha == "1":
        saque = float(input("Digite o valor desejado\n"))
        if saque > 500:
            print("O valor solicitado utrapassa o limite por saque(R$ 500,00).\nTente Novamente!")
        elif saque_diario == 3:
            print("Limite diário de saques atingido\nTente Novamente amanhã!")

        elif saque > saldo_conta:
            print("Você não tem saldo suficiente para realizar essa operação!")
            #break
        else:
            saldo_conta -= saque
            print(f"Valor solicitado {saque}")
            saque_diario + 1
                    

        
    if escolha == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

print(escolha)
