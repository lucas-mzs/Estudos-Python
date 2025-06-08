# Lista em python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo 
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
#       append - adiciona um item ao final
#       insert - adiciona um item ao índice escolhido
#       pop - remove do final ou do índice escolhido
#       del - apaga índice
#       clear - limpa a lista
#       extend - estende a lista
#       + - concatena listas
# Create, Read, Update, Delete
# criar , ler , alterar, deletar = lista[i] (CRUD)

texto = 'ABCD'
lista = list(texto)
lista[1] = 'A'
print(lista)

#          0    1   2   3
lista_n = [10, 20, 30, 40]
lista_n.append(50)
print(lista_n)


################

#         0   1   2   3
lista = [10, 20, 30, 40]

lista.append('Lucas')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])

############################

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

lista_a.extend(lista_b)

print(lista_a)


# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutáveis)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Lucas'
print(lista_b)