# coding: windows-1252

class A:
    def run(self):
        return 'A'

class B:
    def run(self):
        return 'B'

    def run_again(self):
        return 'B again'

# Python suporta uma forma superficial de heran�a multipla, aonde todas as classes herdadas
# s�o passadas como par�metros para declara��o da classe, a busca de m�todos � sempre realizada
# nas classes da esquerda para a direta
class C(A, B):
    pass

c = C()

# Ao ser invocado o m�todo run(), o mesmo ser� localizado primeiro na classe A, sendo este executado
print(c.run())

# Ao ser invocado o m�todo run_again(), o mesmo n�o � localizado na classe A, sendo assim a busca � realizada
# na pr�xima classe a ser herdada, B, sendo este o m�todo executado
print(c.run_again())

# A classe com heran�a multipla possui o atributo __mro__ que significa 'Method Resolution Order', que indica em qual
# Ordem a inst�ncia deve buscar a invoca��o de m�todo e atributos herdados
print(C.__mro__)