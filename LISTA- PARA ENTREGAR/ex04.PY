#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mesPorExtenso de AAAA. 
# Valide a data e retorne NULL caso a data seja inválida.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def data(dd, mm, aaaa):
    if mm == 2:
        if aaaa % 4 != 0 and dd > 28:
            print('Data inválida')
        elif aaaa % 4 == 0 and dd > 29:
            print('Data inválida')
        else:
            return print(f'{dd} de {meses[mm-1]} de {aaaa}')

    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if dd > 30:
            print('Data inválida')
        else:
            return print(f'{dd} de {meses[mm-1]} de {aaaa}')

    else:
        if dd > 31 or mm > 12:
            print('Data inválida')
        else:
            return print(f'{dd} de {meses[mm-1]} de {aaaa}')

while True:
    try:
        d = input('Digite a Data: ')        
        x = int(d[0:2])
        y = int(d[3:5])
        z = int(d[-4:])
    except ValueError:
        print('Data Incorreta. Digite no formato dd/mm/aaaa')
    else:
        break

data(x,y,z)