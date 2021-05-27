#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date

dic_nome = {}

p = ''

while p != 'N':

    nome = input('Digite o nome: ').capitalize()

    while  nome == '':
        print('Nome inválido!')
        dic_nome[nome] = input('Digite o nome: ')

    dic_nome[nome] = {}

    while True:
        try:
            dic_nome[nome]['Ano de Nascimento'] = int(input('Digite o ano de nascimento: '))
        except ValueError:
            print('Ano de nascimento inválido')
            continue
        else:
            break

    while True:
        try:        
            dic_nome[nome]['CTPS'] = int(input('Digite o número da carteira de trabalho: '))
        except ValueError:
            print('Número da CTPS inválido. Tente novamente.')
            continue
        else:
            break

    if dic_nome[nome]['CTPS'] != 0:
        while True:
            try:
                dic_nome[nome]['Ano da Contratação'] = int(input('Digite o ano da contratação: '))
            except ValueError:
                print('Ano da contratação inválido')
                continue
            else:
                break
        dic_nome[nome]['Salário'] = float(input('Digite o Salário: ').replace(',','.'))
        dic_nome[nome]['Idade'] = date.today().year - dic_nome[nome]['Ano de Nascimento']
        dic_nome[nome]['Idade para aposentadoria'] = dic_nome[nome]['Ano da Contratação'] + 35 - dic_nome[nome]['Ano de Nascimento']
        
    else:
        del dic_nome[nome]['CTPS']
        
    p = input('Deseja cadastrar outro trabalhador? (S ou N): ').upper()

    while p != 'S' and p != 'N':
        print('Resposta incorreta. Digite S para SIM ou N para NÃO')
        p = input('Deseja cadastrar outro trabalhador? (S ou N): ').upper()
        
for k,v in dic_nome.items():
    print(f'{k} - {v}')