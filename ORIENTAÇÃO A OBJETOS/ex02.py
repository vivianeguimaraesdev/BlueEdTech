#Crie uma classe chamada Conta para simular as operações de 
#uma conta corrente. Sua classe deverá ter os atributos Titular e 
#Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe 
#Conta e teste os atributos e métodos implementados

class Conta():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = 0

    def saque(self):
        self.sacar = int(input("Quanto deseja sacar? ")
        self.final = (self.saldo - self.sacar) 
        print(f"O valor do saldo após o saque é: R$ {self.sinal}")

    def deposito(self):
        self.depositar = int(input("Quanto deseja depositar? "))
        self.fim = self.depositar + self.saldo
        print(f"O seu saldo total após o depósito de: R$ {self.depositar} é de:R$ {self.fim}")

titular1 = Conta("Lucas","R$500.00")
titular2 = Conta("Gabriel","R$800.00")
titular1.Conta()


        