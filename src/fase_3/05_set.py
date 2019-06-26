# coding: windows-1252

# Método set() é utilizado para conjuntos que não permitem elementos duplicadas, não assegura ordem e nem índice entre os elementos

# Intersecção de conjuntos
print(set([1, 2, 3, 4, 5]) & set([2, 4]))

# União de conjuntos
print(set([1, 2, 3, 4, 5]) | set([6, 7]))

# X não contém Y
print(set([1, 2, 3, 4, 5]).isdisjoint(set([6, 7])))
print(set([1, 2, 3, 4, 5]).isdisjoint(set([4, 7])))

# Diferença
print(set([1, 2, 3, 4]) - set([1, 3, 4]))

# Todos elementos de Y estão em X
print(set([1, 2, 3, 6, 7, 4]) >= set([1, 2, 3]))
