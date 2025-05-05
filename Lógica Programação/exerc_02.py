# EXERCICIO:

nome = 'Lucas Felipe'
altura = 1.75
peso = 82
imc = peso / (altura * altura)

# Lucas Felipe tem 1.75 de altura,
# pesa 82 quilos e seu IMC é 
# 26.775510204081634

# print(nome, 'tem', altura, 'de altura',)
# print('pesa', peso, 'quilos e seu IMC é',)
# print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc}'

print(linha_1)
print(linha_2)
print(linha_3)