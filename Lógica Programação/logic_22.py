# Iterável -> str, tange, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

# Como funciona o for

texto = 'Lucas'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# ou

for letra in texto:
    print(letra)


######################

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('for completo com sucesso')