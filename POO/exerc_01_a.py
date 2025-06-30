# Exercício:

# Salve sua classe em JSON:
# Salve os dados da sua classe em Json e depois crie novamente as instâncias da classe com os dados salvos.
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'exerc_01.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =idade

p1 = Pessoa('João', 33)
p2= Pessoa('Helena', 21)
p3 = Pessoa('Joana', 19)
bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()