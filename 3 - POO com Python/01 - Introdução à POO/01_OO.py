"""
A Orientação a Objetos (O.O) é um paradigma de programação que utiliza "objetos" para representar dados e métodos. Esses objetos são instâncias de "classes", 
que definem as propriedades (atributos) e comportamentos (métodos) que os objetos criados a partir delas terão. 
A O.O. facilita a organização e a modularização do código, promovendo a reutilização e a manutenção.

Os principais conceitos da Orientação a Objetos são:

Classe: Um molde ou modelo a partir do qual objetos são criados. Define atributos e métodos.
Objeto: Uma instância de uma classe. Representa uma entidade concreta com estado e comportamento.
Encapsulamento: Esconde os detalhes internos de um objeto e expõe apenas o necessário através de métodos públicos.
Herança: Permite que uma classe herde atributos e métodos de outra classe, promovendo a reutilização de código.
Polimorfismo: Permite que diferentes classes sejam tratadas através da mesma interface, geralmente através de métodos com o mesmo nome mas comportamentos diferentes.
Aqui está um exemplo básico de como esses conceitos são implementados em Python:
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Criando objetos
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

print(cachorro.fazer_som())  # Saída: Au Au
print(gato.fazer_som())      # Saída: Miau

"""
Neste exemplo, Animal é a classe base, e Cachorro e Gato são classes derivadas que herdam de Animal. 
Cada classe derivada implementa o método fazer_som de maneira diferente, demonstrando polimorfismo.
"""