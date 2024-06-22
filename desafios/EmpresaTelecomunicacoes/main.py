# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(user_consumo):
    plano_1= 10
    plano_2 = 20
    if user_consumo <= plano_1:
        return "Plano Essencial Fibra - 50Mbps"
    elif user_consumo <= plano_2:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"


# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input('Informe seu consumo'))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))