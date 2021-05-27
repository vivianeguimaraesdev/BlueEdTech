#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
#Os códigos utilizados são:
#1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


candidato1 = 0
canditato2 = 0
canditato3 = 0
canditato4 = 0
nulo = 0
branco = 0
cont_votos = 0
fim_votos = 0
print("ELEIÇÕES DE 2021 - \nJosé[1]\nJoão[2]\nJeremias[3]\nJosué[4]\nNulo[5]\nBranco[6]")

while fim_votos == 0:
    seuvoto = int(input("Digite o número do seu voto: "))
    if seuvoto == 1:
        candidato1 =+1
    elif seuvoto == 2: 
        candidato2 =+1
    elif seuvoto == 3: 
        candidato3 =+1
    elif seuvoto == 4: 
        candidato4 =+1
    elif seuvoto == 5: 
        nulo =+1
    elif seuvoto == 6:
        branco =+1
    fim_votos = input("Digite 1 (Para encerrar a votação) ou 0 (Para continuar): ")
    break
    

print("José recebeu: ", candidato1)
print("João recebeu: ", candidato2)
print("Jeremias recebeu: ", candidato3)
print("Josué recebeu: ", candidato4)
print("Os votos nulos foram: ",nulo)
print("Os votos em branco foram: ", branco)



    



