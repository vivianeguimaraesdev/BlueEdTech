#CONTADOR DE VOGAIS

def some_vogal(frase):
    vogais = "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî"
    for letra in vogais:
        if letra in frase:
            frase = frase.replace(letra,"")
    return frase

str_frase = input("Digite uma palavra ou frase para retirarmos as vogais: ")
print("A palavra ou frase '",str_frase,"' fica '",some_vogal(str_frase),"' sem as vogais")

