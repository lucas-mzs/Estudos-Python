# Exercício:

"""
Calculo do primeiro dígito do CPF:
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um 
dos valores por uma contagem regressiva começando de 10.

Ex: 746.824.890-70 (746824890)
   10 9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27 0

Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7.
"""

import random

def gerar_cpf():
    nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))

    soma_d1 = sum(int(dig) * peso for dig, peso in zip(nove_digitos, range(10, 1, -1)))
    digito_1 = (soma_d1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    soma_d2 = sum(int(dig) * peso for dig, peso in zip(dez_digitos, range(11, 1, -1)))
    digito_2 = (soma_d2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf

print(gerar_cpf())