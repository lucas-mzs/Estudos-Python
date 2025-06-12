# Exercício:

# Qual letra apareceu mais vezes na frase?

from collections import Counter

frase = 'O Python é uma linguagem de programação multiparadigma. O Python foi criado por Guido Van Rossum.'

frase_sem_espacos = frase.replace(' ', '')

contador = Counter(frase_sem_espacos)

letra_mais_comun, qtd = contador.most_common(1)[0]

print(f'A letra que apareceu mais vezes foi "{letra_mais_comun}", que apareceu {qtd} vezes.')