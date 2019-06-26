# coding: windows-1252

# Protocolos são utilizados para implementar comportamentos padronizados em classes,
# A implementação de um protocolo se dá ao implementar uma série de métodos especiais para cada tipo a ser criado

# Protocolo de Container
'''
O protocolo de container é implementado ao implementar o método __contains__, cuja função é 
responder se um elemento faz parte do container
'''
class Cidade:
    def __init__(self):
        self.cidades = ['Sorocaba', 'Angatuba', 'Itapetininga']

    def __contains__(self, item):
        return True if item in self.cidades else False

cidade = Cidade()

print('Sorocaba' in cidade)
print('Angatuba' in cidade)
print('São Paulo' in cidade)

# Protocolo Sized
'''
O protocolo sized, ou container de tamanho definido, é implementado ao implementar o método __len__, cuja função é
responder o tamanho de um determinado elemento
'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __len__(self):
        return len(self.nome)

pessoa = Pessoa('Bruno de Andrade')

print(len(pessoa))

# Protocolo iterável
'''
O protocolo iterável, faz com que determinado objeto pode ser iterado, sabendo inclusive como responder ao próximo elemento
da iteração, através dos métodos __iter__() e __next__()
'''
class Animal:
    def __init__(self, animais):
        self.animais = animais
        self.__index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            animal = self.animais[self.__index]
        except IndexError:
            self.__index = 0
            raise StopIteration

        self.__index += 1

        return animal

animais = Animal(['Cachorro', 'Cavalo', 'Gato', 'Peixe', 'Galinha'])

for a in animais:
    print(a)

# Protocolo de sequências
'''
O protocolo de sequências, deve implementar os métodos dos três protocolos anteriores, ou seja,
deve ser um container, de tamanho definido, iterável e que seja capaz de retornar um elemento,
com a diferença que deve ser capaz de retornar um elemento através de um índice, através do método
__getitem__
'''
class Animal2:
    def __init__(self, animais):
        self.animais = animais
        self.__index = 0

    def __len__(self):
        return len(self.animais)
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            animal = self.animais[self.__index]
        except IndexError:
            self.__index = 0
            raise StopIteration

        self.__index += 1

        return animal
    
    # Apenas inteiros ou slice são permitidos
    def __getitem__(self, i):
        if isinstance(i, int) or isinstance(i, slice):
            return self.animais[i]

        raise TypeError("Indice ou Slice inválido!: '{}'".format(str(i)))

animais = Animal2(['Cachorro', 'Cavalo', 'Gato', 'Peixe', 'Galinha'])

print(animais[1])
print(animais[1:4])