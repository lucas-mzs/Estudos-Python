# Exercício:

# Faça um jogo para o usuário adivinhar qual a palavra secreta.
# - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
# - Quaando o usuário digitar um letra, você vai conferir se a letra digitada está na palavra secreta.
#     - Se a letra digitada estiver na palavra secreta, exiba letra;
#     - Se a letra digitada não estiver na palavra secreta, exiba *.
# Faça a contagem de tentativas do seu usuário.

def jogo_adivinhacao():
    palavra_secreta = 'programar'
    letras_acertadas = set()
    numero_tentativas = 0

    print('=== Jogo da Palavra Secreta ===')
    print('Tente adivinhar a palavra!\n')

    while True:
        letra_digitada = input('Digite uma letra: ').lower().strip()
        numero_tentativas += 1

        if len(letra_digitada) != 1 or not letra_digitada.isalpha():
            print('Digite apenas uma letra válida (A-Z).')
            continue

        if letra_digitada in letras_acertadas:
            print(f'Você já tentou a letra "{letra_digitada}".')
        elif letra_digitada in palavra_secreta:
            print(f'Boa! A letra "{letra_digitada}" está na palavra.')
            letras_acertadas.add(letra_digitada)
        else:
            print(f'A letra "{letra_digitada}" não está na palavra.')

        palavra_formada = ''.join([
            letra if letra in letras_acertadas else '*'
            for letra in palavra_secreta
        ])

        print('Palavra formada:', palavra_formada)
        print('-' * 30)

        if palavra_formada == palavra_secreta:
            print('\n🎉 VOCÊ GANHOU! PARABÉNS!')
            print(f'A palavra era: {palavra_secreta}')
            print(f'Tentativas: {numero_tentativas}')
            break

jogo_adivinhacao()