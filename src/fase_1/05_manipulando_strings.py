# coding: windows-1252

# Aspas duplas
print("Ol� 'Mundo'!")

# Aspas simples
print('Ol� "Mundo"!')

# Multiline String com aspas simples
print('''
#############################################
Ol� mundo!

Est� � um string multiline com aspas simples!
#############################################
''')

# Multiline String com aspas duplas
print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Ol� mundo!

Est� � um string multiline com aspas duplas!
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

# Literais separadas por espa�o ser�o convertidas em uma unica string, por�m todas juntas
print('Ol�' 'Mundo!' 'Testando multiplas string na sa�da com espa�o')

# Literais separadas por v�rgula ser�o convertidas em uma unica string, por�m separadas por espa�o
print('Ol�', 'Mundo!', 'Testando multiplas string na sa�da com v�rgula')

# Acessando index points de uma String
print('Ol� Mundo!'[2])

# Slice notation
print('Ol� Mundo!'[2:7])

# Tamanho de uma string
print(len('Ol� Mundo!'))

# Opera��es l�gicas com Strings
if 'u' in 'Ol� Mundo!':
    print('"Ol� Mundo!" possui a letra "u"')
else:
    print('"Ol� Mundo!" n�o possui a letra "u"')

# Multiplica��o de Strins
print('Ol� Mundo!' * 3)

# Itera��o sobre strings
for i in 'Ol� Mundo!':
    print(i)

# Strings s�o IMUT�VEIS
# minha_string = 'Ol� mundo!'
# minha_string[2] = 'X'

# Primeira letra mai�scula - captalize()
print('ol� mundo!'.capitalize())

# Contar quantidade de um caracter na string - count()
print('ol� mundo!'.count('o'))

# Verificar se a string come�a com um determinado caracter - startswith()
print('ol� mundo!'.startswith('o'))

# Verificar se a string termina com um determinado caracter - endswith()
print('ol� mundo!'.endswith('!'))

# Separar strings por um determinado caracter - split()
print('Ol� Mundo Python!'.split(' '))

# Realizar uni�o de strings - join()
print(''.join(['Ol�', 'Mundo','Python!']))

# Substitui��o de strings - replace()
print('Ol� Mundo!'.replace('Mundo', 'Mundo Python!!!'))

# Interpola��o de Strings - int
print("%i Mundo!" % (1))

# Interpola��o de Strings - float
print("%f Mundo!" % (5.3))

# Interpola��o de Strings - str
print("%s Mundo!" % ("Ol�!"))

# Jun��o de Strings com separador comum - join()
print(','.join(['Teste 1', 'Teste 2', 'Teste 3']))

# Interpola��o de Strings - posicional - format()
print('Ol� mundo! {} {}'.format('Teste 1', 'Teste 2'))

# Interpola��o de Strings - declarativo - format()
print('Ol� mundo! {p2} {p1}'.format(p1='Teste 1', p2='Teste 2'))
