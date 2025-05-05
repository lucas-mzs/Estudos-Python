# Operadoes lógicos (and)
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# são considerados falsy (que você já viu)
# 0 0.0 '' = False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# print(True and False and True)


# Operadoes lógicos (or)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# print(True or False or 0 or 'abc')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)


# Operadoes lógicos (not)
# not - Usado para inverter expressões.
# not True = False
# not False = True

print(not True) #False
print(not False) #True



# Operadoes lógicos (in e not in)
# in - Estar entre
# not in - Não estar entre
# Strings são iteráveis
# 0 1 2 3 4 5
# l u c a s
#-5-4-3-2-1

nome = 'Lucas'
# print(nome[2])
# print(nome[-3])

# print( 'uca' in nome)
# print('uca' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')