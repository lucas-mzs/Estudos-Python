# Exercício:

# Faça uma lista de compras com listas.
# O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
# Não permita que o programa quebre com erros de índices inexistentes na lista.

import os
import platform

def limpar_tela():
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(comando)

lista = []

def mostrar_menu():
    print('\n Selecione uma opção:')
    print('[i] Inserir')
    print('[a] Apagar')
    print('[l] Listar')
    print('[s] Sair')

while True:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == 'i':
        limpar_tela()
        valor = input('Digite o valor para inserir: ').strip()
        if valor:
            lista.append(valor)
            print(f'Valor "{valor}" adicionado com sucesso!')
        else:
            print('Valor vazio não foi adicionado.')

    elif opcao == 'a':
        if not lista:
            print('Lista vazia. Nada para apagar.')
            continue

        try:
            indice_str = input('Digite o índice para apagar: ')
            indice = int(indice_str)
            removido = lista.pop(indice)
            print(f'Item "{removido}" removido com sucesso.')
        except:
            print('Índice inválido. Tente novamente.')
    
    elif opcao == 'l':
        limpar_tela()
        if not lista:
            print('Lista vazia. Nada para listar.')
        else:
            print('Itens na lista:')
            for i, valor in enumerate(lista):
                print(f'{i}: {valor}')

    elif opcao == 's':
        print('Encerrando o programa.')
        break

    else:
        print('Opção inválida. Tente novamente.')




















while True:
    print('Selecione uma opção.')
    opcao = input('[i]nserir [a]paghar [l]istar : ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar esse índice')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar.')
        
        for i, valor in enumerate(lista):
            print(i, valor)