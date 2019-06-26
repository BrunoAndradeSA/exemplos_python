# coding: windows-1252

# Podemos interceptar o acesso aos atributos de uma classe através do Design Pattern 'Proxy',
# que consiste em atuar como uma camada entre o cliente e o objeto que o proxy encapsula

class Proxy:
    def __init__(self, objeto):
        self.objeto = objeto

    # Ao tentarmos acessar um atributo não definido da classe, acionamos o método __getattr__
    def __getattr__(self, atributo):
        if hasattr(self.objeto, atributo):
            print('Acesso ao atributo {} da classe {}'.format(atributo, type(self.objeto).__name__))

            return getattr(self.objeto, atributo)
        else:
            print('Não existe o atributo {} na classe {}'.format(atributo, type(self.objeto).__name__))

    # Ao tentarmos setar um atributo não definido acionamos o método __setattr__
    # def __setattr__(self, atributo, valor):
    #    raise Exception('Não é permitida a atribuição de atributos a classe!')

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

# Ao tentarmos acessar um atributo que foi definido, o método __getattribute__() é acionado
class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __getattr__(self, atributo):
        print('Acesso ao atributo NÃO DEFINIDO {}'.format(atributo))

        print('Não existe o atributo {}'.format(atributo))

    def __getattribute__(self, atributo):
        print('Tentando acessar o atributo {}'.format(atributo))

        return object.__getattribute__(self, atributo)

pessoa_2 = Pessoa2('Bruno de Andrade', 30)

# O método __getattribute__() sempre é disparado, procurando pelo atributo no dicionário interno da classe
# Ao encontrar o atributo definido, o mesmo é buscado no dicionário interno da classe

# Quando o atributo não existe no dicionário interno da classe, __getattribute__() também e invocado,
# porém ao não localizar o atributo no dicionário interno da classe, o mesmo repassa a execução para __getattr__()
print('Atributo Definido: {}'.format(pessoa_2.nome))
print('Atributo Não-Definido: {}'.format(pessoa_2.cpf))