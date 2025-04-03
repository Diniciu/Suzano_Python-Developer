"""
Herança é um dos pilares da Programação Orientada a Objetos (POO) e permite que uma classe (chamada de classe derivada ou subclasse) herde atributos e métodos de outra classe 
(chamada de classe base ou superclasse). Isso promove a reutilização de código e a criação de hierarquias de classes.

Aqui está um exemplo básico de herança em Python:
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Miau!"

# Criando instâncias das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

print(cachorro.fazer_som())  # Output: Rex diz: Au Au!
print(gato.fazer_som())      # Output: Mimi diz: Miau!

"""
Neste exemplo:

° A classe Animal é a superclasse com um método fazer_som que é sobrescrito nas subclasses.
° As classes Cachorro e Gato herdam de Animal e implementam o método fazer_som de maneira específica para cada tipo de animal.
° Instâncias de Cachorro e Gato são criadas e seus métodos fazer_som são chamados, demonstrando a herança e a sobrescrita de métodos.
"""