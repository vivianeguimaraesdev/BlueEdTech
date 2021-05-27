#Exercíco 01

num1 = int(input('Digite o primeiro número inteiro: '))
print()
num2 = int(input('Digite o segundo número: '))
print()
print('Soma:', num1 + num2)
print('Divisão inteira:', num1 // num2)

if num1 > num2:
    print('Maior número:', num1)
elif num1 == num2:
    print('Os números são iguais!')
else:
    print('Maior número:', num2)

if (num1 + num2) % 2 == 0:
    print('A soma é PAR!')
else:
    print('A soma é ÍMPAR!')

if num1 * num2 > 40:
    x = format((num1 * num2) / (num1 // num2),'.2f').replace('.',',')
    print(x)
else:
    print('A multiplicação é menor que 40!')