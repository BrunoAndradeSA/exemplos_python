# coding: windows-1252

# A diretiva 'nonlocal' � utilizada quando queremos alterar, dentro de uma fun��o interna, o valor do par�metro recebido 
# pela fun��o externa. A Principio podemos apenas LER este valor dentro da fun��o interna, com a diretiva 'nonlocal'
# torna-se poss�vel alterar o valor de uma vari�vel/par�metro definido no escopo da fun��o externa
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