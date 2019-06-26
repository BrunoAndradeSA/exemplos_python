# coding: windows-1252

# Em Python, funções são representadas como objetos de primeira classe. sendo assim podemos usar 
# a técnica de closures, que consiste em retornar uma função que utilize internamente variáveis
# da função que a define

# O código abaixo cria uma função que recebe um valor fixo em sua 'instânciação'
# Após instânciado, retorna uma função interna que verifica se o valor passado como parâmetro
# é maior que o valor fixo
def maior_que(valor_fixo):
    
    def _maior(valor):
        if valor > valor_fixo:
            return '{} é maior que {}'.format(valor, valor_fixo)
        else:
            return '{} não é maior que {}'.format(valor, valor_fixo)
    
    return _maior

maior_que_1000 = maior_que(1000)

print(maior_que_1000(900))
print(maior_que_1000(1001))

maior_que_500 = maior_que(500)

print(maior_que_500(400))
print(maior_que_500(560))