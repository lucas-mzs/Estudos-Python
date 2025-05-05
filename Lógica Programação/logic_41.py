# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etrc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutáveeis: dict, list

# pessoa = dict(nome='Lucas Felipe', sobrenome='Menezes')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 456},
    ],
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])


####################


# Maniuplando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])