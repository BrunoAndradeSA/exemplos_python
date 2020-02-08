# coding: windows-1252

# Realizamos a leitura de arquivos com o comando 'open', atrav�s da diretiva 'r'
# arquivo = open('meu_arquivo.txt', 'r')

# Leitura dos 4 primeiros caracteres do arquivo
'''
print(arquivo.read(4))
arquivo.close()
'''

# Ler todas as linhas do arquivo
'''
arquivo = open('meu_arquivo.txt', 'r')

for l in arquivo:
    print(l)

arquivo.close()
'''

# Abrindo arquivos com o comando 'with'
'''
with open('meu_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()

    print(conteudo)
'''

# Escrevendo em arquivos, apagando o conte�do
'''
arquivo = open('meu_arquivo.txt', 'w')

conteudo = input('Conte�do do arquivo:')
arquivo.write(conteudo)

arquivo.close()
'''

# Escrevendo em arquivos, adicionando o resultado ao final
'''
arquivo = open('meu_arquivo.txt', 'a')

conteudo = input('Conte�do do arquivo:')
arquivo.write(conteudo + '\n') # \n indica uma quebra de linha

arquivo.close()
'''

# Manipula��o do ponteiro do arquivo com a fun��o seek
'''
arquivo = open('meu_arquivo.txt', 'r')

print(arquivo.read(2))
print(arquivo.read(2))
print(arquivo.read(2))
arquivo.seek(0)
print(arquivo.read(2))
print(arquivo.read(2))
arquivo.close()
'''