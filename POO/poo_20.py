# Herança Múltipla
# Quer dizer que no Python, uma classe pode estender várias outras classes.
# Herança Simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)

# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#           A
#         /   \
#        B     C
#         \   /
#           D

# Python 3 usa C3 superclass linearzation para gerar o mro.
# https://en.wikipedia.org/wiki/C3_linearzation

# Para saber a ordem de chamada dos método:
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ 
# (Dunder - Double Underscore)

class A:
    ...

    def quem_sou(self):
        print('A')

class B:
    ...

    def quem_sou(self):
        print('B')

class C:
    ...

    def quem_sou(self):
        print('C')

class D:
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
print(D.mro())