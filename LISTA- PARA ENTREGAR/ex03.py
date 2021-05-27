#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, 
#só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
#onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
#a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, 
#no final mostre quantos palpites foram necessários para vencer.

from random import randint
from time import sleep


senha = 'blue2021'
entrada = input('Digite a senha: ')
print()

while entrada != senha:
    print('Senha Incorreta. Tente novamente.\n')
    entrada = input('Digite a senha: ')
    print()

print('Acesso Liberado!\n\nSeja Bem vindo ao Jogo de Advinhação!\n')
sleep(1)

print('O número que eu pesei é:', end=' ')
sleep(1)
print('X\n')
sleep(1)
print('Tente advinhar o número entre 1 e 20!!!\n')

num = randint(1,20)
cont = 1

while True:
    try:
        x = int(input('Digite um número inteiro: '))
        print()
    except ValueError:
        print()
        print('Número inválido! Tente novamente.\n')
    else:
        break

while x != num:
    print('Você ERROU o número!!!. Tente novamente.\n')
    cont += 1
    while True:
        try:
            x = int(input('Digite um número inteiro: '))
            print()
        except ValueError:
            print('Número inválido! Tente novamente.\n')
        else:
            break


if cont > 1:
    print(f'Parabéns!!! Você acertou o número em {cont} tentativas!\n')
else:
    print(f'Parabéns!!! Você acertou o número em {cont} tentativa!\n')