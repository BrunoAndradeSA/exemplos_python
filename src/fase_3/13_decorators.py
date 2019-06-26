# coding: windows-1252
import time

# Devido ao fato de fun��es serem tratadas com objetos pelo Python, podemos criar fun��es
# que recebem fun��es como par�metros, e que retornar fun��es.

# o decorator � um mecanismo de sintaxe que chama uma fun��o, passando outra como par�metro
# ou chama o construtor de uma classe passando uma fun��o como par�metro

# em outras palavras, podemos adicionar comportamentos extras a fun��es existentes

# Fun��o decoradora
def exibe_execucao(funcao):
    def execucao(*args, **kwargs):
        print('Fun��o {} executada com os argumentos {}'.format(
            funcao.__name__, args
        ))

        result = funcao(*args, **kwargs)

        return result

    return execucao

@exibe_execucao
def soma(num1, num2):
    return num1 + num2

@exibe_execucao
def multiplicacao(num1, num2):
    return num1 * num2

print('Soma � {}'.format(soma(5, 7)))
print('Multiplica��o � {}'.format(multiplicacao(5, 4)))

# Classe Decoradora, necess�rio implementar a classe __call__()
class tempo_execucao:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self, *args, **kwargs):
        inicial = time.time()
        result = self.funcao(*args, **kwargs)
        final = time.time()

        tempo_execucao = str(final - inicial)

        print('Fun��o {} executada em {} segundos'.format(self.funcao.__name__, tempo_execucao))

        return result

@tempo_execucao
def soma2(num1, num2):
    return num1 + num2

@tempo_execucao
def multiplicacao2(num1, num2):
    return num1 * num2

print('Soma 2 � {}'.format(soma2(5, 7)))
print('Multiplica��o 2 � {}'.format(multiplicacao2(5, 4)))