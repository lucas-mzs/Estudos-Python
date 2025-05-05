# Exercício:

# Faça um programa que peça ao usuário para digitar um número interiro, informe se este número é par ou impar. 
# Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_imper_texto = 'ímpar'

    if par_impar:
        par_imper_texto = 'par'
    
    print(f'O número {entrada_int} é {par_imper_texto}')
else:
    print('Você não digitou um número interiro')