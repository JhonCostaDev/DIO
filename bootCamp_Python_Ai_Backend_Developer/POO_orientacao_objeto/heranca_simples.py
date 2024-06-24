class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print('Ligando Motor')
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto_1 = Motocicleta('Vermelha', 'XYZ-2525', 2)
# moto_1.ligar_motor()

carro = Carro("azul", "UND-4543", 4)

caminhao = Caminhao("Preto", "QTD-0950", 16, True)
print("\n")
print(moto_1)
print(carro)
print(caminhao)
print("\n")