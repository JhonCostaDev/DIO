# contatos = {
#     "joaozinho@gmail.com" : {"nome" : "joao", "telefone" : "3398-4587"},
#     "pedrinho@gmail.com" : {"nome" : "pedro", "telefone" : "3398-9863"},
#     "sofi@gmail.com" : {"nome" : "sophia", "telefone" : "3398-0247"},
#     "gabizinha@gmail.com" : {"nome" : "Gabriella", "telefone" : "3398-3620"},
# }

# # Acessando campos

# telefone = contatos["pedrinho@gmail.com"]["telefone"] # "3398-9863"
# print(telefone)

# ## Iterar dicionários

# #for chave in contatos:
#     #print(chave, contatos[chave])
    
# for chave, valor in contatos.items():
#     print(chave, valor)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}

motor = carro.get('motor')
print(motor)