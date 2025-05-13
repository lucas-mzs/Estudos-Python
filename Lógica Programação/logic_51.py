# Generator expression, Itarables e Itaratores em Python.
# Generator são funções produzem valores sob demanda.

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

import sys

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)