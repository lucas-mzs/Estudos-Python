# Flag (Bandeira) - Marcar um lugar
# None = Não valor
# is e is not = é e não é (tipo, valor, identidade)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')