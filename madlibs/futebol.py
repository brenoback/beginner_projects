def madlib():
    print("######## Jogo de Palavras com Futebol ######## ")
    nome_time = input("Nome do time de futebol: ")
    adjetivo = input("Adjetivo: ")
    nome_pessoa = input("Nome da pessoa: ")
    verbo1 = input("Verbo (passado): ")
    substantivo = input("Substantivo no plural: ")
    numero = input("Numero: ")
    adjetivo2 = input("Adjetivo: ")
    verbo2 = input("Verbo (Infinitivo): ")
    verbo3 = input("Verbo (Passado): ")


    madlib = f"A grande final entre {nome_time} e seus rivais foi extremamente {adjetivo}. O capitão do time, {nome_pessoa}, \
{verbo1} o primeiro gol e animou os {substantivo} na arquibancada. Com o placar em {numero} a 0, \
a equipe estava determinada a manter sua vantagem. Foi uma partida {adjetivo2} e todos os jogadores se esforçaram ao máximo para {verbo2} a vitória. No último minuto, \
o goleiro fez uma defesa incrível e garantiu a vitória. O estádio inteiro {verbo3} em celebração enquanto os campeões levantavam a taça."

    print(madlib)

madlib()