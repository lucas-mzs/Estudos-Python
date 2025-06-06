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
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa}: removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa}: adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa.')
        return
    
    print(f'{tarefa}: adicionada na lista de tarefas.')
    print()
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer e refazer ou digite uma nova tarefa.')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'limpar': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas)
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()