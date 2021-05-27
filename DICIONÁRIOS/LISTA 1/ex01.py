# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
#{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81} 

print("Multiplicação dos indices de uma lista - 1, 2, 3, 4, 5, 6, 7, 8, 9")

#Programa Principal

fator = {i:i **2 for i in range(1,11)}
print("O resultado é: ", fator)
 