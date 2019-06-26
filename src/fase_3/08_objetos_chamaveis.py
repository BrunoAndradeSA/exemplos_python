# coding: windows-1252

# Objetos que implementam o m�todo __call__(), podem ser invocados pela sintaxe de chamada, ou seja,
# usando par�nteses. Exemplos s�o fun��es e m�todos


class Soma:
    def __init__(self):
        pass

    def __call__(self, *args):
        soma = 0

        for n in args:
            print('N�mero: {}'.format(soma))
            soma = soma + n
        
        return soma

soma = Soma()

print('Soma �: {}'.format(soma(1, 3, 5, 7, 9)))
