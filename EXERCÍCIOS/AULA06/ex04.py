def trabalho(horas,adicional):
    if h > 40:
        print('Você receberá: R$', h*a, 'a mais por hora trabalhada.')
    else:
        print("O seu salário será: ", h * 10.00)


#Programa Principal

h = int(input('Digite as horas trabalhadas: '))
a = 1.5

trabalho(h,a)
