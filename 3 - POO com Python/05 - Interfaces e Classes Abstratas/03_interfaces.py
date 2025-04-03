"""
Interfaces são contratos que definem um conjunto de métodos que uma classe deve implementar. Em Python, as interfaces são geralmente implementadas usando classes abstratas da 
biblioteca abc (Abstract Base Classes). Uma interface especifica o que uma classe deve fazer, mas não como ela deve fazer. Isso permite que 
diferentes classes implementem a interface de maneiras variadas, proporcionando flexibilidade e polimorfismo.

Aqui está um exemplo básico de como definir e usar uma interface em Python:
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Uso das classes
cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())  # Saída: Au Au
print(gato.fazer_som())      # Saída: Miau

"""
No exemplo acima, Animal é uma interface que define o método fazer_som. As classes Cachorro e Gato implementam essa interface fornecendo suas próprias versões do método fazer_som.
"""