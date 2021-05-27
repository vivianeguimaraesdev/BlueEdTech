#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
def umafrase (frase):
    print()
    cont =0 #variavel contador
    for i in frase:
        if i in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî':
            cont += 1
            frase = frase.replace(i,'') #pegando a vogal e substituindo por espaço
    print('Número de vogais:', cont)
    print(frase,'\n')
    x = 'Quantidade de letras retiradas: ' +str(cont)
    return x

print(umafrase(input('Digite uma frase: ')))
print()
    
