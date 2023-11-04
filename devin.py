import random

def menu():
	print("1- L'ordinateur choisit un nombre et vous le devinez")
	print("2- Vous choisissez un nombre et l'ordinateur le devine")
	print("0- Quitter le programme") 
	
#R2 : Comment demander le choix de l’utilisateur
	choix = int(input("Votre choix : "  ))
	
#R2 : Comment traiter le choix de l’utilisateur
	if choix == 1: 
		user_guess()
	elif choix == 2 :
		machine_guess()
	elif choix == 0 :
		print ("Au revoir...")

#R2 : Comment "Demander un nombre à la machine"

def user_guess(): 
    test = 0
    found = False 
    random_number_machine = (random.randint(1, 999+1))

#R2 : Comment "Traiter le choix de la machine"
    print("J'ai choisi un nombre compris entre 1 et 999.")

#R2 : Comment "Demander la réponse de l’utilisateur" 
    while not found: 
        test += 1
        user_answer = int(input(f"Proposition {test} : "))

#R2 : Comment "Traiter la réponse de l’utilisateur 
        if user_answer < random_number_machine:
            print("Trop petit !")
        elif user_answer > random_number_machine:
            print("Trop grand !")
        else:
            find = True
            print("Trouvé ! ")
            replay()

#R2 : Comment "Afficher le nombre d’essai"
            print("Bravo ! Vous avez trouvé en ", test, "essais. ")

def machine_guess():
    test = 0
    found = False
    min = 1
    max = 1000

    user_choice = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ")

    while user_choice != "o":
        if user_choice == "n":
            print("J'attends...")
            user_choice = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ")
        else:
            user_choice = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ")
    
    while not found:
        test += 1 
        machine_answer = int((min + max) / 2)
        print(f"Proposition_machine {test} : {machine_answer}")

        user_answer = input("Trop (g)rand, trop (p)etit ou (t)rouvé ? ")

        if user_answer == "g":
            print("Trop grand")
            max = machine_answer
        elif user_answer == "p":
            print("Trop petit")
            min = machine_answer
        elif user_answer == "t":
            print("J'ai trouvé en", test, "essais.")
            found = True
            replay()
        else:
            print("Je n'ai pas compris la réponse. Merci de répondre :")
            print("     g si ma proposition est trop grande")
            print("     p si ma proposition est trop petite")
            print("     t si j'ai trouvé le nombre")

def replay(): 
    restart = input("Voulez-vous recommencer une autre partie ? o(oui) / n (non) : ")

#R2 : Comment "Traiter le choix de l’utilisateur"
    if restart == "o": 
        menu()
    elif restart == "n":
        print("Au revoir …")
    else: 
        print("Je n’ai pas compris votre réponse")
        print("Merci de taper o pour oui")
        print("Merci de taper n pour non")
        replay()

menu() 

