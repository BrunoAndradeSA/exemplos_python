# coding: windows-1252

# Enumerar listas('lists') afim de obter seu indice - enumerate()
frutas = ['Abacaxi', 'Uva', 'Manga', 'Goiaba', 'Ma�a']

print('Enumerando listas:')
for i, fruta in enumerate(frutas):
    print('{}) {}'.format(i, fruta))

# Enumerar tuplas('tuples') afim de obter seu indice - enumerate()
frutas = ('Abacaxi', 'Uva', 'Manga', 'Goiaba', 'Ma�a')

print('Enumerando tuplas:')
for i, fruta in enumerate(frutas):
    print('{}) {}'.format(i, fruta))

# Enumerar dicionarios('dicts') afim de obter seu indice - enumerate()
frutas = {'fruta': 'Ma��', 'cor': 'Vermelha', 'tamanho': 'Pequena', 'qualidade': 'Fuji'}

print('Enumerando dicion�rios:')
for i, (key, value) in enumerate(frutas.items()):
    print('{}) {} - {}'.format(i, key, value))