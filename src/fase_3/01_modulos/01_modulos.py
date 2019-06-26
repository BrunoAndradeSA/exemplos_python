# coding: windows-1252
import meu_modulo
import meu_modulo as matematica
from meu_modulo import multiplicacao
from meu_modulo import soma, multiplicacao
from meu_modulo import (
    soma,
    multiplicacao,
    divisao
)
from meu_modulo import *

# Importanto um módulo e todo seu código-fonte
print('Resultado da soma: {}'.format(meu_modulo.soma(5, 5)))

# Importando um módulo através de um alias
print('Resultado da divisão: {}'.format(matematica.divisao(10, 2)))

#Importanto funções específicas de um módulo
# Importando um módulo através de um alias
print('Resultado da multiplicação: {}'.format(multiplicacao(10, 2)))