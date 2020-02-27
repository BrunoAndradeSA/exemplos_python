# coding: windows-1252

# Ao utilizar o comando print() em uma classe, obtemos a representa��o textual da mesma

class Classe1:
    def __init__(self, nome):
        self.nome = nome


# Ambas as representa��es exibem o m�todo __main__ devido a terem sido invocadas atrav�s do terminal
print('Representa��o textual da classe 1: {}'.format(Classe1))

classe_1 = Classe1('MinhaClasse1')

print('Representa��o textual do objeto 1: {}'.format(classe_1))

# Representa��o textual de classes atrav�s do m�todo __str__()
class Classe2:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Classe nomeada como {}".format(self.nome)

print('Representa��o textual da classe 2: {}'.format(Classe2))

classe_2 = Classe2('Classe 2')

# A representa��o textual da inst�ncia passa a exibir o retorno da fun��o __str__
print('Representa��o textual do objeto 2: {}'.format(classe_2))

# De modo semelhante ao m�todo __str__ podemos utilizar o m�todo __repr__
class Classe3:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "Classe nomeada como {}".format(self.nome)

print('Representa��o textual da classe 3: {}'.format(Classe3))

classe_3 = Classe3('Classe 3')

print('Representa��o textual do objeto 3: {}'.format(classe_3))

# A diferen�a entre __str__ e __repr__ � que o segundo carrega uma representa��o formal da classe,
# que ser� exibida ao invocarmos a classe no terminal por exemplo, enquanto o primeiro � utilizado
# para representa��o da classe quando esta � explicitamente convertida em um str