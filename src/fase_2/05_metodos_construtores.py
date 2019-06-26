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
    

# Inst�nciando a classe, caso n�o seja informado os par�metros definidos no construtor, ir� ocorrer erro
minha_classe = MinhaClasse('teste1', 'teste2', 'teste3')

# Verificando o tipo do objeto criado
print(type(minha_classe))

print('Par�metro 1: {}'.format(minha_classe.param1))