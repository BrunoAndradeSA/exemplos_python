# coding: windows-1252

# A sintaxe de list comprehensions em python possibilita a geração de listas de elementos
# através de uma sintaxe mais enxuta, a fim de evitar repetição de código

# Criação de lista de maneira tradicional
lista1 = []
for i in range(10):
    lista1.append(i)

print('Lista 1: {}'.format(lista1))

# List comprehensions
lista2 = [i for i in range(10)]

print('Lista 2: {}'.format(lista2))

# Os elementos podem retornados podem ser livremente manipulados dentro da sintaxe de list comprehensions
lista3 = [i * 2 for i in range(10)]

print('Lista 3: {}'.format(lista3))


lista4 = [i * 2 for i in range(10) if i % 2 == 0]

print('Lista 4: {}'.format(lista4))

# Possibilidade de criar listas aninhadas

# Sintaxe tradicional
nested = []

for i in range(2):
    for j in range(3):
        nested.append((i, j))

print('Lista aninhada: {}'.format(nested))

# List comprehensions
nested = [(i, j) for i in range(2) for j in range(3)]

print('Lista aninhada com list comprehensions: {}'.format(nested))