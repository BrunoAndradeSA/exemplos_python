# coding: windows-1252

# Caso seja chamado pelo terminal, a vari�vel '__name__' ser� igual ao '__main__', condicionando assim
# a execu��o do c�digo
def main():
    print('Invoca��o do m�todo main! Executado do terminal')


if __name__ == '__main__':
    main()
else:
    print('M�dulo main importado! O m�todo n�o � executado a menos que seja explicitamente invocado')