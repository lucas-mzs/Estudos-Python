# Problema dos parâmetros mutáveis em funções Python

def adicionando_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionando_clientes('luiz')
adicionando_clientes('Joana', cliente1)
adicionando_clientes('Fernando', cliente1)
cliente1.append('Julia')

cliente2 = adicionando_clientes('Helena')
adicionando_clientes('Maria', cliente2)

cliente3 = adicionando_clientes('Marcos')
cliente3.append('Viviane')

print(cliente1)
print(cliente2)
print(cliente3)