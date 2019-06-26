# coding: windows-1252

# Dicionários - 'dicts'
dicionario = {'nome': 'Bruno', 
              'idade':30,
              'enderecos':[{
                  'cidade': 'Angatuba'
              },{
                  'cidade': 'Sorocaba'
              }]
             }

print(dict)

# Acessar um elemento do dict
print(dicionario.get('nome'))
print(dicionario.get('enderecos')[0].get('cidade'))
print(dicionario.get('enderecos')[1].get('cidade'))

# Adicionando novo elemento ao dict
dicionario.update({'ano_nascimento': 1988})
print(dicionario)

# Adicionar um valor default caso não exista a chave no dict
print('Nacionalidade é: {}'.format(dicionario.setdefault('nacionalidade', 'Brasileiro')))

# Retornar um elemento do dict pela chave e remove-lo em seguida - pop()
print('Antes do pop() - {}'.format(dicionario))
print('Ano de nascimento é {}'.format(dicionario.pop('ano_nascimento')))
print('Depois do pop() - {}'.format(dicionario))

# Removendo todos itens do dict
dicionario.clear

dicionario = {'nome': 'Bruno', 
              'idade':30,
              'enderecos':[{
                  'cidade': 'Angatuba'
              },{
                  'cidade': 'Sorocaba'
              }]
             }

# Iterando sobre dicionários - chave
print('Iterando sobre chaves:')
for key in dicionario.keys():
    print(key)

# Iterando sobre dicionários - valor
print('Iterando sobre valores:')
for values in dicionario.values():
    print(values)

# Iterando sobre dicionários - chave, valor
print('Iterando sobre itens:')
for key, value in dicionario.items():
    if isinstance(value, list):
        for i in value:
            for k, v in i.items():
                print('{} - {}'.format(k, v))
    else:
        print('{} - {}'.format(key, value))

"""
Iterar sobre duas listas como se fosse um dicionário - zip()
"""
lista_chave = ['nome', 'idade', 'cidade', 'estado']
lista_valor = ['Bruno', 30, 'Sorocaba', 'SP']

print('Iterando com zip:')
for key, value in zip(lista_chave, lista_valor):
    print('{} - {}'.format(key, value))
