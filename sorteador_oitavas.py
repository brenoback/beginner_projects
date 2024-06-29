"""
Código que tem como objetivo simular o sorteio da fase de Oitavas de Final da Copa Libertadores da América
Onde os 8 primeiros colocados enfrentam os 8 segundos colocados
Como entrada o usuário fornece o nome dos times primeiro colocados e segundo colocados
O programa sorteia e devolve os confrontos. 

"""

import random
import time
lista_primeiros = []
lista_segundos = []

def preenche_listas():
    count1 = 1
    count2 = 1
    while count1 <= 8:
        times = input(f'Digite o nome do time classificado em PRIMEIRO LUGAR. Time {count1}: \n')
        lista_primeiros.append(times)
        count1 += 1
    while count2 <= 8:
        times = input(f'Digite o nome do time classificado em SEGUNDO LUGAR. Time {count2}: \n')
        lista_segundos.append(times)
        count2 += 1
    sorteador()


def sorteador():
    random.shuffle(lista_primeiros)
    random.shuffle(lista_segundos)
    print('O sorteio está sendo definido...')
    time.sleep(3)
    print('Temos os confrontos! Será que pintou clássico por ai?\n')
    time.sleep(3)
    print('Confrontos das Oitavas de Final da Copa Libertadores: \n')
    for i in range (len(lista_primeiros)):
        if i == len(lista_primeiros) - 1:
            print(lista_primeiros[i] + ' ✘ ' + lista_segundos[0])
        else:
            print(lista_primeiros[i] + ' ✘ ' + lista_segundos[i + 1])
        i += 1

preenche_listas()