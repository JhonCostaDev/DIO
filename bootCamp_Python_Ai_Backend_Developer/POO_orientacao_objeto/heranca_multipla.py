class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorinco(Mamifero, Ave):
    pass


    
gato = Gato(nro_patas=4, cor_pelo='amarelo')
print(gato)

ornitorinco = Ornitorinco(nro_patas=4, cor_pelo='Marrom', cor_bico='Laranja')
print(ornitorinco)
