# Entendendo self em Classes Python
# Classe - Molde (geralmente sem dados)
# Instância de class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a prápria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()
fusca.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
celta.acelerar(celta)
# print(celta.nome)