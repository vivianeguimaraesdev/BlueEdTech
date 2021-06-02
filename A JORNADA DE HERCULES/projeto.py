#Emily Alessandra
#Vivianne Sophie
#Gabriel Baldez
from string import Template
from time import sleep

class Trabalhos:
    def __init__(self, vida, graca, bencao):
        self.vida = vida
        self.graca = graca
        self.__bencao = bencao
    
    def getBencao(self):
        return self.__bencao

    def setBencao(self, bencao):
        self.__bencao == bencao

    def mensagem_inicial(self,lista):#print(modulos.mensagem_inicial([2, 'Hydra', 'mensagem']))
        frase = Template("${trabalho}° trabalho: ${monstro}.\n${mensagem}.")
        frase = frase.substitute(
        trabalho = lista[0],
        monstro = lista[1],
        mensagem = lista[2]
        )
        return frase

    def linha(self):
        print('-='*20)

    def cabeçalho(self,txt):
        self.linha()
        print(txt.center(42))
        self.linha()
        
    def menu(self,lista):
        self.cabeçalho('TAREFAS')
        c = 1
        for item in lista:
            print(f'{c} - {item}')
            c += 1
        self.linha()
        opcao = input('Escolha sua opção: ')
        return opcao

    def menu_ataque(self,lista):
        self.cabeçalho('AÇÕES')
        c = 1
        for item in lista:
            print(f'{c} - {item}')
            c += 1
        self.linha()
        arma = input('Escolha sua arma: ')
        return arma

class Hercules(Trabalhos):
    def __init__(self, vida, graca, bencao):
        self.energia = 100
        self.cura = False
        self.arma = False
        super().__init__(vida, graca, bencao)
   

    def __str__(self):
        return "Você tem: " + str(hercules.vida) +' de vida. E possui '+str(hercules.graca)+" graças."

    def descanso(self):
        self.forca = True
        self.cura = True
        self.vida += 100    

class Bolsa(Trabalhos):
    def __init__(self):
        self.ambrosia = 1
        self.pocao = 1
        

if(__name__ == "__main__"):
    trabalho = 1
    hercules = Hercules(100,0,100)
    bolsa = Bolsa()
    while hercules.vida > 0:
        hercules.linha()
        print(hercules)
        hercules.linha()
        if hercules.vida < 50:
            print('Cuidado você está fraco, sofrer outro dano pode ser fatal. Convém tomar uma ambrosia para se fortalecer.')
        if trabalho == 1:
            print(hercules.mensagem_inicial([1, 'Leão de Neméia', 'Um Leão está aterrorizando os moradores da aldeia de Neméia. Sua missão é ir até lá e derrotá-lo.']))
            opcao = hercules.menu(['Achar a ambrosia...', 'Tomar a ambrosia para ter força', 'Afiar  uma pedra para fazer a arma.', 'Tomar a poção de cura', 'Atacar o monstro'])
            if (opcao == '1'):
                bolsa.ambrosia += 1
                print('Você encontrou a ambrosia! E pode usá-la para aumentar sua força!')
            elif (opcao == '2'):
                hercules.forca = True
                print('Agora você possui força o suficiente para atacar o monstro!')
            elif (opcao == '3'):
                hercules.arma = True
                print('Agora você pode atacar o monstro')            
            elif (opcao == '4'):
                bolsa.pocao += 1
                hercules.vida + 20
                print(f'Você aumentou em 20 sua vida, agora você tem {hercules.vida} de vida!')
            elif (opcao == '5'):
                arma = ''
                while arma !="3":
                    if hercules.arma == True:
                        arma = hercules.menu_ataque(['Clava', 'Flechas', 'Usando as próprias mãos'])     
                        if (arma == '1'):
                            hercules.vida -= 20
                            print(f'Você causou dano no Leão mas não o derrotou. Tente novamente.\nVIDA: {hercules.vida}')
                        elif (arma == '2'):
                            hercules.vida -= 40
                            print(f'Suas flechas não acertaram o leão e ele lhe feriu.\nVIDA: {hercules.vida}')
                        elif (arma == '3'):
                            print('Você o estrangulou e conseguiu derrotar o leão.\nAgora você possui uma capa com a pele do mesmo que o protegerá!')
                            trabalho +=1
                            hercules.graca += hercules.getBencao()
                            hercules.linha()
                            print('')
                                    
                        else:
                            print('Você não afiou a arma, você não poderá atacar o monstro!') 
            
        if trabalho == 2:
            print(hercules.mensagem_inicial([2, 'Hydra de Lerna', 'Agora você está na cidade de Lerna e descobre que um grande monstro HYDRA de 9 cabeças está aterrorizando a cidade. Você precisará conseguir uma tocha,poção de cura e a graça dos deuses!']))
            opcao = hercules.menu(['Usar a graça dos deuses para comprar madeira e tecido.', 'Comprar madeira e tecido e fazer a tocha.', 'Tomar poção de cura', 'Atacar o monstro'])
            if opcao == '1':
                hercules.graca += 20
                print('Agora você poder comprar madeira e tecido. Você irá precisar!')
            elif opcao == '2':
                if hercules.graca >= 20:
                    hercules.arma = True
                    print('Agora você pode fazer uma tocha! Será necessário para derrotar a Hydra!')
                else:
                    print('Você não tem graças o suficiente')
            elif opcao == '3':
                hercules.vida += 20
            elif opcao == '4':
                if hercules.arma == True:
                    arma = hercules.menu_ataque(['Flechas', 'Clava', 'Tocha'])
                    if arma == '1':
                        hercules.vida -= 30
                        print('Você causou dano mas não o derrotou.')
                    elif arma == '2':
                        hercules.vida -= 40
                        print('Não foi possível derrotar o monstro com esse ataque.')
                    elif arma == '3':
                        print('Você derrotou o monstro!')
                        trabalho +=1
                        hercules.graca += hercules.getBencao()
                        hercules.linha()
                        print('')
                    else:
                        print('Você precisará da tocha para poder enfrentar a Hydra.')
            
        if trabalho == 3:
                print(hercules.mensagem_inicial([3, 'Javali de Erimanto', 'Você vai embora de Lerna, após ter matado a Hydra. Pelo caminho você encontra o monte Erimanto, no noroeste da Arcádia. E descobre que um Javali, enorme e feroz, mata quem cruzar o seu caminho. Um morador pede que você o capture vivo, sem usar armas letais!']))
                opcao = hercules.menu(['Comprar uma espada do morador', 'Guardar sua clava e tocha.', 'Comprar um chicote do morador.', 'Comprar uma corda do morador', 'Atacar o Javali.'])
                if opcao == '1':
                    print('Você tentou atacar o monstro com uma arma letal e foi morto por ele.')
                    break
                elif opcao == '2':
                    hercules.energia += 20
                    print('Com menos peso para carregar você terá mais energia para o combate.')
                elif opcao == '3':
                    hercules.energia += 10
                    print('Você comprou o chicote e com isso aumentou seu poder de ataque.')
                elif opcao == '4':
                    hercules.arma = True
                    print('Você está pronto para atacar o monstro.')
                elif opcao == '5':
                    if hercules.arma == True:
                        arma = hercules.menu_ataque(['Chicote', 'Corda', 'Usar as mãos '])
                        if arma == '1':
                            hercules.vida -= 20
                            hercules.energia -= 20
                            print('Você causou dano mas não o derrotou.')
                        elif arma == '2':
                            hercules.vida -= 20
                            print('Você conseguiu amarrar o monstro mas precisa de força para mantê=lo preso.')
                            trabalho +=1
                            hercules.graca += hercules.getBencao()
                            hercules.linha()
                            print('')
                        elif arma == '3':
                            print('Você causou leve dano no monstro!')
            
        if trabalho == 4:
             print(hercules.mensagem_inicial([4, 'CORÇA CERINÉIA', 'Finalmente tendo capturado o javali, Hércules ganhou 30 de graça. E descobriu,uma nova tarefa. No monte Cerineu – também próximo da região da Arcádia –havia uma corça com chifres de ouro e pés de bronze. Ela era muito veloz e tinha que ser capturada viva. ']))
             opcao = hercules.menu(['Encontrar um mercador.', ' Comprar chinelos de Dédalo.', 'Comprar chicote para capturar a corça.', 'Atacar a Corça!.'])       
             if opcao == "1":
                 print("Você encontrou o mercador")
             elif opcao == "2":   
                 print("Você comprou chinelos de Dédalo")
                 hercules.graca -= 60
             elif opcao == "3":
                 print("Você comprou o chicote")
                 hercules.graca -= 15
             elif opcao == "4":
                 print("Atacar a corça")   
                 arma = hercules.menu_ataque(['Chinelos', 'Chicote', 'Usar as mãos '])   
                 if arma == "1":
                     hercules.arma == True
                     print("Você encontrou a corça")
                 if arma == "2":
                     if hercules.arma == True:
                         print("Você capturou a corça")
                         hercules.graca += 40
                         hercules.energia -= 15
                         trabalho +=1
                         hercules.graca += hercules.getBencao()
                         print('')
                         hercules.linha() 
                     else:
                         print("Você não tem o necessario pra capturar a corça!")
                 if arma == "3":
                    print("Você usou força bruta! A corça não foi capturada") 
                      

        if trabalho == 5:
            print(hercules.mensagem_inicial([5, 'AVES DO ESTÍNFALE', '“Parabéns! Após ter encontrado a corça nas margens de um rio, você a capturou e ganhou 40 de graça! Você segue o seu caminho e ao acampar em um bosque, às margens do lago Estínfale, no norte da Arcádia, escondiam-se aves que, além de devorar as colheitas da região, também atacavam os homens.Você precisa matar essas aves e usar um antigo instrumento de cordas para atraí-las!. ']))
            opcao = hercules.menu(['Achar um mercador no Bosque. ', ' Comprar um címbalo. ', 'Comprar uma espada. ', 'Atacar as aves!'])
            if opcao == "1":
                print("Você achou um mercador no Bosque")
            elif opcao == "2":
                print("Você comprou um címbalo, que custou 70 graças")
                hercules.graca -= 70   
            elif opcao == "3":
                print("Você comprou uma espada, custou 50 graças ")
                hercules.graca -= 50   
            elif opcao == "4":
                print("Atacar as aves!")
                arma = hercules.menu_ataque(['Flechas', 'Címbalo', 'Espada '])   
                if arma == "1":
                    print("Você machucou o monstro, mas não o matou.")
                    hercules.energia -= 50
                elif arma == "2":
                    print("Você atraiu o monstro")
                    hercules.energia += 20
                elif arma == "3":
                    print("Você matou o monstro")
                    hercules.energia -= 20
                    hercules.graca += 15    
                    trabalho +=1
                    hercules.graca += hercules.getBencao()
                    print('')
                    hercules.linha()
        if trabalho == 6:
            print(hercules.mensagem_inicial([6, 'CAVALARIÇAS DE AÚGIAS ', '“Ual! Você já está no seu sexto desafio! Agora o importante rei Áugias da cidade de Élida, região oeste de Arcádia, ficou sabendo de sua fama em caçar criaturas e gostaria que você lavasse todo o estrume de seu estábulo. Prometendo uma grande recompensa! ']))
            opcao = hercules.menu(['Comprar uma veste nova.', ' Comprar uma espada nova. ', 'Comprar comida. ', 'Limpar estábulos. '])
            if opcao == "1":
                print("Você comprou uma veste nova, portanto perdeu 10 graças")
                hercules.graca -= 10
            elif opcao == "2":
                print("Você comprou uma espada nova, portanto perdeu 25 graças")
                hercules.graca -= 25
            elif opcao == "3":
                print("Você comprou comida, por isso está mais forte")
                hercules.energia += 20
            elif opcao == "4":
                print("Você limpou os estábulos")
                arma = hercules.menu_ataque(['Usar Clava', ' Usar Címbalo', 'Usar Flechas ', 'Usar as mãos'])
                if arma == "1":
                    hercules.graca -= 10
                elif arma == "2":
                    hercules.graca -= 10
                elif arma == "3":
                    hercules.graca -= 10
                elif arma == "4":
                    print("Você ganhou!") #coloquei como estava escrito, mas não entendi muito bem esse "ganhar"
                    hercules.graca += 30
                    trabalho +=1
                    hercules.graca += hercules.getBencao()
                    print('')
                    hercules.linha()
        if trabalho == 7 :     
             print(hercules.mensagem_inicial([7, 'TOURO DE CRETA ', 'Agora você está conhecido por sua coragem e humildade perante as tarefas. Sabendo de um touro que foi amaldiçoado por Poseidon, você resolve ir até a cidade de Creta resgatar o animal e trazê-lo para o continente consigo. Você vai precisar de alimento para o touro,vai precisar convence-lo a lhe acompanhar e ter muita coragem! ']))
             opcao = hercules.menu(['Comprar comida para o touro. ', ' Aprimorar o chicote.', 'Alimentar o touro. ', 'Capturar o touro. '])      
             if opcao == "1":
                 print("Você comprou comida para o touro")
                 hercules.graca -= 10
             elif opcao == "2": #*
                 print("Você aprimorou o chicote")
                 hercules.graca -= 30
             elif opcao == "3":
                 print("Você alimentou o touro")
                 hercules.graca += 10
             elif opcao == "4":
                 print("Você capturou o touro")
                 arma = hercules.menu_ataque([ ' Usar Címbalo', 'Usar o chicote ', 'Usar a espada'])
                 if arma == "1":
                     hercules.arma == True
                     print("Você conseguiu encantar o touro")
                     hercules.energia += 10
                 elif arma == "2":
                      if hercules.arma == True:
                          print("Você capturou o touro")
                          trabalho +=1
                          hercules.graca += hercules.getBencao()
                          print('')
                          hercules.linha()    
                 elif arma == "3": 
                       print ("GameOver --- você feriu o touro, essa não era a sua tarefa!")

        if trabalho == 8:
            print(hercules.mensagem_inicial([8, 'ÉGUAS DE DIOMEDES', 'Parabéns por você ter chegado até aqui! No caminho você ficou sabendo de uma história, que Diomerdes, filho de Ares o famoso Deus da Guerra, possui quatro éguas ferozes e carnívoras, que são alimentadas com os estrangeiros que aparecem em suas terras. Disposto a acabar com essa tortura, você terá que encontrar as éguas e decidir o que fazer para evitar que elas continuem matando os viajantes! Você pode usar armas! Você precisará de força e esperteza!']))  
            opcao = hercules.menu(['Aprimorar a espada. ', 'Aprimorar o arco.', 'Procurar as éguas no estábulo de Diomedes. ', 'ATACAR as éguas'])
            if opcao == '1':
                hercules.graca -= 10
                hercules.arma = True
            elif opcao == '2':
                hercules.graca -= 20
                hercules.arma = True
            elif opcao == '3':
                if hercules.arma == True:
                    print('Você encontrou as éguas.')
                arma = hercules.menu_ataque([ 'Chicote ', 'Flecha ', 'Espada'])
                if arma == '1':
                    print('Você as capturou!')
                    hercules.energia -= 50
                elif arma == '2':
                    print('Você foi atingido!')
                    hercules.vida -= 30
                elif arma == '3':
                    print('Você capturou e enfraqueceu as éguas, como vingança você jogou Diomedes para alimentá-las e ganhou 50 de vida')
                    hercules.vida += 50
                    trabalho +=1
                    hercules.graca += hercules.getBencao()
                    hercules.linha()
                    print('')
                else:
                    print('Você precisa aprimorar suas armas.')
            elif arma == '4':
                    print('Não era para atacar as éguas.')    

        if trabalho == 9:
            print(hercules.mensagem_inicial([9, 'Cinto de Hipólita', 'Uffa! Você está chegando no final. Um pedido especial do rei Euristeus, levou você até a amazona Hipólita, que possui um lindo cinto! Você precisa conseguilo para levar ao rei, mas Hipólita não quer lhe entregar. Você pode tentar negociar pacificamente com a rainha; Você pode mata-la. As ações terão consequências']))  
            opcao = hercules.menu(['Conversar com Hipóltia. ', 'Oferecer a sua espada a Hipólita.', 'Atacar Hipólita.'])
            if opcao == '1':
                hercules.graca += 5
                print('')
            elif opcao == '2':
                hercules.graca += 50
                print('')
            elif opcao == '3':
                arma = hercules.menu_ataque([ 'Espada ', 'Flecha', 'Próprias mãos'])
                if arma == '1':
                    print('Golpe fatal. Você ganhou o cinto')
                    trabalho +=1
                    hercules.graca += hercules.getBencao()
                    print('')
                    hercules.linha()
                elif arma == '2':
                        print('Causou dano, ganhou o cinto mas não venceu')
                elif arma == '3':
                        print('Perdeu o cinto, não concluiu o trabalho')
                        break
        if trabalho == 10:
            print(hercules.mensagem_inicial([10, 'Bois de Gérion', 'Ao infinito e além! Euristeus tem outra tarefa para você! Agora você precisa enfrentar Eurítion e seu cão, ambos possuem mais de uma cabeça e guardam um rebanho de bois carnívoros. Você ficou sabendo que eles andam atormentando a ilha de Erítia, agora é sua vez de derrota-los!']))  
            opcao = hercules.menu(['Usar o címbalo para distrair os bois.', 'Comprar veneno para os cães.', 'Envenenar o cão','Atacar Euriton'])
            if opcao == '1':
                hercules.vida -= 15
                print('Não foi uma boa opção, você foi ferido')
            elif opcao == '2':
                hercules.arma = True
                print('Agora você tem veneno para usar contra os cães.')
            elif opcao == '3':
                if hercules.arma == True:
                    print('Você matou o cão.')
                else:
                    print('Você precisa comprar veneno.')
            elif opcao == '4':
                if hercules.arma == True:
                    arma = hercules.menu_ataque([ 'Espada ', 'Usar as mãos'])
                    if arma == '1':
                        print('Golpe fatal, você venceu!')
                        trabalho +=1
                        hercules.graca = hercules.getBencao()
                        hercules.linha()
                        print('')
                    elif arma == '2':
                        print('Não foi uma boa escolha')
                        break
                    

        if trabalho == 11:
            print(hercules.mensagem_inicial([11, 'Pomos de Ouro', 'Agora você precisa achar as famosas maças douradas, também chamadas de POMO DE OURO. Mas no caminho você encontra o gigante Atlas, sofrendo ao carregar o “peso do mundo”. Você precisa ajuda-lo e quem sabe obter a recompensa depois?\nDica: A bondade sempre prevalece, use-a a seu favor.']))  
            opcao = hercules.menu(['Oferecer comida a atlas.', 'Oferecer água e ambrosia a Atlas.', 'Ajudar Atlas a carregar o peso do céu.', 'Atacar atlas.'])
            if opcao == '1':
                print('Você ganhou força com essa ação!')
            elif opcao == '2':
                print('Você ajudou atlas e por isso o gigante irá lhe recompensar. Enquanto você o auxilia a segurar o “peso do céu”, ele lhe estendeu uma maça de ouro. A bondade e generosidade sempre prevalecem. Parabéns pela sua jornada!”')
                
            elif opcao == '3':
                trabalho +=1
                hercules.graca += hercules.getBencao()
                hercules.linha()
                print('')

            elif opcao == '4':
                break
            

        if trabalho == 12:
            print(hercules.mensagem_inicial([12, 'GUARDIÃO DO HADES', 'Euristeus tem um último pedido,para deixar você livre dos hercules. Ele gostaria de ver de perto o famoso cão de três cabeças Cérbero. Para isso você precisará ir até a entrada do submundo de Hades, atrair o cão e convecê-lo a ir com você visitar Euristeus. Essa é a sua última tarefa. Faça com sabedoria!”']))  
            opcao = hercules.menu(['Envenenar o cão.', 'Usar o címbalo para agradar o cão.', 'Pedir a Cérbero que lhe acompanhe.'])
            if opcao == '1':
                break
            elif opcao == '2':
                print('O cão foi convencido!')
                hercules.arma = True
            elif opcao == '3':
                if hercules.arma == True:
                    print('Cérbero irá lhe acompanhar pois quer conhecer o mundo. ')
                else:
                    break
                sleep(1)
                print('Levando o cão')
                sleep(2)
                print('Mostrar Cérbero a Euristeus...')
                sleep(2)
                print('Levar Cérbero de volta.')
                sleep(1)
                break
    if trabalho == 12:
        print('\tVOCÊ VENCEU!\nVocê cumpriu todas as tarefas desta jornada. Parabéns por ter participado deste caminho conosco. Lhe convidamos a conhecer um pouco mais da mitologia grega através de livros e vídeos! Estamos muito felizes que você chegou até o final!')
        print('')
        print('"Enfrentar o futuro é sempre uma batalha, é sempre uma prova, é sempre algo de guerra.\nNão contra o tempo, porque não vamos batalhar contra ele. É uma guerra contra as dificuldades e contra nossas debilidades.')
        print('\tDelia Steinberg Guzmán')
    else:
        print('Game Over')

