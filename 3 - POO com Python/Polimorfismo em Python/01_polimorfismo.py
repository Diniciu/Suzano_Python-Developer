"""
Polimorfismo é um conceito fundamental na programação orientada a objetos que permite que objetos de diferentes classes sejam tratados de maneira uniforme. 
Em outras palavras, o polimorfismo permite que uma única interface seja usada para representar diferentes tipos de objetos.

Existem dois tipos principais de polimorfismo:

    1. Polimorfismo de Sobrecarga (Overloading): Permite que várias funções ou métodos tenham o mesmo nome, 
    mas com diferentes assinaturas (diferentes tipos ou números de parâmetros).

    2. Polimorfismo de Subtipo (Subtyping): Permite que uma classe derivada (subclasse) seja tratada como se fosse uma classe base (superclasse). 
    Isso é frequentemente realizado através de herança e interfaces.

Em Python, o polimorfismo é frequentemente implementado através de métodos que podem ser redefinidos em subclasses. Aqui está um exemplo simples:
"""
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

def emitir_som(animal):
    print(animal.fazer_som())

cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)  # Saída: Latido
emitir_som(gato)      # Saída: Miau

"""
Neste exemplo, tanto Cachorro quanto Gato são subclasses de Animal e redefinem o método fazer_som. A função emitir_som pode aceitar qualquer
objeto que seja uma instância de Animal ou suas subclasses, demonstrando o polimorfismo em ação.
"""