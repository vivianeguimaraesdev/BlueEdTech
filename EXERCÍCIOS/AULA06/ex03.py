#Imposto e Custo

def somaImposto(txImposto, Custo):
    return (1+ txImposto/100)* Custo

#PROGRAMA PRINCIPAL

taxa = float(input('Digite a taxa de imposto: '))
custo_1 = float(input('Digite o custo: '))
print('O valor com imposto é: ', somaImposto (taxa,custo_1))
