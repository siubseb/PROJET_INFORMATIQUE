import random
import time

def cls():
	print "\n" * 100

def takeCardPlayer(deckN):
        chosenCard = random.choice(cardsAvailable)
        cardsAvailable.remove(chosenCard)
        if cardsPlayer[deckN][0] == 0:
                cardsPlayer[deckN][0] = chosenCard
        else:
                cardsPlayer[deckN].append(chosenCard)

def takeCardDealer():
	chosenCard = random.choice(cardsAvailable)
	cardsAvailable.remove(chosenCard)
	cardsDealer.append(chosenCard)
	
def valueCardPlayer(deckN):
	value = 0
	for i in range(len(cardsPlayer[deckN])):
		currentCard = cardsPlayer[deckN][i][0]
		if currentCard == "2":
			value = value +2
		if currentCard == "3":
			value = value +3
		if currentCard == "4":
			value = value +4
		if currentCard == "5":
			value = value +5
		if currentCard == "6":
			value = value +6
		if currentCard == "7":
			value = value +7
		if currentCard == "8":
			value = value +8
		if currentCard == "9":
			value = value +9
		if currentCard == "T":
			value = value +10
		if currentCard == "J":
			value = value +10
		if currentCard == "Q":
			value = value +10
		if currentCard == "K":
			value = value +10
		if currentCard == "A":
			value = value +11
	return value

def valueCardDealer():
	value = 0
	for i in range(len(cardsDealer)):
		currentCard = cardsDealer[i][0]
		if currentCard == "2":
			value = value +2
		if currentCard == "3":
			value = value +3
		if currentCard == "4":
			value = value +4
		if currentCard == "5":
			value = value +5
		if currentCard == "6":
			value = value +6
		if currentCard == "7":
			value = value +7
		if currentCard == "8":
			value = value +8
		if currentCard == "9":
			value = value +9
		if currentCard == "T":
			value = value +10
		if currentCard == "J":
			value = value +10
		if currentCard == "Q":
			value = value +10
		if currentCard == "K":
			value = value +10
		if currentCard == "A":
			value = value +11
	return value


play = True

while play == True:
        defaultSleep = 1.5
        cls()
        cardsAvailable = ["2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As","2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad"]
        cardsPlayer = [[0 for x in range(1)] for y in range(3)]
        cardsDealer = []
        betAccepted = False
        playerStop = False
        dealerStop = False
        gains = 0
        canTakeMoreCard = True
        rejouer = ""
        result = [[0 for x in range(1)] for y in range(3)]
        fichier = open("data.txt", "r")
        soldeCompte = float(fichier.read())
        fichier.close()
        
        print "Bienvenue sur BlackJack"
        print "________________________"
        print

        print
        print "---"
        print "Voici le solde de votre compte : ", soldeCompte, "frs"
        print "---"
        print
        print
        while betAccepted != True:
                betSize = raw_input("Veuillez entrer la taille de votre mise (en frs) : ")
                print
                if soldeCompte >= float(betSize):
                        soldeCompte = soldeCompte - float(betSize)
                        betAccepted = True
                        betSize = float(betSize)
        cls()
        print "Jeu en cours, vous misez ", betSize, "frs pour cette partie."
        print "____________"
        print
        print
	
        takeCardPlayer(0)

        takeCardDealer()

        takeCardPlayer(0)
        cardsPlayer[0] = ["5c", "5d"]

        for i in range(3):
                if cardsPlayer[i][0] == 0:
                        break
                else:
                        playerStop = False
                        while playerStop != True:
                                
                                print "Voici vos cartes pour le deck no " + str(i) + " : ", cardsPlayer[i]
                                choix = ""
                                print "	 La valeur de votre main est de :", valueCardPlayer(i)
                                print
                                print
                                print "Le croupier montre : ", cardsDealer
                                print "	 La valeur de la main du croupier est de :", valueCardDealer()
                                print

                                if valueCardPlayer(i) == 21 and len(cardsPlayer[i]) == 2 and valueCardDealer() < 10 :
                                        result[i] = "2CardsBJ" 
                                        playerStop = True
                                        break
                                
                                if valueCardPlayer(i) > 21:
                                        result[i] = "moreThan21"
                                        break


                                if canTakeMoreCard == False:
                                        playerStop = True
                                        break
                                        
                                print
                                print
                                print "Que souhaitez-vous faire..."
                                if len(cardsPlayer[i]) == 2 and cardsPlayer[i][0][0] == cardsPlayer[i][1][0]:
                                        while choix !="T" and choix != "D" and choix != "R" and choix != "S":
                                                choix = raw_input("...[T]irer, [D]oubler, [R]ester ou [S]plit ? ").upper()
                                                print
                                                print
                                                if choix == "T":
                                                        takeCardPlayer(i)
                                                        cls()
                                                        print
                                                        print
                                                        print "Le croupier vous donne une carte ..."
                                                        print


                                                if choix == "D":
                                                        if soldeCompte < betSize:
                                                                print "Vous n'avez pas suffisament de fonds sur votre compte"
                                                                print
                                                                choix = ""
                                                        else:
                                                                betSize = 2 * betSize
                                                                takeCardPlayer(i)
                                                                canTakeMoreCard = False

                                                if choix == "S":
                                                        cardsPlayer[i+1][0] = cardsPlayer[i][1]
                                                        del cardsPlayer[i][1]
                                                        print cardsPlayer
                                                        takeCardPlayer(i)
                                                        takeCardPlayer(i+1)
                                                        print
                                                        print "Le croupier vous donne une carte pour votre deck no "+ str(i)
                                                        print "Le croupier vous donne une carte pour votre deck no "+ str(i+1)
                                                        
                                                        
                                                if choix == "R":
                                                        print
                                                        print
                                                        print "Vous decidez de ne pas tirer de carte."
                                                        print
                                                        playerStop = True





                                                

                                                

                                else:
                                        
                                        while choix !="T" and choix != "D" and choix != "R":
                                                print
                                                print
                                                choix = raw_input("...[T]irer, [D]oubler ou [R]ester ? ").upper()

                                                if choix == "T":
                                                        takeCardPlayer(i)
                                                        cls()
                                                        print
                                                        print
                                                        print "Le croupier vous donne une carte ..."
                                                        print


                                                if choix == "D":
                                                        if soldeCompte < betSize:
                                                                print "Vous n'avez pas suffisament de fonds sur votre compte"
                                                                print
                                                                choix = ""
                                                        else:
                                                                betSize = 2 * betSize
                                                                takeCardPlayer(i)
                                                                canTakeMoreCard = False
                                                        
                                                if choix == "R":
                                                        print
                                                        print
                                                        print "Vous decidez de ne pas tirer de carte."
                                                        print
                                                        playerStop = True


                               
        takeCardDealer()
        print
        print "Le croupier montre : ", cardsDealer
        print "	 La valeur de la main du croupier est de :", valueCardDealer()
	
	
        while dealerStop != True:
                if valueCardDealer() <= 16:
                        print
                        print
                        print "Le croupier prend une carte ..."
                        print
                        takeCardDealer()
                        time.sleep(defaultSleep)
                        print "Le croupier montre : ", cardsDealer
                        print "	 La valeur de la main du croupier est de :", valueCardDealer()
                        print
                        print
                else:
                        print
                        print
                        print "Le croupier arrete de tirer"
                        time.sleep(defaultSleep)
                        print "Le croupier montre : ", cardsDealer
                        print "	 La valeur de la main du croupier est de :", valueCardDealer()
                        print
                        dealerStop = True

                        if result == "":
                                if valueCardDealer() > valueCardPlayer(i) and valueCardDealer() <= 21:
                                        result = "DealerWin"

                                if valueCardDealer() == valueCardPlayer(i):
                                        result = "Draw"
			  
                                if valueCardDealer() > 21:
                                        result = "PlayerWin"
                                else:
                                        if valueCardDealer() < valueCardPlayer(i):
                                                result = "PlayerWin"
			  

        if result == "moreThan21":
                gains = 0
                print
                print "Vous avez malheureusement depasse 21. Vous avez perdu :("
			
		

        if result == "2CardsBJ":
                gains = 2.5 * betSize
                print
                print "BlackJack ! Vous avez gagne ", gains, " frs"
                print " 	", gains, " frs ont ete ajoute a votre compte"
		

        if result == "Draw":
                gains = betSize
                print
                print "Egalite, vous recuperez votre mise"

        if result == "DealerWin":
                gains = 0
                print
                print "Le croupier a ete plus chanceux que vous cette fois-ci ... :("

        if result == "PlayerWin":
                gains = 2 * betSize
                print
                print "Felicitations, vous avez gagne !!!"
                print " 	", gains, " frs ont ete ajoute a votre compte"

        soldeCompte = soldeCompte + gains
        fichier = open("data.txt", "w")
        fichier.write(str(soldeCompte))
        fichier.close()

        print
        while rejouer != "O" and rejouer != "N":
                rejouer = raw_input('Partie terminee... Souhaitez-vous rejouer ? [O]ui, [N]on : ').upper()
        if rejouer == "O":
                play = True
        else: 
                play = False
