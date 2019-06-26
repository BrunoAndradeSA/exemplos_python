# coding: windows-1252
from collections import namedtuple


# Tuplas são estruturas que possuem acesso apenas pelo seu índice
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla[2])

# Tuplas nomeadas são parecidas com instâncias de classes, porém são objetos mais leves em comparação a instâncias de classes
# utilizadas para evitar criação de classes apenas representativas de um modelo, o que fere o principio da orientação a objetos
Usuario = namedtuple(
    'Usuario',
    [
        'IdUsuario',
        'Nome',
        'Idade'
    ]
)

usuario = Usuario(1, 'Bruno de Andrade', 30)

print('ID: {}'.format(usuario.IdUsuario))
print('Nome: {}'.format(usuario.Nome))
print('Idade: {}'.format(usuario.Idade))