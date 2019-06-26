# coding: windows-1252

# Caso seja chamado pelo terminal, a variável '__name__' será igual ao '__main__', condicionando assim
# a execução do código
def main():
    print('Invocação do método main! Executado do terminal')


if __name__ == '__main__':
    main()
else:
    print('Módulo main importado! O método não é executado a menos que seja explicitamente invocado')