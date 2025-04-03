# {}.del deleta um valor do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"},
    "giovanna@gmail.com": { "nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": { "nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": { "nome": "Melanie", "telefone": "3333-7766"},
}

del contatos["viniciuscoutinho.vfc@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos) # {"viniciuscoutinho.vfc@gmail.com"{"nome": "Vinícius"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}, "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"}}
"""

# {}.in

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"},
    "giovanna@gmail.com": { "nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": { "nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": { "nome": "Melanie", "telefone": "3333-7766"},
}

resultado = "viniciuscoutinho.vfc@gmail.com" in contatos # True
print(resultado)

resultado = "megui@gmail.com" in contatos # False
print(resultado)

resultado = "idade" in contatos["viniciuscoutinho.vfc@gmail.com"] # False
print(resultado) 

resultado = "telefone" in contatos["giovanna@gmail.com"] # True
print(resultado)
"""

# {}.values retorna apenas os valores do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"},
    "giovanna@gmail.com": { "nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": { "nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": { "nome": "Melanie", "telefone": "3333-7766"},
}

contatos.values() # dict_values([{"nome": "Vinícius", "telefone": "9646-1133"}, {"nome": "Giovanna", "telefone": "3443-2121"}, {"nome": "Chappie", "telefone": "3344-9871"}, {"nome": "Melanie", "telefone": "3333-7766"}])
"""

# {}.update permite atualizar o dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

contatos.update({"viniciuscoutinho.vfc@gmail.com": {"nome": "Vini"}})
print(contatos) # {"viniciuscoutinho.vfc@gmail.com": {"nome": "Vini"}}

contatos.update({"augusto@gmail.com": {"nome": "Augusto", "telefone": "9876-5432"}})
print(contatos) # {"viniciuscoutinho.vfc@gmail.com": {"nome": "Vini"}, "augusto@gmail.com": {"nome": "Augusto", "telefone": "9876-5432}}
"""

# {}.setdefault cria uma chave com um valor padrão

"""
contato = { "nome": "Vinícius", "telefone": "9646-1133"}

contato.setdefault("nome", "Augusto") # Vinícius
print(contato) # { "nome": "Vinícius", "telefone": "9646-1133"}

contato.setdefault("idade", 23) # 23
print(contato) # { "nome": "Vinícius", "telefone": "9646-1133", "idade": 23}
"""

# {}.popitem remove o último item em sequência

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

contatos.popitem() # ("viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"})

contatos.popitem() # KeyError
"""

# {}.pop remove um valor do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

resultado = contatos.pop("viniciuscoutinho.vfc@gmail.com") # "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
print(resultado)

resultado = contatos.pop("viniciuscoutinho.vfc@gmail.com", {}) # {}
print(resultado)
"""

# {}.keys retorna apenas as chaves do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

contatos.keys() # dict_keys(["viniciuscoutinho.vfc@gmail.com"])

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())
"""

# {}.items retorna uma lista de tuplas contendo chave e valor

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

contatos.items() # dict_items([("viniciuscoutinho.vfc@gmail.com", {"nome": "Vinícius", "telefone": "9646-1133"})])
"""

# {}.get

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

# contatos["chave"] # KeyError

resultado = contatos.get("chave") # None
print(resultado)

resultado = contatos.get("chave", {}) # {}
print(resultado)

resultado = contatos.get("viniciuscoutinho.vfc@gmail.com", {}) # "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
print(resultado)
"""

# {}.fromkeys cria chaves

"""
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}
"""

# {}.copy faz uma cópia do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"}
}

copia = contatos.copy()
copia["viniciuscoutinho.vfc@gmail.com"] = { "nome": "Vinícius"}

contatos["viniciuscoutinho.vfc@gmail.com"]

copia["viniciuscoutinho.vfc@gmail.com"]
"""

# {}.clear apaga todos os valores do dicionário

"""
contatos = {
    "viniciuscoutinho.vfc@gmail.com": { "nome": "Vinícius", "telefone": "9646-1133"},
    "giovanna@gmail.com": { "nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": { "nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": { "nome": "Melanie", "telefone": "3333-7766"},
}

contatos.clear()
contatos
"""