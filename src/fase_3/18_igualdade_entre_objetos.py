# coding: windows-1252

# Em Python, toda compara��o de inst�ncias de classes retornar� FALSE, devido a tudo
# para a linguagem ser um objeto. Para realizar a compara��o, a classe deve implementar
# um m�todo especial chamado __eq__ que recebe em seu construtor a inst�ncia de outra classe
# para compara��o de seus atributos

class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome

classe_1 = MinhaClasse('Classe1')
classe_2 = MinhaClasse('Classe2')

print(classe_1 == classe_2)

class MinhaClasse2:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, other):
        return self.nome == other.nome

classe_1 = MinhaClasse2('Classe1')
classe_2 = MinhaClasse2('Classe2')

# Retornar� FALSE pois os nomes s�o diferentes
print(classe_1 == classe_2)

classe_1 = MinhaClasse2('Classe3')
classe_2 = MinhaClasse2('Classe3')

# Retornar� TRUE pois os nomes s�o iguais
print(classe_1 == classe_2)

# Outros m�todos de compara��o de inst�ncias de classes
# object.__lt__(self, other) => x  < y 
# object.__le__(self, other) => x <= y
# object.__ne__(self, other) => x != y
# object.__gt__(self, other) => x  > y
# object.__ge__(self, other) => x >= y