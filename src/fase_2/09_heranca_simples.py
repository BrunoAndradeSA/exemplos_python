# coding: windows-1252

class ClasseMae:
    def __init__(self):
        print('Construtor da classe mãe invocado')

    def metodo_classe_mae(self):
        print('Método da classe mãe invocado')

# Herança é realizada passando como parâmetro da classe filha, a classe mãe que será herdada
class ClasseFilha(ClasseMae):
    def __init__(self):
        # O Método super() representa a instância da classe que foi herdada
        super().__init__()
        print('Construtor da classe filha invocado')

# Instanciação da classe filha
classe_filha = ClasseFilha()

# Classe filha acessando métodos da classe mãe
classe_filha.metodo_classe_mae()

# Verificando a instância criada'
if isinstance(classe_filha, ClasseFilha):
    print('Classe-filha é instância de ClasseFilha')
else:
    print('Classe-filha NÃO é instância de ClasseFilha')

if isinstance(classe_filha, ClasseMae):
    print('Classe-filha é instância de ClasseMae')
else:
    print('Classe-filha NÃO é instância de ClasseMae')