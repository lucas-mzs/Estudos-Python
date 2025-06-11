# Exercício

# Faça um programa que pergunte a hora ao usuário e, baseando-se no hórario descrito, exiba a saudação apropriada.
# Ex.: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

horas = int(input('Digite a hora: '))

try:
    if horas >= 0 and horas <= 11:
        print('Bom dia!')
    elif horas >= 12 and horas <= 17:
        print('Boa tarde!')
    elif horas >= 18 and 23:
        print('Boa noite!')
except:
    print('Por favor, digite um número inteiro.')