# Exercício:

# Calculadora com while

while True:
    numero_1 = float(input('Digite um número: '))
    numero_2 = float(input('Digite outro número: '))
    operador = input('Digite um operador ( +-/* ): ')

    numeros_validos = None

    try:
        numero_1
        numero_2
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos.')
        continue

    operadores_permitidos = ' + - / * '

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{numero_1} + {numero_2}: ', numero_1 + numero_2)
    elif operador == '-':
        print(f'{numero_1} - {numero_2}: ', numero_1 - numero_2)
    elif operador == '/':
        print(f'{numero_1} / {numero_2}: ', numero_1 / numero_2)
    elif operador == '*':
        print(f'{numero_1} * {numero_2}: ', numero_1 * numero_2)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break