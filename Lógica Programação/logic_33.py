# Introdução as funções (def) em Python
# Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
# Por padrão, funções Python retornam None (nada).

# def Print():
#     print('Váriaveis 1')
#     print('Váriaveis 2')
#     print('Váriaveis 3')
#     print('Váriaveis 4')

# Print()


# def imprimir(a, b, c):
#     print(a, b , c)

# imprimir(1, 2, 3)


# def saudacao(nome = 'Sem nome'):
#     print(f'Olá {nome}!')

# saudacao('Maria Julia')


def multiplo_de(numero, multipo):
    resultado = numero % multipo == 0
    print(f'{numero} é múltiplo de {multipo}', end ='')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)