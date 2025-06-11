# Exercício:

# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#      Exiba:
#           Seu nome é {nome}
#           Seu nome é invertido é {nome invertido}
#           Seu nome contém (ou não) espaços
#           Seu nome tem {n} letras
#           A primiera letra do seu nome é {letra}
#           A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#       exiba: "Desculpe, você deixou campos vazios."

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é : {nome}.')
    print(f'Sua nome invertido é : {nome[::-1]}')

    if idade <= 18:
        print('Você é maior de idade.')
    else:
        print('Você ainda não é maior de idade.')

    if ' ' in nome:
        print('Seu nome contém espeços.')
    else:
        print('Seu nome não contém espeços.')
    
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é : {nome[0]}')
    print(f'A última letra do seu nome é : {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')