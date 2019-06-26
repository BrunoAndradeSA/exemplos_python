# coding: windows-1252

# Todos objetos em Python possuem seus atributos guardados em estruturas de dados do tipo dict()
# Podemos acessar estas estruturas com invocando a variável interna da instância chamada __dict__

class Pessoa:
    def __init__(self, nome=None, idade=None, sexo=None, cidades=[]):
        self._nome = nome,
        self._idade = idade
        self._sexo = sexo
        self._cidades = cidades

    def adicionar_cidade(self, cidade):
        self._cidades.append(cidade)

pessoa = Pessoa('Bruno', 30, 'M')

pessoa.adicionar_cidade('Angatuba')
pessoa.adicionar_cidade('Sorocaba')

print('Dicionário de atributos da instância: {}'.format(pessoa.__dict__))

# Exibição dos atributos referentes aos métodos de uma classe
print('Dicionário de atributos dos métodos da classe: {}'.format(Pessoa.__dict__.keys()))

# Possibilidade de realizar manipulação do dicionário de atributos de uma classe
pessoa_2 = Pessoa()
setattr(pessoa_2, '_nome', 'Bruno de Andrade')

print('Atributo nome setado pelo método "setattr": {}'.format(pessoa_2._nome))

# Possibilidade de realizar manipulação arbitrária do dicionário de atributos de uma classe
setattr(pessoa_2, '_data_nascimento', '08/09/1988')
print('Atributo Data de Nascimento setado pelo método "setattr": {}'.format(pessoa_2._data_nascimento))

# Obter o valor de um atributo de uma instância a partir de uma string arbitrária
nome = getattr(pessoa_2, '_nome')

print('Nome: {}'.format(nome))

try:
    cpf = getattr(pessoa_2, '_cpf')
    print('CPF: {}'.format(cpf))
except AttributeError:
    print('Pessoa não possui atributo CPF')

# Opicionalmente o método hasattr() retorna TRUE se um objeto possui determinadl atributo, e FALSE caso não possua
print(hasattr(pessoa_2, '_nome'))
print(hasattr(pessoa_2, '_cpf'))