#EXERCÍCIO CRIME

perg = []
perg.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
perg.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
perg.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
perg.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
perg.append(input("Já trabalhou com a vitima? 1/Sim ou 0/Não: "))

respostas = 0
for x in perg: #Soma o número de respostas
    respostas += int(x) #x como variável temporária

if (respostas < 2):
    print("Inocente!")
elif (respostas == 2):
    print("Suspeita!")
elif (3 <= respostas <= 4):
    print("Cumplice")
elif (repostas == 5):
    print("Assassino!")


