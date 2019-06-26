# coding: windows-1252

# Em Python, toda comparação de instâncias de classes retornará FALSE, devido a tudo
# para a linguagem ser um objeto. Para realizar a comparação, a classe deve implementar
# um método especial chamado __eq__ que recebe em seu construtor a instância de outra classe
# para comparação de seus atributos

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

# Retornará FALSE pois os nomes são diferentes
print(classe_1 == classe_2)

classe_1 = MinhaClasse2('Classe3')
classe_2 = MinhaClasse2('Classe3')

# Retornará TRUE pois os nomes são iguais
print(classe_1 == classe_2)

# Outros métodos de comparação de instâncias de classes
# object.__lt__(self, other) => x  < y 
# object.__le__(self, other) => x <= y
# object.__ne__(self, other) => x != y
# object.__gt__(self, other) => x  > y
# object.__ge__(self, other) => x >= y