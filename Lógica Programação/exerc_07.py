# Exercício

# Faça um prgrama que peça o primeiro nome do usuário:
 
# Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
# Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
# Maior que 6 escreva "Seu nome é muito grande".

nome = len(input('Digite seu nome: '))

if nome <= 4:
    print('Seu nome é muito curto.')
elif nome >= 5 and nome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')