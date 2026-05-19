# Jeu du Pendu

## Description

Programme permettant de jouer au jeu du pendu. Le programme choisit un mot aléatoire dans un fichier texte et le joueur doit le deviner lettre par lettre avant d'épuiser ses 6 chances.

---

## Fonctionnalités

- Sélection aléatoire d'un mot depuis un fichier texte (`mots_pendu.txt`)
- Possibilité de fournir son propre fichier de mots
- Gestion des accents : `é è ê à â û …` → `e e e a a u …` via un dictionnaire
- Affichage de l'état du mot avec `_` pour les lettres non devinées
- Suivi des lettres déjà jouées
- Détection de victoire et de défaite
- Proposition de rejouer ou quitter après chaque partie
- Bonus: indice automatique quand il ne reste qu'une seule chance (révèle une lettre qui n'est pas dans le mot)

---

## Structure du projet

```
main.py           # Script principal du jeu
mots_pendu.txt    # Fichier de mots par défaut
README.md         # Ce fichier
```

---

## Utilisation

### Lancer le jeu

Au démarrage, le programme demande si vous souhaitez utiliser votre propre fichier de mots :

- **Laissez vide** → utilise `mots_pendu.txt` (doit être dans le même dossier que `main.py`)
- **Entrez le nom d'un fichier dans le dossier** → ex. `mots_pendu_test.txt` (permet de tester la fonctionnalité avec un fichier texte qui ne contient que le mot `abricot`)


### Format du fichier de mots

Un mot par ligne, encodage UTF-8. Les accents sont acceptés (car ils seront automatiquement normalisés).

---

## Fonctions

Le programme est uniquement composé de fonctions :

- `normaliser(texte)`: Retire les accents via un dictionnaire et met le texte en minuscules
- `choisir_mot(mots_pendu)`: Sélectionne un mot aléatoire dans la liste
- `etat_mot(mot, lettres_trouvees)`: Retourne le mot masqué avec des `_` pour les lettres non devinées
- `charger_mots(chemin_fichier)`: Charge et normalise les mots depuis un fichier texte
- `est_mot_devine(mot, lettres_trouvees)`: Retourne `True` si toutes les lettres du mot ont été trouvées
- `demander_lettre(lettres_deja_jouees)`: Valide et retourne la lettre saisie par le joueur
- `mettre_a_jour_chances(lettre, mot, chances)`: Décrémente les chances si la lettre est absente du mot
- `proposer_rejouer()`: Demande au joueur de rejouer ou de quitter
- `demander_fichier_mots()`: Demande le chemin d'un fichier de mots personnalisé
- `donner_indice(mot, lettres_trouvees)`: Révèle une lettre qui n'est pas dans le mot
- `jouer_une_partie(liste_mots)`: Gère le déroulement complet d'une partie
- `main()`: Point d'entrée du programme
