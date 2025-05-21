# Exercício:

# Somando Listas:
# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores for maior que a outra, a soma só vai considerar o tamanho da menor.
# Ex.:
# lista_a = [1, 2, 3, 4, 5, 6,]
# lista_b = [1, 2, 3, 4]
# Resultado;
# lista_soma = [2, 4, 6, 8]

lista_a = [1, 2, 3, 4, 5, 6,]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)