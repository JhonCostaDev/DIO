class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, parada=False):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.parada = parada
    
    def buzinar(self):
        print("Beeeee")
        
    def em_movimento(self):
        self.parada = True
    
    # Retornando valores da classe
    # Primeiro método
    #def __str__(self) -> str:
    #    return f"Bicicleta: Cor={self.cor}, Modelo={self.modelo}, ano={self.ano}, Valor={self.valor}"
   
    # Segundo método
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
        
## Instânciamento

bicicleta_azul = Bicicleta("azul", "monark", 1989, 1200)

bicicleta_vermerlha = Bicicleta('vermelha', "caloi", 1995, 1500, True)

bicicleta_azul.buzinar()

bicicleta_azul.em_movimento()
movimento = bicicleta_azul.parada

print(f"""
      RESUMO
      Modelo: {bicicleta_azul.modelo}
      Ano: {bicicleta_azul.ano}
      Valor: R$ {bicicleta_azul.valor:.2f}
      
      """)
if not movimento:
    print("Parando")
else:
    print("Vrummmm")
# Exibir valores retornados da classe 
print(bicicleta_vermerlha)
        