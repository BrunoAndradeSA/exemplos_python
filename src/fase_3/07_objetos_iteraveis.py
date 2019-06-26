# coding: windows-1252

# Toda classe que implemente os métodos __iter__ e __next__ podem ser tratadas com objetos iteráveis

# Método __iter__ indica qual o objeto será iterável, no caso, a própria instância da classe
# Método __next__ indica o que será retornado a cada iteração, no caso, será retornada uma linha lida do arquivo a cada iteração
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