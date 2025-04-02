class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
    def buzinar(self):
        print("BIBI")
    
    def parar(self):
        print("Parando...")    
    
    def correr(self):
        print("Correndo...")
    
    #def __str__(self):
    #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    

B1 = Bicicleta("azul", "Caloi", 2020, 700)
B1.buzinar()
B1.parar()
B1.correr()
print(B1.cor, B1.modelo, B1.ano, B1.valor)

B2 = Bicicleta("vermelha", "Monark", 2000, 200)
print(B2)