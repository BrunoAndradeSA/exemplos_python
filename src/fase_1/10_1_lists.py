# coding: windows-1252

# Listas - 'list'
lista = [1, 'dois', [3, 4, 5]]
print(lista)

# 'Slice' de listas
print(lista[0:2])

# Listas s�o MUT�VEIS
lista[0] = 'Seis'
print(lista)

# Adicionando valores a uma lista - append()
lista.append(7)
print(lista)

# Removendo valores a uma lista - remove()
lista.remove('Seis')
print(lista)

# Removendo TODOS os itens de uma lista - clear()
lista.clear()

if lista:
    print('Lista cont�m itens!')
else:
    print('Uma express�o condicional com uma lista vazia sempre retorna FALSE')

# Ordenando os itens de uma lista' - OBS: S� � poss�vel ordenar listas do mesmo tipo
lista = [5, 3, 2, 8, 9, 10]
lista.sort()
print(lista)

# Iterando sobre listas
animais = ['Cavalo', 'Cachorro', 'Bode', 'Gato', 'Papagaio']
# Ordena��o antes da itera��o
animais.sort()

for animal in animais:
    print('Animal:{}'.format(animal))