#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados 
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_num = [[],[]]

for i in range(1,8):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        lista_num[0].append(x)
    else:
        lista_num[1].append(x)

lista_num[0].sort()
lista_num[1].sort()
print('Números pares:',', '.join(str(x) for x in lista_num[0]))
print('Números ímpares:',', '.join(str(x) for x in lista_num[1]))