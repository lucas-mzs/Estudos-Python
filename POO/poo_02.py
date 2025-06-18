# Cada classe tem seu próprio self.
# self - 

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Lucas', 'Felipe')

p2 = Pessoa('Julia', 'Martins')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)