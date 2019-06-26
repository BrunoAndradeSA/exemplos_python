# coding: windows-1252
import time

# Devido ao fato de funções serem tratadas com objetos pelo Python, podemos criar funções
# que recebem funções como parâmetros, e que retornar funções.

# o decorator é um mecanismo de sintaxe que chama uma função, passando outra como parâmetro
# ou chama o construtor de uma classe passando uma função como parâmetro

# em outras palavras, podemos adicionar comportamentos extras a funções existentes

# Função decoradora
def exibe_execucao(funcao):
    def execucao(*args, **kwargs):
        print('Função {} executada com os argumentos {}'.format(
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

print('Soma é {}'.format(soma(5, 7)))
print('Multiplicação é {}'.format(multiplicacao(5, 4)))

# Classe Decoradora, necessário implementar a classe __call__()
class tempo_execucao:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self, *args, **kwargs):
        inicial = time.time()
        result = self.funcao(*args, **kwargs)
        final = time.time()

        tempo_execucao = str(final - inicial)

        print('Função {} executada em {} segundos'.format(self.funcao.__name__, tempo_execucao))

        return result

@tempo_execucao
def soma2(num1, num2):
    return num1 + num2

@tempo_execucao
def multiplicacao2(num1, num2):
    return num1 * num2

print('Soma 2 é {}'.format(soma2(5, 7)))
print('Multiplicação 2 é {}'.format(multiplicacao2(5, 4)))