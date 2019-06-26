# coding: windows-1252

# DuckTyping � uma express�o que diz "Tudo que pode faz 'Quack' � um pato", ou seja,
# aproveitando-se da tipagem din�mica, um objeto pode se comportar como se fosse outro
# Qualquer, desde que tenha certa semelhan�a, por exemplo, se um c�digo acessa um
# m�todo do objeto para verificar seu tipo, QUALQUER objeto que possua este m�todo poder� utilizar o c�digo
class Pato:
    def barulho(self):
        return "Quack"

class Cachorro:
    def barulho(self):
        return "Au Au!"

class Peixe:
    pass

class Carro:
    def barulho(self):
        return 'Vrumm!'

def verificar_animal(animal, nome=None):
    try:
        animal.barulho()
        print("o Animal {} fez o barulho '{}' ao ser verificado, logo {} � um animal".format(nome, animal.barulho(), nome))
    except (AttributeError, TypeError):
        print("o Animal {} N�O fez um barulho ao ser verificado, logo {} N�O � um animal".format(nome, nome))

pato = Pato()
cachorro = Cachorro()
peixe = Peixe()
carro = Carro()

verificar_animal(pato, 'Pato')
verificar_animal(cachorro, 'Cachorro')
verificar_animal(peixe, 'Peixe')
verificar_animal(carro, 'Carro')

# Exemplo de mundo real
print('#########################################################################')
def calcular(num1, num2, num3):
    return (num1 + num2) * num3

print(calcular(1, 2, 3))
print(calcular([1, 2, 3], [4, 5, 6], 3))
print(calcular('N�mero 1', 'N�mero 2', 3))

print('#########################################################################')