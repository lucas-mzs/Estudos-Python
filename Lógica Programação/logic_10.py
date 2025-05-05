# Interpolação básica de strings
# s - strings
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'Lucas' 
preco = 100.9522345
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (15, 15))