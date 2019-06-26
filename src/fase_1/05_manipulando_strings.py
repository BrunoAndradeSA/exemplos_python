# coding: windows-1252

# Aspas duplas
print("Olá 'Mundo'!")

# Aspas simples
print('Olá "Mundo"!')

# Multiline String com aspas simples
print('''
#############################################
Olá mundo!

Está é um string multiline com aspas simples!
#############################################
''')

# Multiline String com aspas duplas
print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Olá mundo!

Está é um string multiline com aspas duplas!
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

# Literais separadas por espaço serão convertidas em uma unica string, porém todas juntas
print('Olá' 'Mundo!' 'Testando multiplas string na saída com espaço')

# Literais separadas por vírgula serão convertidas em uma unica string, porém separadas por espaço
print('Olá', 'Mundo!', 'Testando multiplas string na saída com vírgula')

# Acessando index points de uma String
print('Olá Mundo!'[2])

# Slice notation
print('Olá Mundo!'[2:7])

# Tamanho de uma string
print(len('Olá Mundo!'))

# Operações lógicas com Strings
if 'u' in 'Olá Mundo!':
    print('"Olá Mundo!" possui a letra "u"')
else:
    print('"Olá Mundo!" não possui a letra "u"')

# Multiplicação de Strins
print('Olá Mundo!' * 3)

# Iteração sobre strings
for i in 'Olá Mundo!':
    print(i)

# Strings são IMUTÁVEIS
# minha_string = 'Olá mundo!'
# minha_string[2] = 'X'

# Primeira letra maiúscula - captalize()
print('olá mundo!'.capitalize())

# Contar quantidade de um caracter na string - count()
print('olá mundo!'.count('o'))

# Verificar se a string começa com um determinado caracter - startswith()
print('olá mundo!'.startswith('o'))

# Verificar se a string termina com um determinado caracter - endswith()
print('olá mundo!'.endswith('!'))

# Separar strings por um determinado caracter - split()
print('Olá Mundo Python!'.split(' '))

# Realizar união de strings - join()
print(''.join(['Olá', 'Mundo','Python!']))

# Substituição de strings - replace()
print('Olá Mundo!'.replace('Mundo', 'Mundo Python!!!'))

# Interpolação de Strings - int
print("%i Mundo!" % (1))

# Interpolação de Strings - float
print("%f Mundo!" % (5.3))

# Interpolação de Strings - str
print("%s Mundo!" % ("Olá!"))

# Junção de Strings com separador comum - join()
print(','.join(['Teste 1', 'Teste 2', 'Teste 3']))

# Interpolação de Strings - posicional - format()
print('Olá mundo! {} {}'.format('Teste 1', 'Teste 2'))

# Interpolação de Strings - declarativo - format()
print('Olá mundo! {p2} {p1}'.format(p1='Teste 1', p2='Teste 2'))
