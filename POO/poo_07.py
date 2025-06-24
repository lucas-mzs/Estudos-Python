# Atributos de Classe

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Maria', 10)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.ano_nascimento())
print(p2.ano_nascimento())