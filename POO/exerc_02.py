# Exercício:

# 1 - Crie uma classe Carro (Nome);
# 2 - Crie uma classe Motor (Nome);
# 3 - Crie uma classe Fabricante (Nome);
# 4 - Faça a ligação entre Carro tem um Motor.
# Obs.: Um motor pode ser de vários carros.
# 5 - Faça a ligação entre Carro e um Fabricante.
# Obs.: Um fabricante pode fabricar vários carros;
# Exiba o nome do carro, motor e fabricante na tela.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

dodge_c = Carro('Dodge Challenger')
fabricante_c = Fabricante('Brampton Assembly Plant')
v8 = Motor('v8')
dodge_c.fabricante = fabricante_c
dodge_c.motor = v8
print(dodge_c.nome, dodge_c.fabricante.nome, dodge_c.motor.nome)

dodge_m = Carro('Dodge Muscle')
dodge_m.fabricante = fabricante_c
dodge_m.motor = v8
print(dodge_m.nome, dodge_m.fabricante.nome, dodge_m.motor.nome)