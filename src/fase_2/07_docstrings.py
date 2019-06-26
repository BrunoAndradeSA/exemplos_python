# coding: windows-1252

class MinhaClasse:
    """
    #########################################################################################################################
    Docstrings s�o a documenta��o de classes e objetos

    Tudo que � informado nesta se��o, ap�s a declara��o de classes e m�todos entre aspas triplas, se torna o atributo __doc__

    da classe ou m�todo, podendo assim sem acessado em outras partes do c�digo

    Esta � a docstring da classe MinhaClasse
    #########################################################################################################################
    """

    def __init__(self):
        """
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Esta � a docstring do m�todo construtor da classe MinhaClasse
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        """
        pass


minha_classe = MinhaClasse()

print(minha_classe.__doc__)
print(minha_classe.__init__.__doc__)