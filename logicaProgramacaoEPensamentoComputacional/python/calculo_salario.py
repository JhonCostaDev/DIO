print("Calculo de Salário")

def calculo_imposto(salario):
    impostoFaixa1 = salario * 0.05
    impostoFaixa2 = salario * 0.1
    impostoFaixa3 = salario * 0.15
    
    if salario <= 1100:
        return salario - impostoFaixa1
    elif salario <= 2500:
        return salario - impostoFaixa2
    else:
       return salario - impostoFaixa3 
    

salario_bruto = float(input("Digite o valor em Reais (R$) do Salário Bruto:\n"))
beneficio = float(input("Digite o valor em Reais (R$) do Benefício:\n"))

salario_liquido = calculo_imposto(salario_bruto) + beneficio
print(salario_liquido)




