# coding: windows-1252

class ClasseMae:
    def __init__(self):
        print('Construtor da classe m�e invocado')

    def metodo_classe_mae(self):
        print('M�todo da classe m�e invocado')

# Heran�a � realizada passando como par�metro da classe filha, a classe m�e que ser� herdada
class ClasseFilha(ClasseMae):
    def __init__(self):
        # O M�todo super() representa a inst�ncia da classe que foi herdada
        super().__init__()
        print('Construtor da classe filha invocado')

# Instancia��o da classe filha
classe_filha = ClasseFilha()

# Classe filha acessando m�todos da classe m�e
classe_filha.metodo_classe_mae()

# Verificando a inst�ncia criada'
if isinstance(classe_filha, ClasseFilha):
    print('Classe-filha � inst�ncia de ClasseFilha')
else:
    print('Classe-filha N�O � inst�ncia de ClasseFilha')

if isinstance(classe_filha, ClasseMae):
    print('Classe-filha � inst�ncia de ClasseMae')
else:
    print('Classe-filha N�O � inst�ncia de ClasseMae')