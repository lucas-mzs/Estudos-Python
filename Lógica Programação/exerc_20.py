# Exercício:

# Aumente os preços dos produtos em 10%.
# Gere novos_produtos por depy copy (cópia profunda).

# Ordene os produtos por nome decrescente (do maior para o menor).
# Gere produtos_ordenados_por_nome por depy copy (cópia profunda).

# Ordene os produtos por preço crescente (do menor para o maior).
# Gere produtos_ordenados_por_preco por depy copy(cópia profunda).

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos['preco'] = float(produtos['preco'])

preco = produtos['preco']
aumento = preco * 0.10
print(aumento)