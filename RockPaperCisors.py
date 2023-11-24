import random
# User choice
def user_choice():
    print("1 = Pierre")
    print("2 = Papier")
    print("3 = Ciseaux")
    while True:
        choice = input("Faites votre choix (1, 2, ou 3) : ")
        
        try:
            return int(choice)
        except ValueError:
            print("Erreur : Veuillez entrer un nombre.")

# Computer choice
def pc_choice():
    return random.randint(1, 3)

# Win condition
def choose_winer(choix_utilisateur: int, choix_ordinateur: int):
    rules = {
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
# Print an error message if the user writes a choice other than those available
    result = rules.get((choix_utilisateur, choix_ordinateur), "Choix invalides!")
    return result

# Function to restart the game
def restart_game():
    return input("Voulez-vous relancer le jeu? (Oui(o)/Non(n)): ").lower() == "o"

# Gameplay
def play():
    
    while True:
        print("Bienvenue au jeu Pierre-Papier-Ciseaux!")
        choix_user: int = user_choice()
        choix_pc: int = pc_choice()

        print("Vous avez choisi " + str(choix_user))
        print("L'ordinateur a choisi " + str(choix_pc))
        
        result = choose_winer(choix_user, choix_pc)
        print(result)
        
        if not restart_game():
            print("Merci d'avoir joué! A la prochaine.")
            break

#Call the function to start the game
play()
