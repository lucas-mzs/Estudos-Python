# Exercício:

# Faça um programa que peça ao usuário para digitar um número interiro, informe se este número é par ou impar. 
# Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

try:
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

except ValueError:
    print('Digite algum número.')