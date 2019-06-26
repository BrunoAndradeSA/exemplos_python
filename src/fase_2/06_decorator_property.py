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
        
    @property
    def param3(self):
        return self.__param3

# Instânciando a classe, caso não seja informado os parâmetros definidos no construtor, irá ocorrer erro
minha_classe = MinhaClasse('teste1', 'teste2', 'teste3')

# Ao utilizar o decorator @property, podemos encapsular variáveis/comportamentos em métodos e utilizá-los como se fossem parâmetros
# favorecendo assim o encapsulamento
print('Parâmetro privado 3 - {}'.format(minha_classe.param3))