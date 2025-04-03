# Herança Simples

# Na herança simples, uma classe herda de uma única classe base.
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} diz: Au Au!"

# Exemplo de uso
cachorro = Cachorro("Rex")
print(cachorro.falar())  # Output: Rex diz: Au Au!

#Herança Múltipla

# Na herança múltipla, uma classe pode herdar de mais de uma classe base.
class Mamifero:
    def __init__(self, nome):
        self.nome = nome

    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        return f"{self.nome} está voando."

class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        Mamifero.__init__(self, nome)
        Ave.__init__(self, nome)

# Exemplo de uso
morcego = Morcego("Bruce")
print(morcego.amamentar())  # Output: Bruce está amamentando.
print(morcego.voar())       # Output: Bruce está voando.

"""
Esses exemplos mostram como implementar herança simples e múltipla em Python. A herança simples é mais comum e fácil de gerenciar, 
enquanto a herança múltipla pode ser útil em casos específicos, mas deve ser usada com cuidado para evitar complexidade excessiva.
"""