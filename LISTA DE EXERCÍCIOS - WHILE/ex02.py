# Faça um programa que leia dez conjuntos de dois valores, 
# o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  
# Encontre o aluno mais alto e o mais baixo. 
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
numero_alunos = []
altura_alunos = []

for i in range(10):
    print("Digitação número ", i + 1," :")
    n_aluno = int(input("Digite o número do aluno: "))
    while n_aluno in numero_alunos:
        print("[Este número ja foi digitado]")
        n_aluno = int(input("Digite outro número: "))
    a_aluno = altura_alunos.append(float(input("Digite a altura do aluno: ")))
    numero_alunos.append(n_aluno)

indice_baixo = altura_alunos.index(min(altura_alunos))
indice_alto = altura_alunos.index(max(altura_alunos))

print("Aluno mais baixo \nNúmero: ", numero_alunos[indice_baixo], "\nAltura: ", min(altura_alunos))
print("Aluno mais alto \nNúmero: ", numero_alunos[indice_alto], "\nAltura: ", max(altura_alunos))

