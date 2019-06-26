# coding: windows-1252

# Defini��o de classes no python
class MinhaClasse:
    # M�todo construtor de classe, o par�metro 'self', recebe por inje��o de dep�ndencias, uma inst�ncia da pr�pria classe
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        # Atributo protegido
        self._param2 = param2
        # Atributo privado
        self.__param3 = param3

    # Quando n�o � necess�ria a manipula��o da inst�ncia, o m�todo pode ser est�tico
    @staticmethod
    def metodo_public():
        print('Chamada de m�todo p�blico')
        
    def _metodo_protected(self):
        # Ao iniciar m�todo com um underline (_), o mesmo torna-se protegido, lan�ando erro se invocado fora do m�dulo
        print('Chamada de m�todo protegido, com par�metro protegido {}'.format(self._param2))
    
    def __metodo_private(self):
        # Ao iniciar m�todo com dois underline (__), o mesmo torna-se privado, lan�ando erro ao ser invocado por uma inst�ncia da classe
        print('Chamada de m�todo privado, com par�metro privado {}'.format(self.__param3))

    def acesso_metodo_privado(self):
        print('Acesso de m�todo privado de dentro da inst�ncia')
        self.__metodo_private()
    

# Inst�nciando a classe, caso n�o seja informado os par�metros definidos no construtor, ir� ocorrer erro
minha_classe = MinhaClasse('teste1', 'teste2', 'teste3')

# Verificando o tipo do objeto criado
print(type(minha_classe))

print('Par�metro 1: {}'.format(minha_classe.param1))

minha_classe.metodo_public()
minha_classe._metodo_protected()
# minha_classe.__metodo_private()
minha_classe.acesso_metodo_privado()

# Par�metros podem ser injetados em inst�ncias da classe - OBS: Ficam dispon�veis APENAS para a inst�ncia em que foram injetados
minha_classe2 = MinhaClasse('teste1', 'teste2', 'teste3')

minha_classe.param4 = 'Teste4'

print('Par�metro 4 - Inst�ncia 1: {}'.format(minha_classe.param4))
# print('Par�metro 4 - Inst�ncia 2: {}'.format(minha_classe2.param4))

# Fun��es podem ser passadas como par�metros, pois s�o consideras objetos de primeiro n�vel (first-level objects)
def soma(num1, num2):
    soma = num1 + num2

    print('Soma � {}'.format(soma))

minha_classe.param_soma = soma

print('Soma: {}'.format(minha_classe.param_soma))
minha_classe.param_soma(3, 5)