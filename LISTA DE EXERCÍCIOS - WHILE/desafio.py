#DESAFIO - Desenvolver um programa para verificar a nota do aluno em uma prova 
# com 10 questões, o programa deve perguntar ao aluno a resposta de cada 
# questão e ao final comparar com o gabarito da prova assim calcular o total de acertos 
# e a nota (atribuir 1 ponto por resposta certa).  Após cada aluno utilizar 
# o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 

gabarito = [['01', 'A'],['02', 'B'],['03', 'C'],['04', 'D'],['05', 'E'],['06', 'E'],['07', 'D'],['08', 'C'],['09', 'B'],['10', 'A']]

aluno_resp_nota = []


p = ''
while p != 'N':

    a = input('Digite o nome do aluno: ').capitalize()
    if a == '':
        while a == '':
            print('Nome incorreto!')
            a = input('Digite o nome do aluno: ').capitalize()
    resp_aluno = []
    nota = 0

    for i,j in gabarito:
        x = input(f'Digite a reposta da questão {i}:').upper()

        while x not in 'ABCDE':
            print('Resposta incorreta. Digite A, B, C, D ou E')
            x = input(f'Digite a reposta da questão {i}:').upper()

        resp_aluno.append([i,x])

        if x == j:
            nota += 1

    aluno_resp_nota.append([a, resp_aluno, nota])
    resp_aluno = []
    p = input('Deseja digitar notas de outro aluno?: ').upper()
    while p != 'S' and p != 'N':
        print('Resposta inválida. Digite S para SIM ou N para NÃO!')
        p = input('Deseja digitar notas de outro aluno?: ').upper()


notas_alunos = [k for i,j,k in aluno_resp_nota]
alunos = [i for i,j,k in aluno_resp_nota]
max_aluno = max(notas_alunos)
max_aluno_index = notas_alunos.index(max(notas_alunos))
min_aluno = min(notas_alunos)
min_aluno_index = notas_alunos.index(min(notas_alunos))


print(f'O aluno que tirou a maior nota é {alunos[max_aluno_index]}. Sua nota é {max_aluno}!')
print(f'O aluno que tirou a menor nota é {alunos[min_aluno_index]}. Sua nota é {min_aluno}.')
print(f'Total de alunos avaliados: {len(alunos)}.')
print('Média da Turma:', sum(notas_alunos)/len(notas_alunos))