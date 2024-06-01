# DICIONARIOS EM PYTHON

Um dicionário é um conjunto não ordenado de pares **chave:valor**, onde as chaves são únicas em uma dada instância do dicionário.

```python
pessoa = {"nome" : "jhon", "idade": 35}

pessoa = dict(nome = "jhon", idade = 35)

# adicionando a dicionário

pessoa["telefone"] = "3355-2155"
```
## ACESSO AOS DADOS

```python
dados = {"nome" : "jhon", "idade": 35, "telefone": "3355-2155"}

dados["nome"] # jhon
dados["idade"] # 35
dados["telefone"] # 3355-2155

# Alterando valores de chaves

dados["nome"] = "Josy"
dados["idade"] = 12
dados["telefone"] = "9899-9899"
```
## Dicionários aninhados
Dicionários podem armazenar qualquer tipo de  objeto 
python como valor, desde que a chave para esse valor seja um 
objeto imutável como (strings e números)

```python
contatos = {
    "joaozinho@gmail.com" : {"nome" : "joao", "telefone" : "3398-4587"},
    "pedrinho@gmail.com" : {"nome" : "pedro", "telefone" : "3398-9863"},
    "sofi@gmail.com" : {"nome" : "sophia", "telefone" : "3398-0247"},
    "gabizinha@gmail.com" : {"nome" : "Gabriella", "telefone" : "3398-3620"},
}

# Acessando campos

contatos["pedrinho@gmail.com"]["telefone"] # "3398-9863"
```

## Iterar dicionários
A forma mais comum para percorrer os dados de um dicionário é utilizando o comando **for**.
```python
for chave in contatos:
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(chave, valor)
```

