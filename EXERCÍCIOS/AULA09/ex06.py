#MEDIA DOS ALUNOS

n = int(input("Entre com o número de matérias: "))

notas = []
for i in range(n):
    nota = float(input("Digite a nota da matéria: "))
    notas.append(nota)

media = sum(notas)/n 
print("A média final é: ", str(media))

