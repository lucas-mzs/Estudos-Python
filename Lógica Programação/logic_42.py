# Métodos úteis dos dicionários em Python

# len - retorna quantidade de chaves;
# keys - iterável com as chaves;
# values - iterável com os valores;
# items - iterável com chaves e valores;
# setdefault - adiciona valor se a chave não existir;
# copy - retorna uma cópia rasa (shallow copy);
# get - obtém uma chave;
# pop - apaga um item com a chave especifica (del);
# popitem - apaga o último item adicionado;
# update - atualiza um dicionário com outro.

pessoas = {
    'nome': 'Luiz Ótavio',
    'sobrenome': 'Miranda',
}

pessoas.setdefault('idade', 18)
# print(pessoas['idade'])

# print(len(pessoas))
# print(list(pessoas.keys()))
# print(list(pessoas.values()))

# for valor in pessoas.values():
#     print(valor)

# print(list(pessoas.items()))

# for chave in pessoas.items():
#     print(chave, valor)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 9999

# print(d1)
# print(d2)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# print(p1.get('nome', 'Não existe'))

nome = p1.pop('nome')
# print(nome)

ultima_chave = p1.popitem()
# print(ultima_chave)

p1.update({
    'nome': 'Lucas',
    'idade': 30,
})

p1.update(nome='Lucas', idade=30)

tupla = (('nome', 'Lucas'), ('idade', 30))
lista = [['nome', 'Lucas'], ['idade', 30]]
p1.update(lista)

# print(p1)