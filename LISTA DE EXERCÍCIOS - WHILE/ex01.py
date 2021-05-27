#Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.

senha = "cachorro"
login = input("Digite a senha: ")

while login != senha:
    print("SENHA INVÁLIDA! Tente Novamente!")
    login = input("Digite a senha: ")    
if login == senha:
    print("SENHA CORRETA! ENTRANDO NO SISTEMA...")