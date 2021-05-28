class aluno():
    def __init__(self, nome_do_aluno, idade,serie, nota1, nota2, matricula, sala): # O  nome do argumento não precisa ser  o mesmo do atributo
        self.nome = nome_do_aluno
        self.escola = "Escola da Mayara"
        self.idade = idade
        self.serie = serie
        self.nota1 = nota1
        self.nota2 = nota2
        self.matricula = matricula
        self.sala = sala
        self.media = 0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) /2
        print(f"A média do {self.nome} é {self.media}")
    def altera_sala(self):
        nova_sala = input("Digite a nova sala: ")
        confirmacao = input(f"Você quer alterar o aluno {self.nome} da sala {self.sala} para a sala {nova_sala} Digite S?")
        if confirmacao == "S":
            self.sala = nova_sala
        else:
            print("Ok, nada alterado!")
        print(f"A sala do(a) aluno(a) {self.nome} é: {self.sala}")

aluno_ycaro = aluno("Ycaro", 18,"3AM",10,2,"087594","Sala 15")
aluna_nivia = aluno("Nívia",18,"3AM",9,5,"078524954","Sala 15")
#print(vars(aluno_ycaro))
print(aluno_ycaro.nome)
print(vars(aluno_ycaro))
print(vars(aluna_nivia))
print()
aluno_ycaro.calcula_media()
aluna_nivia.calcula_media()
aluno_ycaro.altera_sala()
print(vars(aluno_ycaro))
print(vars(aluna_nivia))

#o atributo é o nome e nome_do_aluno é o parâmetro
