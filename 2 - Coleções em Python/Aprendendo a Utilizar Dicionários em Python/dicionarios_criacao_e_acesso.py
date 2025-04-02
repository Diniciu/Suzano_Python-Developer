# Dicionários aninhados

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"},
    "giovanna@gmail.com": { "nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": { "nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": { "nome": "Melanie", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]
"""

# Acesso aos dados por chave

"""
dados = {"nome": "Vinícius", "idade": 28, "telefone": "789456123"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "Maria"
dados["idade"] = 13
dados["telefone"] = 987654321

dados # {"nome" : "Maria", "idade" : 13, "telefone" : "987654321"}
"""

# Exemplo

"""
pessoa = {"nome": "Vinícius", "idade": 23}

pessoa = dict(nome = "Vinícius", idade = 23)

pessoa = ["telefone"] = "789456123" # pessoa = {"nome": "Vinícius", "idade": 23, "telefone": "789456123"}
"""