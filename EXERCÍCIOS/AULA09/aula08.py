#REPETIÇÃO FOR

from typing import ItemsView


lista = ['Ana', 'Bernardo', 'Carlos', 'Daniel', 'Eurico', 'Filipe','Gabriel']
contador = 0
for item in lista:
    if item == 10:
        contador += 1
        print(item)
    if contador > 3:
        print("existem mais do que 3 itens iguais a 10")
        break #PARE!
  

#input vazio dá entrada na execução

#PARA CADA ELEMENTO DA LISTA
#Se não usar o for, ele imprime com os colhecetes e aspas


#O programa ja sabe que o elemento é o componente da lista

#range(5) -> [0,1,2,3,4]:

#for item in range(5):
    #print(item+1)

#Números pares de 2 em 2
#for item in range(6,21,2):
    #print(item)

#range é diferente de lista
