# Exercício:

# Lista de tarefas com desfazer e refazer.

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    
def desfazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_desfazer.append(tarefa)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer.')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        print(2)
        continue
    elif tarefa == 'refazer':
        print(3)
        continue
    else:
        tarefas.append(tarefa)
        continue