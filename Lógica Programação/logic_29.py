# split e join com list e str
# split - divide uma string
# join - une uma string
# strip - corta os espaços do começo e do fim da string
# rstrip - corta os espaços da direita da string
# lstrip - corta os espaços da esquerda da string

frase = '    Olha só que     ,      coisa interessante       '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidas = '-'.join('abcdefghijklmnopqrstuvwxyz')
print(frases_unidas)