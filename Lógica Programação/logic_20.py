# while / else
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('o else foi executado.')
print('Fora do while.')