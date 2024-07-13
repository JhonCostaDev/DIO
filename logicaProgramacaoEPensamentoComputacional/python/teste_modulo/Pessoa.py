class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def printPessoa(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        