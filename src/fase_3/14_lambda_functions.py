# coding: windows-1252

# Lambda functions s�o fun��es an�nimas, que s�o empregadas geralmente quando uma fun��o
# necessita ser executada apenas uma vez

percentual = lambda x, y: round((x/y) * 100, 2)

print('Percentual de 27 em um total de 430: {}%'.format(percentual(27, 100)))
print('Percentual de 27 em um total de 430: {}%'.format(percentual(27, 430)))

