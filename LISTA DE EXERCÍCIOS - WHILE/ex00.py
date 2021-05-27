#Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. 
#Enquanto a soma não for 50, ele deve continuar repetindo.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2

while soma != 50:
    print("Valor inválido. Tente Novamente!")
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    soma = numero1 + numero2
if soma == 50:
    print("O valor desta soma é 50!")

