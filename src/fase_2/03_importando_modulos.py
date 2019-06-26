# coding: windows-1252

# Importa��o do m�dulo built-in da linguagem python
import math
# Importando fun��es espec�ficas de dentro de um m�dulo
from math import sqrt
# Importando fun��es espec�ficas de dentro de um m�dulo utilizando alias
from math import pow as potencia
# Importando m�dulos de itera��o com sistema operacional
import platform

# Valor de PI do m�dulo math
print('Valor de PI: %f' % math.pi)

#Raiz quadrada de um n�mero, utilizando a fun��o 'sqrt()' do m�dulo math
print('Raiz quadrada de 9: %f' % sqrt(9))

# Potencia��o de um n�mero, utilizando a fun��o 'pow()' do m�dulo math, por�m com o alias 'potencia'
print('2 elevado a 2: %i' % potencia(2, 2))

# Informa��es do sistema
print('Seu sistema operacional � {}, vers�o {} na arquitetura {}'.format(platform.system(), 
                                                                         platform.release(),
                                                                         platform.architecture()
                                                                        )
)