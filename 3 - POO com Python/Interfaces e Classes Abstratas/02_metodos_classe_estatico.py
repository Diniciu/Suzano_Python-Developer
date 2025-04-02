class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome 
        self.idade = idade
     
    @classmethod   
    def data_nacimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2025 - ano
        return Pessoa(nome, idade)
        
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
# pessoa = Pessoa("Vinícius", 23)
# print(pessoa.nome, pessoa.idade)

pessoaID = Pessoa.data_nacimento(2001, 6, 3, "Vinícius") 
print(pessoaID.nome, pessoaID.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(23))