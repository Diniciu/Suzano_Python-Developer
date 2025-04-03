class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo instância...")
    
    def comunicar(self):
        print("Au au!")

def criar_cachorro():
    cao = Cachorro("Pentium", "Branco", False)
    print(cao.nome)

# cao = Cachorro("Celeron", "Preto")
# cao.comunicar()

criar_cachorro()