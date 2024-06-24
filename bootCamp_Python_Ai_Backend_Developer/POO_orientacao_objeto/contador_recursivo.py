def contar_a_dez(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    contar_a_dez(maximo, atual + 1)

#contar_a_dez(11, 1)

# Refindado

def contar_a_dez_refinado(maximo, atual):
    if atual <= maximo:
        print(atual)
        contar_a_dez_refinado(maximo, atual + 1)
        
        
contar_a_dez_refinado(10, 1)        