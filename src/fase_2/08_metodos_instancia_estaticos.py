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

    # Quando não é necessária a manipulação da instância, o método pode ser estático
    @staticmethod
    def metodo_public():
        print('Chamada de método público')
        
    def _metodo_protected(self):
        # Ao iniciar método com um underline (_), o mesmo torna-se protegido, lançando erro se invocado fora do módulo
        print('Chamada de método protegido, com parâmetro protegido {}'.format(self._param2))
    
    def __metodo_private(self):
        # Ao iniciar método com dois underline (__), o mesmo torna-se privado, lançando erro ao ser invocado por uma instância da classe
        print('Chamada de método privado, com parâmetro privado {}'.format(self.__param3))

    def acesso_metodo_privado(self):
        print('Acesso de método privado de dentro da instância')
        self.__metodo_private()
    

# Instânciando a classe, caso não seja informado os parâmetros definidos no construtor, irá ocorrer erro
minha_classe = MinhaClasse('teste1', 'teste2', 'teste3')

# Verificando o tipo do objeto criado
print(type(minha_classe))

print('Parâmetro 1: {}'.format(minha_classe.param1))

minha_classe.metodo_public()
minha_classe._metodo_protected()
# minha_classe.__metodo_private()
minha_classe.acesso_metodo_privado()

# Parâmetros podem ser injetados em instâncias da classe - OBS: Ficam disponíveis APENAS para a instância em que foram injetados
minha_classe2 = MinhaClasse('teste1', 'teste2', 'teste3')

minha_classe.param4 = 'Teste4'

print('Parâmetro 4 - Instância 1: {}'.format(minha_classe.param4))
# print('Parâmetro 4 - Instância 2: {}'.format(minha_classe2.param4))

# Funções podem ser passadas como parâmetros, pois são consideras objetos de primeiro nível (first-level objects)
def soma(num1, num2):
    soma = num1 + num2

    print('Soma é {}'.format(soma))

minha_classe.param_soma = soma

print('Soma: {}'.format(minha_classe.param_soma))
minha_classe.param_soma(3, 5)