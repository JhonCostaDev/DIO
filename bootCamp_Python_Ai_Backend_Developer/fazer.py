#faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso. 
# EXEMPLO: Data 01/01/2024, ===>  01 de janeiro de 2024.

dia = 22
mes = 5
ano = 2024

def imprime_data_formatada(dia, mes, ano):
    mes_formatato = ""
    if mes == 1:
        mes_formatato = "Janeiro"
    elif mes == 2:
        mes_formatato = "Fevereiro"
    elif mes == 3:
        mes_formatato = "Marco"
    elif mes == 4:
        mes_formatato = "Abril"
    elif mes == 5:
        mes_formatato = "Maio"
    elif mes == 6:
        mes_formatato = "Junho"
    elif mes == 7:
        mes_formatato = "Julho"
    
    
    print(f"{dia} de {mes_formatato} de {ano}") 


imprime_data_formatada(dia, mes, ano)
    

