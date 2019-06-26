# coding: windows-1252

# Fun��es geradoras permitem comportamentos que podem ser obtidos com listas e iteradores
# Por�m com a diferen�a que com listas e itera��es, toda a lista est� sendo carregada de
# uma vez em mem�ria (Ex: uma lista com um milh�o de itens) o que pode impactar em desempenho.

# Fun��es geradoras podem manter o estado de um item a ser gerado, carregando o elemento em mem�ria
# apenas quando este for chamado

def number_generator():
    for i in range(1000):
        yield i

# A palavra-chave 'yield' identifica uma fun��o geradora, cada chamada da fun��o 'gera' o pr�ximo item
# da sequencia atrav�s do m�todo next()

number = number_generator()

print('Primeira chamada: {}'.format(next(number)))
print('Segunda chamada: {}'.format(next(number)))
print('Terceira chamada: {}'.format(next(number)))

# Itera��o sobre fun��o geradora
for number in number_generator():
    print(number)