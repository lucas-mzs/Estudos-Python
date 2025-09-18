# Maria pegou um emprés de R$1.000.000,00 para realizar o pagamento em 5 anos.
# A data em que ela pegou o emprestimo foi 20/12/2020 e o vencimento de cada parcela é no dia 20 de cada mês.
# - Crie a data do empréstimo;
# - Crie a data finmal do empréstimo;
# - Mostre todas as datas de vencimento e o valor de cada parcela;

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
data_inicio = datetime(2020, 12, 20)
prazo_anos = 5
qtd_parcelas = prazo_anos * 12
valor_parcela = valor_emprestimo / qtd_parcelas

data_final = data_inicio + relativedelta(years=prazo_anos)

print(f'Data do empréstimo: {data_inicio.strftime('%d/%m/%Y')}')
print(f'Data final do empréstimo: {data_final.strftime('%d/%m/%Y')}')
print(f'Quantidade de parcelas: {qtd_parcelas}')
print(f'Valor de cada parcela: {valor_parcela:,.2f}\n')

print('Datas de vencimento das parcelas:')
datas_vencimento = []
for i in range(1, qtd_parcelas + 1):
    vencimento = data_inicio + relativedelta(months=i)
    datas_vencimento.append(vencimento)
    print(f'Parcela {i}: {vencimento.strftime('%d/%m/%Y')} - R${valor_parcela:,.2f}')

hoje = datetime.now()
parcelas_pagas = sum(1 for d in datas_vencimento if d < hoje)
parcelas_restantes = qtd_parcelas - parcelas_pagas
valor_restante = parcelas_restantes * valor_parcela

print('\nSituação atual:')
print(f'Hoje: {hoje.strftime('%d/%m/%Y')}')
print(f'Parcelas pagas: {parcelas_pagas}')
print(f'Parcelas restantes: {parcelas_restantes}')
print(f'Valor restante a pagar: R${valor_restante:,.2f}')