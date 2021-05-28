#Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro.
#quantidadeCombustivel.
#A classe deve possuir no mínimo esses métodos: 
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e 
# mostra a quantidade de litros que
#foi colocada no veículo.
#abastecerPorLitro( ) – método onde é informado a quantidade em 
# litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de 
# combustível total na bomba

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def alteraValor(self, valorLitro):
        self.valorLitro = valorLitro
    
    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
    
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        temp = valor/ self.valorLitro #armazena total de litros do abastecimento
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - temp)
        return temp
    
    def abastecerPorLitro(self,qtd):
        temp = qtd * self.valorLitro #valor total a ser pago
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - qtd)
        return temp

gasolina = bombaCombustivel("Gasolina Aditivada",6.15,500)
print(vars(gasolina))
gasolina.alteraValor(6.11)
print(vars(gasolina))
gasolina.alterarCombustivel("Gasolina Supra")
print(vars(gasolina))
gasolina.alterarQuantidadeCombustivel(1000)
print(vars(gasolina))

#Abastecer 50 litros
print(gasolina.abastecerPorLitro(50))
print(vars(gasolina))

#Abastecer 50,00
valor = 50
print(gasolina.abastecerPorValor(50))
