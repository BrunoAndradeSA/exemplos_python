# coding: windows-1252

# de maneira semelhante a list comprehensions, a dict comprehensions fornece uma sintaxe
# simplificada para criação de dicioánios

chave = ['id', 'nome', 'idade', 'sexo']
valor = [1, 'Bruno', 30, 'M']

# tradicional
dict1 = {}

for k, v in zip(chave, valor):
    dict1.update({k:v})

print('Dict 1: {}'.format(dict1))

# Dict comprehensions
dict2 = {k:v for k, v in zip(chave, valor)}

print('Dict 2: {}'.format(dict2))