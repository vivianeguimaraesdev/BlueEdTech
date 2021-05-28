class Heroi():#o selfie é para agrupar elementos da mesma classe
    def __init__(self, nome, idade, peso):#atributos em ordem
        self.nome = nome
        self.idade = idade
        self.peso = peso
 
    def engordar(self, peso):
        self.peso += peso
    
    def salvar(self):#é para dizer que é da classe herói, só o self ele não espera nenhum argumento
        print("O capitão salvou o mundo de novo. Nossa, que coisa...")

a = Heroi('Capitão América', 30, 85) #tem que ser nessa ordem
b = Heroi('Homem de Ferro',20,352)
print(vars(a))#manda printar as variáveis do objeto 'a'
print(vars(b))
a.engordar(10) #aumenta no peso descrito em acima em 'a
b.peso = 100 #mudando o valor do peso do objeto 'b'
print(vars(a))
print(vars(b))
a.salvar
print()

b.peso = a.peso #atribuindo o peso de a para b
print(f"O novo peso do {b.nome} é {b.peso}")
#Monta em estrutura de dicionário mas sua classe é um objeto

print("\n  === CLASSE PESSOA ===\n")

class Pessoa():
    def __init__(self, nome, altura, peso): #mesma quantidade de atributo tem que ser  o mesmo preenchido
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def emagrecer(self, peso):
        self.peso -= peso

a = Pessoa('Steve Rogers',1.80, 90)
print(vars(a))
a.emagrecer(10)
print(vars(a))
