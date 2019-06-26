# coding: windows-1252

# Podemos interceptar o acesso aos atributos de uma classe atrav�s do Design Pattern 'Proxy',
# que consiste em atuar como uma camada entre o cliente e o objeto que o proxy encapsula

class Proxy:
    def __init__(self, objeto):
        self.objeto = objeto

    # Ao tentarmos acessar um atributo n�o definido da classe, acionamos o m�todo __getattr__
    def __getattr__(self, atributo):
        if hasattr(self.objeto, atributo):
            print('Acesso ao atributo {} da classe {}'.format(atributo, type(self.objeto).__name__))

            return getattr(self.objeto, atributo)
        else:
            print('N�o existe o atributo {} na classe {}'.format(atributo, type(self.objeto).__name__))

    # Ao tentarmos setar um atributo n�o definido acionamos o m�todo __setattr__
    # def __setattr__(self, atributo, valor):
    #    raise Exception('N�o � permitida a atribui��o de atributos a classe!')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Veiculo:
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo

pessoa = Proxy(Pessoa('Bruno de Andrade', 30))
veiculo = Proxy(Veiculo('Carro', 'HB20'))

print(pessoa.nome)
print(pessoa.cpf)

print(veiculo.tipo)
print(veiculo.placa)

# Ao tentarmos acessar um atributo que foi definido, o m�todo __getattribute__() � acionado
class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __getattr__(self, atributo):
        print('Acesso ao atributo N�O DEFINIDO {}'.format(atributo))

        print('N�o existe o atributo {}'.format(atributo))

    def __getattribute__(self, atributo):
        print('Tentando acessar o atributo {}'.format(atributo))

        return object.__getattribute__(self, atributo)

pessoa_2 = Pessoa2('Bruno de Andrade', 30)

# O m�todo __getattribute__() sempre � disparado, procurando pelo atributo no dicion�rio interno da classe
# Ao encontrar o atributo definido, o mesmo � buscado no dicion�rio interno da classe

# Quando o atributo n�o existe no dicion�rio interno da classe, __getattribute__() tamb�m e invocado,
# por�m ao n�o localizar o atributo no dicion�rio interno da classe, o mesmo repassa a execu��o para __getattr__()
print('Atributo Definido: {}'.format(pessoa_2.nome))
print('Atributo N�o-Definido: {}'.format(pessoa_2.cpf))