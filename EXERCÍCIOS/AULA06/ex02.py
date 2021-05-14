def numero(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')

n = int(input("Digite um número"))
print('Este número é: ', end='')
numero(n)