def madlib():
    print("######## Jogo de Palavras com a final da Champions ######## ")
    nome_jogador = input("Nome: ")
    adjetivo1 = input("Adjetivo: ")
    adjetivo2 = input("Adjetivo: ")
    idade = input("Idade: ")
    tempo = input("Numero de 1 a 45: ")
    adjetivo3 = input("Adjetivo: ")
    numero = input("Número: ")
    time_de_futebol = input("Time de Futebol: ")
    adjetivo4 = input("Adjetivo: ")



    madlib = f"A final da Champions League estava para começar, os jogadores já estavam alinhados para entrar em campo. \
{nome_jogador} estava completamente focado, era possivel notar no seu olhar que ele estava pronto para fazer história. \
Todos conheciam ele por ser um jogador {adjetivo1} e {adjetivo2}, era uma estrela aos {idade} anos e já jogava pela seleção \
do seu país. O jogo começou e aos {tempo} saiu o primeiro gol do time adversário, {nome_jogador} não se abalou, chamou o time \
e colocou a bola no centro de campo para recomeçar o jogo. Ao final do primeiro tempo, com assistência dele, o time empatou. \
O jogo foi para o intervalo e a torcida estava {adjetivo3} e estava confiante na vitória pois tinha um supercraque em campo. \
No segundo tempo, {nome_jogador} marcou mais {numero} gol(s) e garantiu a virada para o {time_de_futebol}. A torcida ficou {adjetivo4} \
e todos foram comemorar, levantaram a taça e agradeceram a todos. "
    
    print(madlib)


madlib()