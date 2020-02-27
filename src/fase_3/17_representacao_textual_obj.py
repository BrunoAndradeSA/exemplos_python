# coding: windows-1252

# Ao utilizar o comando print() em uma classe, obtemos a representação textual da mesma

class Classe1:
    def __init__(self, nome):
        self.nome = nome


# Ambas as representações exibem o método __main__ devido a terem sido invocadas através do terminal
print('Representação textual da classe 1: {}'.format(Classe1))

classe_1 = Classe1('MinhaClasse1')

print('Representação textual do objeto 1: {}'.format(classe_1))

# Representação textual de classes através do método __str__()
class Classe2:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Classe nomeada como {}".format(self.nome)

print('Representação textual da classe 2: {}'.format(Classe2))

classe_2 = Classe2('Classe 2')

# A representação textual da instância passa a exibir o retorno da função __str__
print('Representação textual do objeto 2: {}'.format(classe_2))

# De modo semelhante ao método __str__ podemos utilizar o método __repr__
class Classe3:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "Classe nomeada como {}".format(self.nome)

print('Representação textual da classe 3: {}'.format(Classe3))

classe_3 = Classe3('Classe 3')

print('Representação textual do objeto 3: {}'.format(classe_3))

# A diferença entre __str__ e __repr__ é que o segundo carrega uma representação formal da classe,
# que será exibida ao invocarmos a classe no terminal por exemplo, enquanto o primeiro é utilizado
# para representação da classe quando esta é explicitamente convertida em um str