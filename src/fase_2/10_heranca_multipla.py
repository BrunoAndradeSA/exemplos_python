# coding: windows-1252

class A:
    def run(self):
        return 'A'

class B:
    def run(self):
        return 'B'

    def run_again(self):
        return 'B again'

# Python suporta uma forma superficial de herança multipla, aonde todas as classes herdadas
# são passadas como parâmetros para declaração da classe, a busca de métodos é sempre realizada
# nas classes da esquerda para a direta
class C(A, B):
    pass

c = C()

# Ao ser invocado o método run(), o mesmo será localizado primeiro na classe A, sendo este executado
print(c.run())

# Ao ser invocado o método run_again(), o mesmo não é localizado na classe A, sendo assim a busca é realizada
# na próxima classe a ser herdada, B, sendo este o método executado
print(c.run_again())

# A classe com herança multipla possui o atributo __mro__ que significa 'Method Resolution Order', que indica em qual
# Ordem a instância deve buscar a invocação de método e atributos herdados
print(C.__mro__)