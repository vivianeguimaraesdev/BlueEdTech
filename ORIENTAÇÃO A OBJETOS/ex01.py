#1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
#b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.
#c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos.

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def printar(self):
        print(f"O nome da pessoa é {self.nome} {self.sobrenome} e ele(a) tem {self.idade} anos.")


pessoa1 = Pessoa("Vivianne","Guimarães",26)
pessoa2 = Pessoa("Victor","Luz",25)
print(vars(pessoa1))
print(vars(pessoa2))
pessoa1.printar()
pessoa2.printar()
