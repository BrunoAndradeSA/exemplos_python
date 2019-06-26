# coding: windows-1252

# A diretiva 'nonlocal' é utilizada quando queremos alterar, dentro de uma função interna, o valor do parâmetro recebido 
# pela função externa. A Principio podemos apenas LER este valor dentro da função interna, com a diretiva 'nonlocal'
# torna-se possível alterar o valor de uma variável/parâmetro definido no escopo da função externa
def get_contador(count):
    def contador():
        nonlocal count        
        count = count + 1

        return count
    
    return contador

contar = get_contador(0)

print(contar())
print(contar())
print(contar())
print(contar())