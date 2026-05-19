import random

#Constante

CHANCES = 6
MOTS_PAR_DEFAUT = "mots_pendu.txt"

#Fonctions

def normaliser(texte):
    """Renvoie une lettre sans accent par l'intermédiaire d'un dictionnaire"""
    accents = {
        'à': 'a', 'â': 'a', 'á': 'a', 'ä': 'a',
        'è': 'e', 'ê': 'e', 'é': 'e', 'ë': 'e',
        'î': 'i', 'ï': 'i', 'í': 'i', 'ì': 'i',
        'ô': 'o', 'ó': 'o', 'ö': 'o', 'ò': 'o',
        'û': 'u', 'ú': 'u', 'ü': 'u', 'ù': 'u',
        'ç': 'c', 'ñ': 'n',
    }
    resultat =""
    for lettre in texte.lower():
        if lettre in accents:
            resultat += accents[lettre]
        else:
            resultat += lettre
    return resultat

def choisir_mot(mots_pendu):
    """Choisit un mot de la liste"""
    return random.choice(mots_pendu)

def etat_mot(mot_aleatoire, lettres_trouvees):
    """Affiche le mot avec des _ pour les lettres non encore devinées."""
    affichage = ""
    for lettre in mot_aleatoire:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()  # enlève l'espace final

def charger_mots(chemin_fichier=None):
    """
    Charge la liste de mots depuis un fichier texte et la normalise.
    Si aucun fichier n'est fourni, utilise la liste de mots par défaut.
    """
    if chemin_fichier:
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as fichier:  #Si le fichier n'existe pas, une erreur est levée ici
                return [normaliser(ligne.strip()) for ligne in fichier if ligne.strip()]
        except FileNotFoundError:
            print(f"[!] Fichier introuvable : '{chemin_fichier}'. Utilisation de la liste intégrée.")  #On gère le cas d'erreur

    return charger_mots(MOTS_PAR_DEFAUT)

def est_mot_devine(mot, lettres_trouvees):
    for lettre in mot:
        if lettre not in lettres_trouvees:
            return False   #Si une lettre manque, on renvoie faux
    return True            #Toutes les lettres ont été trouvées

def demander_lettre(lettres_deja_jouees):
    """
    Demande à l'utilisateur d'entrer une lettre valide.
    Retourne la lettre normalisée (sans accent, minuscule).
    """
    while True:
        saisie = input("Entrez une lettre : ").strip()
        saisie_normalisee = normaliser(saisie)

        if len(saisie_normalisee) != 1:
            print(" Veuillez entrer une seule lettre !")
        elif not saisie_normalisee.isalpha():
            print(" Veuillez entrer une lettre de l'alphabet !")
        elif saisie_normalisee in lettres_deja_jouees:
            print(f" Vous avez déjà joué la lettre '{saisie_normalisee}' !")
        else:
            return saisie_normalisee

def mettre_a_jour_chances(lettre, mot, chances):
    """
    Vérifie si la lettre est dans le mot et met à jour le nombre de chances restantes
    """
    if lettre in mot:
        return chances, True
    return chances - 1, False

def proposer_rejouer():
    """
    Propose au joueur de rejouer ou de quitter.
    """
    while True:
        choix = input("\n   Nouvelle partie ? (o/n) : ").strip().lower()
        if choix in ("o", "oui", "y", "yes"):
            return True
        if choix in ("n", "non", "no"):
            return False
        print("  Répondez par 'o' (oui) ou 'n' (non).")

def demander_fichier_mots():
    """
    Demande à l'utilisateur s'il veut fournir son propre fichier de mots.
    Retourne le chemin du fichier choisi (ou None pour utiliser le défaut).
    """
    print("\n  Voulez-vous utiliser votre propre fichier de mots ?")
    choix = input("  (Laissez vide pour utiliser le fichier par défaut) : ").strip()
    if choix:
        return choix
    return None

def donner_indice(mot, lettres_trouvees):
    """
    Révèle une lettre qui n'est pas encore dans le mot
    parmi les lettres de l'alphabet non encore jouées.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lettres_hors_mot = alphabet - set(mot) - lettres_trouvees
    if lettres_hors_mot:
        indice = random.choice(list(lettres_hors_mot))
        return indice
    return None


def jouer_une_partie(liste_mots):
    """
    Gère le déroulement complet d'une partie.
    Retourne True si le joueur souhaite rejouer, False pour quitter.
    """
    mot = choisir_mot(liste_mots)
    chances = CHANCES
    lettres_trouvees = set()
    lettres_jouees = set()

    print("Nouvelle partie")
    print(f"  Le mot contient {len(mot)} lettres.")

    #Boucle du jeu
    while chances > 0:
        print(f"  Chances restantes : {chances}")
        print(f"  Lettres jouées    : {', '.join(sorted(lettres_jouees)) or '—'}")
        print(f"  Mot               : {etat_mot(mot, lettres_trouvees)}\n")

        #Indice quand il reste une seule chance
        if chances == 1:
            indice = donner_indice(mot, lettres_jouees)
            if indice:
                print(f" INDICE : la lettre '{indice}' n'est PAS dans le mot.")

        lettre = demander_lettre(lettres_jouees)
        lettres_jouees.add(lettre)

        chances, dans_le_mot = mettre_a_jour_chances(lettre, mot, chances)

        if dans_le_mot:
            lettres_trouvees.add(lettre)
            print(f"\n Bonne réponse ! '{lettre}' est dans le mot.")
        else:
            print(f"\n Mauvaise réponse. '{lettre}' n'est pas dans le mot.")

        #En cas de victoire
        if est_mot_devine(mot, lettres_trouvees):
            print(f"\n  FELICITATIONS ! Vous avez trouvé le mot : « {mot} »")
            return proposer_rejouer()

    #En cas de défaite
    print(f"\n  DOMMAGE ! Le mot était : « {mot} »")
    return proposer_rejouer()

def main():
    chemin = demander_fichier_mots()
    liste_mots = charger_mots(chemin)
    rejouer = True
    while rejouer:
        rejouer = jouer_une_partie(liste_mots)
main()