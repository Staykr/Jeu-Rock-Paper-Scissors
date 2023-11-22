import random
# Determiner le choix de l'utilisateur
def choix_utilisateur():
    print("1 = Pierre")
    print("2 = Papier")
    print("3 = Ciseaux")
    choix = input("Faites votre choix (1, 2, ou 3) : ")
    return int(choix)

# Determiner le choix de l'ordi
def choix_ordinateur():
    return random.randint(1, 3)

# Condition pour Gagner
def determiner_gagnant(choix_utilisateur: int, choix_ordinateur: int):
    regles = {
        (1, 1): "Égalité! (CHOKBAR DE ZINZIN)",
        (1, 2): "L'ordinateur a gagné! DOMMAGE...",
        (1, 3): "Vous avez gagné! GG WP",
        (2, 1): "Vous avez gagné! GG WP",
        (2, 2): "Égalité! (CHOKBAR DE ZINZIN)",
        (2, 3): "L'ordinateur a gagné! DOMMAGE...",
        (3, 1): "L'ordinateur a gagné! DOMMAGE...",
        (3, 2): "Vous avez gagné! GG WP",
        (3, 3): "Égalité! (CHOKBAR DE ZINZIN)"
    }
# Comment obtenir le résultat
    resultat = regles.get((choix_utilisateur, choix_ordinateur), "Choix invalides!")
    return resultat

# Fonction pour relancer le jeu
def relancer_jeu():
    return input("Voulez-vous relancer le jeu? (Oui(o)/Non(n)): ").lower() == "o"

# Fonction pour le déroulement du jeu
def jouer():
    print("Bienvenue au jeu Pierre-Papier-Ciseaux!")
    
    while True:
        choix_user: int = choix_utilisateur()
        choix_pc: int = choix_ordinateur()
        
        print("Vous avez choisi " + str(choix_user))
        print("L'ordinateur a choisi " + str(choix_pc))
        
        resultat = determiner_gagnant(choix_user, choix_pc)
        print(resultat)
        
        if not relancer_jeu():
            print("Merci d'avoir joué! A la prochaine.")
            break

# Appeler la fonction jouer pour commencer le jeu
jouer()