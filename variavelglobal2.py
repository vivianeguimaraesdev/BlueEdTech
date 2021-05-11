#Variável Global Dentro da Função
#Não é o ideal de se usar

def soma(x,y):
    global total
    total = x + y

total = 10
soma(3,5)
print("IMPRIMINDO PELA PRIMEIRA VEZ: ", total)

