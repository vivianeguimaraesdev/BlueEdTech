#NÚMERO E SEUS DIVISORES

n = int(input("Digite um número inteiro: "))
print("Os divisores de ", n, "são:")
contador = 0
for i in range(n,0,-1): #-1 é descrecente
    if(n % i == 0):
        print(i)
        contador += 1

if contador == 2:
    print(n, "é um número primo!")