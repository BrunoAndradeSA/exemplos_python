# coding: windows-1252

class MinhaClasse:
    """
    #########################################################################################################################
    Docstrings são a documentação de classes e objetos

    Tudo que é informado nesta seção, após a declaração de classes e métodos entre aspas triplas, se torna o atributo __doc__

    da classe ou método, podendo assim sem acessado em outras partes do código

    Esta é a docstring da classe MinhaClasse
    #########################################################################################################################
    """

    def __init__(self):
        """
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Esta é a docstring do método construtor da classe MinhaClasse
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        """
        pass


minha_classe = MinhaClasse()

print(minha_classe.__doc__)
print(minha_classe.__init__.__doc__)