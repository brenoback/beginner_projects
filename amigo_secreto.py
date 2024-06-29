"""
Projeto iniciante em Python de um sorteador para um amigo secreto.
O usuário deve fornecer como input o número de amigos que deseja colocar para o amigo secreto, sendo no mínimo 4!
Após isso, o sistema irá sortear quem tira quem e devolver ao usuário.

"""

import random
lista_amigos = []


def preenche_lista():
    qtd = int(input("Olá! Quantos amigos você deseja adicionar a lista para sortear?\n"))
    while qtd < 4:
        print('Só é possível realizar o sorteio com no mínimo 4 participantes!')
        print('### - ###' * 20)
        qtd = int(input("Quantos amigos você deseja adicionar a lista para sortear? Lembre-se: no mínimo 4 :)\n"))
        
    for i in range(qtd):
        amigo = input("Nome do amigo (Lembre-se de adicionar sobrenome para diferenciar nomes iguais): ")
        if amigo not in lista_amigos:
            lista_amigos.append(amigo)
    random.shuffle(lista_amigos)
    sorteador()


def sorteador():
    for i in range (len(lista_amigos)):
        if i == len(lista_amigos) - 1:
            print(lista_amigos[i] + ' ➝  ' + lista_amigos[0])
        else:
            print(lista_amigos[i] + ' ➝  ' + lista_amigos[i + 1])
        i += 1


preenche_lista()