"""
Jogo do número secreto.
O sistema gera um número aleatório entre 1 e 500 e o usuário tem que acertar
A cada chute do usuário, o sistema devolve uma dica
Ao acertar o sistema avisa e diz quantas tentativas foram necessárias

"""


import random

x = 500
numero_secreto = random.randint(1, x)

chute = 0
tentativas = 0

while chute != numero_secreto:
    chute = int(input(f'Advinhe o número secreto entre 1 e {x}! Tenta a sorte! \n'))
    if chute < numero_secreto:
        print('Uhhh, muito baixo! O número secreto é maior. Continue tentando!')
        tentativas += 1
    elif chute > numero_secreto:
        print('Uhhh, muito alto! O número secreto é menor. Continue tentando!')
        tentativas += 1
    
print(f'OOOOPPAAAA! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas! Parabéns jogador, você é realmente um bom advinhador.')

