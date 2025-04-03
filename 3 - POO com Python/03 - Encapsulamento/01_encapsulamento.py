"""
Encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO). Ele se refere à prática de restringir o acesso direto a alguns dos componentes de um objeto, 
o que significa que os detalhes internos do objeto são escondidos do mundo exterior. Em Python, isso é geralmente feito usando convenções de nomenclatura para indicar que certos 
atributos ou métodos são privados e não devem ser acessados diretamente fora da classe.

Em Python, você pode usar um sublinhado (_) antes do nome de um atributo ou método para indicar que ele é protegido (não deve ser acessado diretamente fora da classe ou subclasses). 
Para tornar um atributo ou método privado, você pode usar dois sublinhados (__), o que ativa o name mangling (modificação do nome) para evitar colisões de nomes em subclasses.

Aqui está um exemplo simples de encapsulamento em Python:
"""
class MinhaClasse:
    def __init__(self):
        self._atributo_protegido = "valor protegido"
        self.__atributo_privado = "valor privado"

    def metodo_publico(self):
        return "Este é um método público"

    def _metodo_protegido(self):
        return "Este é um método protegido"

    def __metodo_privado(self):
        return "Este é um método privado"

    def acessar_privado(self):
        return self.__metodo_privado()

obj = MinhaClasse()
print(obj.metodo_publico())  # Acessível
print(obj._atributo_protegido)  # Acessível, mas não recomendado
print(obj._metodo_protegido())  # Acessível, mas não recomendado

# print(obj.__atributo_privado)  # Não acessível diretamente
# print(obj.__metodo_privado())  # Não acessível diretamente
print(obj.acessar_privado())  # Acessível através de um método público

"""
Neste exemplo, (__atributo_privado) e (__metodo_privado) não podem ser acessados diretamente fora da classe MinhaClasse, 
mas podem ser acessados através do método público (acessar_privado).
"""