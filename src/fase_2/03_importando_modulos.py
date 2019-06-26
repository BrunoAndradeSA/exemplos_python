# coding: windows-1252

# Importação do módulo built-in da linguagem python
import math
# Importando funções específicas de dentro de um módulo
from math import sqrt
# Importando funções específicas de dentro de um módulo utilizando alias
from math import pow as potencia
# Importando módulos de iteração com sistema operacional
import platform

# Valor de PI do módulo math
print('Valor de PI: %f' % math.pi)

#Raiz quadrada de um número, utilizando a função 'sqrt()' do módulo math
print('Raiz quadrada de 9: %f' % sqrt(9))

# Potenciação de um número, utilizando a função 'pow()' do módulo math, porém com o alias 'potencia'
print('2 elevado a 2: %i' % potencia(2, 2))

# Informações do sistema
print('Seu sistema operacional é {}, versão {} na arquitetura {}'.format(platform.system(), 
                                                                         platform.release(),
                                                                         platform.architecture()
                                                                        )
)