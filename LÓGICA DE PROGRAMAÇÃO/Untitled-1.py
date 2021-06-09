palavra = "CERVEJA"

palavra_forca = ["_" for i in palavra]

chance = 0
print("A palavra é: ", end=" ")
print(" ".join(palavra_forca))

maximo = len(palavra) + 6 #quantidade de tentativas
for i in range(maximo):
    #VERIFICAR CONDIÇÕES DE PARADA: GANHOU OU PERDEU
    if palavra_forca.count("_") == 0 or chance == 6: break
    letra = input("Digite uma levra: ")
    if letra in palavra:
        print("A palavra é: ", end=" ")
        for n in range (len(palavra)):
            if letra == palavra [n]:
                del palavra_forca[n]
                palavra_forca.insert(n,letra)
                print(" ".join(palavra_forca))
    else:
         chance += 1
         if chance != 6:
             print("Você errou pela ", str(chance),"a vez. Tente novamente!")

if palavra_forca.count("_") == 0:
    print("Parabéns! Você acertou a palvra!")
else:
    print("FORCA! VOCÊ ERROU PELA SEXTA VEZ!VOCÊ PERDEU!")