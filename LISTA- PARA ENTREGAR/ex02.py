
#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário 
# e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

def umafrase (frase):
    print()
    cont =0 #variavel contador
    for i in frase:
        if i in 'aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî':
            cont += 1
            frase = frase.replace(i,'') #pegando a vogal e substituindo por espaço
    print('Número de vogais:', cont)
    return frase

print(umafrase(input('Digite uma frase: ')))
print()