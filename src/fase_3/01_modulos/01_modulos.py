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

# Importanto um m�dulo e todo seu c�digo-fonte
print('Resultado da soma: {}'.format(meu_modulo.soma(5, 5)))

# Importando um m�dulo atrav�s de um alias
print('Resultado da divis�o: {}'.format(matematica.divisao(10, 2)))

#Importanto fun��es espec�ficas de um m�dulo
# Importando um m�dulo atrav�s de um alias
print('Resultado da multiplica��o: {}'.format(multiplicacao(10, 2)))