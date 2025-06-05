# Exercício:

# Lista de tarefas com desfazer e refazer.

import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa}: removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa}: adicionada na lista de tarefas.')
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas, tarefas_refazer):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa.')
        return
    
    print(f'{tarefa}: adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    tarefas_refazer.clear()


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer e refazer ou digite uma nova tarefa.')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        print()
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        print()
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        print()
        continue
    elif tarefa == 'limpar':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas, tarefas_refazer)
        listar(tarefas)
        print()
        continue