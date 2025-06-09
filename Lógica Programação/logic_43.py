# Sets - Conjuntos em Python (tipo ser)
# Conjuntos são ensinados na matemática.
# Representados graficamente pelo diagrama de Venn.
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set() # vazio
s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
# - seus valores serão sempre únicos;
# - eles não aceitam valores mutáveis;
# - eles não tem índices;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 1]
s2 = set(l1)
l2 = list(s2)

s3 = {1, 2, 3}
print(3 not in s3)
for numero in s3:
    print(numero)

# Métodos úteis:
# add, update, clear, discard
s4 = set()
s4.add('Luiz')
s4.add(1)
s4.update(('Olá Mundo', 1, 2, 3, 4))
s4.clear()
s4.discard('Olá Mundo')
print(s4)

# Operadores úteis:
# união | (union) - Une
# interseção & (intersection) - Itens presentes em ambos
# diferença - (difference) - Itens presentes no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s5 = {1, 2, 3}
s6 = {2, 3, 4}
s7 = s5 | s6
s7 = s5 & s6
s7 = s5 - s6
s7 = s5 ^ s6
print(s7)

# Exemplo de uso dos sets:
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns!')
        break

print(letras)