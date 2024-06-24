import re
class Carros:
    carro_1 = 'Gol, modelo 2016, completo'
    carro_2 = 'Celta, ano 2015, 4 portas'
    carro_3 = 'Uno, ano 2015, baixa quilometragem'
    carro_4 = 'Clio, 2018, flex, doc venido'

#print(Carros.carro_1)

#cadastro = re.split("\n+", text)

gol = re.split(", ", Carros.carro_1)
#print(gol)

# cachorro = 'Nego, pequeno porte, preto, 8.16kg'
# cachorro = re.split(", ", cachorro)
# print(cachorro)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    def imprimir(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')
        
pessoa_1 = Pessoa('Joao', 32)
pessoa_2 = Pessoa('Maria', 25)

pessoa_1.imprimir()

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def boas_vindas(self):
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario_1 = Usuario('jhon', 31)
usuario_1.boas_vindas()

# MANIPULAÇÃO: ALTERANDO DADOS DE UMA INSTÂNCIA
## Manipulação direta

usuario_1.nome = 'Tiririca'
usuario_1.idade = 50

usuario_1.boas_vindas()

## Manpulação via função:
setattr(usuario_1, 'nome', 'Homem-Aranha')

delattr(usuario_1, 'idade')
setattr(usuario_1, 'idade', 100)
usuario_1.boas_vindas()
