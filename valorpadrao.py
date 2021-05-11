#AUMENTO DE SALÁRIO DE UM PROFESSOR
#ENTRADA - SALARIO; PERCENTUAL DE AUMENTO; NOVO SALARIO

def aumento_salarial(salario, percentual=10):
    novo_salario = salario * percentual/100 + salario
    return novo_salario

#Programa Principal

salario_fulano = aumento_salarial(5000)
print(salario_fulano)
#se passa um parametro a função usa se não, ele usa o padrão.

