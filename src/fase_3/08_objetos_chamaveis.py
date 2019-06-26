# coding: windows-1252

# Objetos que implementam o método __call__(), podem ser invocados pela sintaxe de chamada, ou seja,
# usando parênteses. Exemplos são funções e métodos


class Soma:
    def __init__(self):
        pass

    def __call__(self, *args):
        soma = 0

        for n in args:
            print('Número: {}'.format(soma))
            soma = soma + n
        
        return soma

soma = Soma()

print('Soma é: {}'.format(soma(1, 3, 5, 7, 9)))
