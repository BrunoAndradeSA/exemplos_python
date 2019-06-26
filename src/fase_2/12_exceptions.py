# coding: windows-1252

# Tentativa de leitura de arquivo inexistente (Modo 2)
try:
    file = open('inexistente.txt', 'r')

    print('Leitura feita com sucesso')
    lines = file.readlines()
except FileNotFoundError:
    print('Problema ao ler o arquivo')

# Tentativa de leitura de arquivo inexistente (Modo 2)
try:
    file = open('inexistente.txt', 'r')
except FileNotFoundError:
    print('Problema ao ler o arquivo')
else:
    print('Leitura feita com sucesso')
    lines = file.readlines()

# Bloco finally
try:
    file = open('inexistente.txt', 'r')

    print('Leitura feita com sucesso')
    lines = file.readlines()
except FileNotFoundError:
    print('Problema ao ler o arquivo')
finally:
    print('Operação de leitura de arquivo realizada')

# Levantanto exceções com raise
def validar_tipo(tipo):
    if tipo not in ('str', 'int', 'float'):
        raise Exception('Tipo de dado inválido!')

# validar_tipo('boolean')

# Definindo as próprias exceptions
class TipoInvalidoException(Exception):
    pass
    
def validar_tipo2(tipo):
    if tipo not in ('str', 'int', 'float'):
        raise TipoInvalidoException

# validar_tipo2('boolean')

# Levantando uma exceção tratada

try:
    validar_tipo2('boolean')
except Exception as e:
    print('Capturei a exception! Porém irei lançá-la mesmo assim')
    raise e