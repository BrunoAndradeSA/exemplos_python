# coding: windows-1252

# Loop 'while'
numero = 0

while numero <= 10:
    print(numero)
    numero += 1

# Loop 'while' - Controle via entrada de dados do terminal
while True:
    opcao = input('Digite um n�mero ou aperte [x] para sair:')
    
    if opcao.upper() == 'X':
        break

    print('N�mero digitado:{}'.format(opcao))

# Loop 'for'
for x in range(10):
    print(x)