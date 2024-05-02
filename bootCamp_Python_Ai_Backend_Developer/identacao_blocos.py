def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print(f'Valor solicitado: {valor}')
        print("Retire o seu dinheiro abaixo!")
    else:
        print("Saldo insuficiente!!!")    
        
    print("Tenha um bom dia!")
    
    
sacar(1000)
