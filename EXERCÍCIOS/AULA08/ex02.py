#FORCA

import random
palavras = input("Digite as palavras: ")
palavras = palavras.split(" ")
#pega um número aleatoriamente entre 0 e número de palavras

letra = palavras[random.randrange(0, len (palavras))]
forca = ["_" for i in letra]

jogada = 1
while (jogada < 7 and forca.count("_")  != 0):
    letra2 = input("Digite uma letra: ")
    if (letra2 in letra): #verifica se a palavra tem a letra correspondente
        print("A palavra é: ", end= " ")
        for p in range(len(letra)):
            if letra2 == letra[p]:
                del forca[p]
                forca.insert(p,letra2)
        print(" ".join(forca))
    else:
        print("-> Você errou pela" + (jogada)+ "a vez. Tente Novamente!")
        jogada = jogada + 1
if forca.count("_") == 0:
    print("Parabéns! Você acertou!")
else:
    print("Forca! GAME OVER!")