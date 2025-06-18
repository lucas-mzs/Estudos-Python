# Exercício:

# Sistema de perguntas e respostas.

def exibir_pergunta(pergunta, opcoes, resposta_correta):
    print(f'Pegurnta: {pergunta}\n')

    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    
    while True:
        escolha = input('\nEscolha uma opção (número): ').strip()

        if escolha.isdigit():
            indice = int(escolha)
            if 0 <= indice < len(opcoes):
                break
            else:
                print('Número fora das opções. Tente novamente.')
        else:
            print('Entrada inválida. Digite apenas o número da opção.')

    acertou = opcoes[indice] == resposta_correta

    if acertou:
        print('\n✅ Resposta correta!\n')
    else:
        print(f'\n❌ Resposta errada! A resposta certa era: "{resposta_correta}"\n')

    return acertou

def quiz():
    perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

    acertos = 0

    print('=== Quiz de matemática ===\n')

    for pergunta in perguntas:
        acertou = exibir_pergunta(
            pergunta['Pergunta'],
            pergunta['Opções'],
            pergunta['Resposta'],
        )
        if acertou:
            acertos += 1

    print('=== Resultado final ===')
    print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
    print(f'Sua pontuação: {acertos / len(perguntas) * 100:.2f}%\n')

quiz()
































































