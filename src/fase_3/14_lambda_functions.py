# coding: windows-1252

# Lambda functions são funções anônimas, que são empregadas geralmente quando uma função
# necessita ser executada apenas uma vez

percentual = lambda x, y: round((x/y) * 100, 2)

print('Percentual de 27 em um total de 430: {}%'.format(percentual(27, 100)))
print('Percentual de 27 em um total de 430: {}%'.format(percentual(27, 430)))

