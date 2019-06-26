# coding: windows-1252

# Em Python, fun��es s�o representadas como objetos de primeira classe. sendo assim podemos usar 
# a t�cnica de closures, que consiste em retornar uma fun��o que utilize internamente vari�veis
# da fun��o que a define

# O c�digo abaixo cria uma fun��o que recebe um valor fixo em sua 'inst�ncia��o'
# Ap�s inst�nciado, retorna uma fun��o interna que verifica se o valor passado como par�metro
# � maior que o valor fixo
def maior_que(valor_fixo):
    
    def _maior(valor):
        if valor > valor_fixo:
            return '{} � maior que {}'.format(valor, valor_fixo)
        else:
            return '{} n�o � maior que {}'.format(valor, valor_fixo)
    
    return _maior

maior_que_1000 = maior_que(1000)

print(maior_que_1000(900))
print(maior_que_1000(1001))

maior_que_500 = maior_que(500)

print(maior_que_500(400))
print(maior_que_500(560))