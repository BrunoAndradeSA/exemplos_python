# coding: windows-1252
from collections import namedtuple


# Tuplas s�o estruturas que possuem acesso apenas pelo seu �ndice
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla[2])

# Tuplas nomeadas s�o parecidas com inst�ncias de classes, por�m s�o objetos mais leves em compara��o a inst�ncias de classes
# utilizadas para evitar cria��o de classes apenas representativas de um modelo, o que fere o principio da orienta��o a objetos
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