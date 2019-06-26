# coding: windows-1252

# Definição de classes no python
class MinhaClasse:
    # Método construtor de classe, o parâmetro 'self', recebe por injeção de depêndencias, uma instância da própria classe
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        # Atributo protegido
        self._param2 = param2
        # Atributo privado
        self.__param3 = param3
    

# Instânciando a classe, caso não seja informado os parâmetros definidos no construtor, irá ocorrer erro
minha_classe = MinhaClasse('teste1', 'teste2', 'teste3')

# Verificando o tipo do objeto criado
print(type(minha_classe))

print('Parâmetro 1: {}'.format(minha_classe.param1))