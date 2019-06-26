# coding: windows-1252

# DuckTyping é uma expressão que diz "Tudo que pode faz 'Quack' é um pato", ou seja,
# aproveitando-se da tipagem dinâmica, um objeto pode se comportar como se fosse outro
# Qualquer, desde que tenha certa semelhança, por exemplo, se um código acessa um
# método do objeto para verificar seu tipo, QUALQUER objeto que possua este método poderá utilizar o código
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
        print("o Animal {} fez o barulho '{}' ao ser verificado, logo {} é um animal".format(nome, animal.barulho(), nome))
    except (AttributeError, TypeError):
        print("o Animal {} NÃO fez um barulho ao ser verificado, logo {} NÃO é um animal".format(nome, nome))

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
print(calcular('Número 1', 'Número 2', 3))

print('#########################################################################')