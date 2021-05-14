nomes = [] #abri uma lista vazia para ser preenchida

for i in range(1000): #recebe no maximo 1000 nomes
    a = input("Digite um nome para acrescentar a lista ou 0 para sair:").lower()
    if a == '0': #se digitar zero para
        break
    else:
        nomes.append(a.lower())
    
nome = input("Digite um nome a ser buscado na lista: ").lower()
if nome in nomes:
    print("O nome está na lista!")
else:
    print("O nome NÃO está na lista!")
