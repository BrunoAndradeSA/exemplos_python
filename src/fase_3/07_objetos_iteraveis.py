# coding: windows-1252

# Toda classe que implemente os m�todos __iter__ e __next__ podem ser tratadas com objetos iter�veis

# M�todo __iter__ indica qual o objeto ser� iter�vel, no caso, a pr�pria inst�ncia da classe
# M�todo __next__ indica o que ser� retornado a cada itera��o, no caso, ser� retornada uma linha lida do arquivo a cada itera��o
class MinhaClasse:
    def __init__(self):
        self._file = open('arquivo_leitura.txt', 'r')

    def __iter__(self):
        return self

    def __next__(self):
        linha = self._file.readline()

        if not linha:
            self._file.close()
            raise StopIteration
        
        return linha

minha_classe = MinhaClasse()

for linha in minha_classe:
    print(linha)