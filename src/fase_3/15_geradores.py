# coding: windows-1252

# Funções geradoras permitem comportamentos que podem ser obtidos com listas e iteradores
# Porém com a diferença que com listas e iterações, toda a lista está sendo carregada de
# uma vez em memória (Ex: uma lista com um milhão de itens) o que pode impactar em desempenho.

# Funções geradoras podem manter o estado de um item a ser gerado, carregando o elemento em memória
# apenas quando este for chamado

def number_generator():
    for i in range(1000):
        yield i

# A palavra-chave 'yield' identifica uma função geradora, cada chamada da função 'gera' o próximo item
# da sequencia através do método next()

number = number_generator()

print('Primeira chamada: {}'.format(next(number)))
print('Segunda chamada: {}'.format(next(number)))
print('Terceira chamada: {}'.format(next(number)))

# Iteração sobre função geradora
for number in number_generator():
    print(number)