# dataclasses - O que são dataclasses ?
# O módulo dataclasses fornece um decorador e funções para criar métodos como:
# __init__(), __repr__(), __eq__(), (entre outros) em classes definidas pelo usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionada na versão 3.7 do Python.
# doc: https://docs.python.prg/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(p1)
    print(p1.nome_completo())
    
    print(asdict(p1))
    print(astuple(p1)[0])