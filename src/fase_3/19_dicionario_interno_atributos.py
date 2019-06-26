# coding: windows-1252

# Todos objetos em Python possuem seus atributos guardados em estruturas de dados do tipo dict()
# Podemos acessar estas estruturas com invocando a vari�vel interna da inst�ncia chamada __dict__

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

print('Dicion�rio de atributos da inst�ncia: {}'.format(pessoa.__dict__))

# Exibi��o dos atributos referentes aos m�todos de uma classe
print('Dicion�rio de atributos dos m�todos da classe: {}'.format(Pessoa.__dict__.keys()))

# Possibilidade de realizar manipula��o do dicion�rio de atributos de uma classe
pessoa_2 = Pessoa()
setattr(pessoa_2, '_nome', 'Bruno de Andrade')

print('Atributo nome setado pelo m�todo "setattr": {}'.format(pessoa_2._nome))

# Possibilidade de realizar manipula��o arbitr�ria do dicion�rio de atributos de uma classe
setattr(pessoa_2, '_data_nascimento', '08/09/1988')
print('Atributo Data de Nascimento setado pelo m�todo "setattr": {}'.format(pessoa_2._data_nascimento))

# Obter o valor de um atributo de uma inst�ncia a partir de uma string arbitr�ria
nome = getattr(pessoa_2, '_nome')

print('Nome: {}'.format(nome))

try:
    cpf = getattr(pessoa_2, '_cpf')
    print('CPF: {}'.format(cpf))
except AttributeError:
    print('Pessoa n�o possui atributo CPF')

# Opicionalmente o m�todo hasattr() retorna TRUE se um objeto possui determinadl atributo, e FALSE caso n�o possua
print(hasattr(pessoa_2, '_nome'))
print(hasattr(pessoa_2, '_cpf'))