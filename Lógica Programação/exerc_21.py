# Exercício:

# Adiando execução de funções:

def soma(x, y):
    return x + y

def multiplaca(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

samo_com_cinco = criar_funcao(soma, 5)
multiplaca_por_dez = criar_funcao(multiplaca, 10)

print(samo_com_cinco(10))
print(multiplaca_por_dez(10))