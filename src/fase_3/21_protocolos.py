# coding: windows-1252

# Protocolos s�o utilizados para implementar comportamentos padronizados em classes,
# A implementa��o de um protocolo se d� ao implementar uma s�rie de m�todos especiais para cada tipo a ser criado

# Protocolo de Container
'''
O protocolo de container � implementado ao implementar o m�todo __contains__, cuja fun��o � 
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
print('S�o Paulo' in cidade)

# Protocolo Sized
'''
O protocolo sized, ou container de tamanho definido, � implementado ao implementar o m�todo __len__, cuja fun��o �
responder o tamanho de um determinado elemento
'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __len__(self):
        return len(self.nome)

pessoa = Pessoa('Bruno de Andrade')

print(len(pessoa))

# Protocolo iter�vel
'''
O protocolo iter�vel, faz com que determinado objeto pode ser iterado, sabendo inclusive como responder ao pr�ximo elemento
da itera��o, atrav�s dos m�todos __iter__() e __next__()
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

# Protocolo de sequ�ncias
'''
O protocolo de sequ�ncias, deve implementar os m�todos dos tr�s protocolos anteriores, ou seja,
deve ser um container, de tamanho definido, iter�vel e que seja capaz de retornar um elemento,
com a diferen�a que deve ser capaz de retornar um elemento atrav�s de um �ndice, atrav�s do m�todo
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
    
    # Apenas inteiros ou slice s�o permitidos
    def __getitem__(self, i):
        if isinstance(i, int) or isinstance(i, slice):
            return self.animais[i]

        raise TypeError("Indice ou Slice inv�lido!: '{}'".format(str(i)))

animais = Animal2(['Cachorro', 'Cavalo', 'Gato', 'Peixe', 'Galinha'])

print(animais[1])
print(animais[1:4])