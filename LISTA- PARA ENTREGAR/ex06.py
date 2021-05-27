#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

   # "Telefonou para a vítima?"

   # "Esteve no local do crime?"

   # "Mora perto da vítima?"

   # "Devia para a vítima?"

   # "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 

   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",

   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 

   # Caso contrário, ele será classificado como "Inocente".

from time import sleep

lista_perguntas = ['Telefonou para a vítima?: ', 'Esteve no local do crime?: ', 'Mora perto da vítima?: ', 'Devia para a vítima?: ', 'Já trabalhou com a vítima?: ']
lista_respostas = []

print('DELEGACIA DE POLÍCIA BLUE ED TECH\n')
sleep(1)
print('Você será interrogado sobre um crime!\n')
sleep(1)

for pergunta in lista_perguntas:
    resposta = input(pergunta).upper()
    print()
    while resposta != 'S' and resposta != 'N':
        print('Resposta Incorreta. Digite S para sim ou N para não!', end=' ')
        sleep(2)
        print('SALAFRÁRIO!!!.\n')        
        resposta = input(pergunta).upper()
        print()
    lista_respostas.append(resposta)

if lista_respostas.count('S') == 5:
    print('Você é o ASSASSINO!!!\n')
elif 3 <= lista_respostas.count('S') <= 4:
    print('Você é Cúmplice do crime!\n')
elif lista_respostas.count('S') == 2:
    print('Você é Suspeito do crime!\n')
else:
    print('Você é Inocente!\n')