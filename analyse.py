# -------------------------
# Analyse de notes
# -------------------------

import random

# Liste d'élèves
eleves = [
    "Nathan E",
    "Sarah M",
    "Lucas D",
    "Emma L",
    "Hugo R",
    "Inès K",
    "Thomas B",
    "Lina A",
    "Alex P",
    "Camille S",
    "Julien T",
    "Manon C",
    "Rayan H",
    "Clara P",
    "Mehdi Z",
    "Laura V",
    "Enzo G",
    "Sofia N",
    "Yanis O",
    "Chloé D"
]

# Dictionnaire : nom de l'élève -> note
notes = {}

def generer_notes_aleatoires():

    for eleve in eleves:
        notes[eleve] = random.randint(0, 20)

def afficher_menu():
    print("\n===== Actions =====")
    print("1 - Afficher les élèves")
    print("2 - Afficher les notes")
    print("3 - Afficher la moyenne de la classe")
    print("4 - Afficher la meilleure note")
    print("5 - Afficher la pire note")
    print("6 - Afficher les élèves au-dessus de la moyenne")
    print("0 - Quitter le programme")


def afficher_eleves():
    print("\n===== Élèves de la classe =====")
    for name in eleves:
        print(name)

def afficher_notes():
    print("\n===== Notes de la classe =====")
    for note in notes.items():   
        print(note)


def calculer_moyenne():
    total = 0
    for note in notes.values():
        total += note
    moyenne = total / len(notes)
    return moyenne

def afficher_meilleure_note():
    meilleure_note = -1
    meilleur_eleve = ""

    for eleve, note in notes.items():
        if note > meilleure_note:
            meilleure_note = note
            meilleur_eleve = eleve

    print(f"\n🏆 Meilleure note : {meilleure_note}/20")
    print(f"👤 Élève : {meilleur_eleve}")


def afficher_pire_note():
    pire_note = 21
    pire_eleve = ""

    for eleve, note in notes.items():
        if note < pire_note:
            pire_note = note
            pire_eleve = eleve

    print(f"\n Pire note : {pire_note}/20")
    print(f"👤 Élève : {pire_eleve}")


def afficher_eleves_au_dessus_moyenne():
    moyenne = calculer_moyenne()
    print(f"\n📈 Élèves au-dessus de la moyenne ({moyenne}/20) :")

    for eleve, note in notes.items():
        if note > moyenne:
            print(f" - {eleve} : {note}/20")


generer_notes_aleatoires()
while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        afficher_eleves()

    elif choix == "2":            
        afficher_notes()

    elif choix == "3":
        moyenne = calculer_moyenne()
        print("\n📊 Moyenne de la classe :"  , moyenne)
    
    elif choix == "4":
        afficher_meilleure_note()

    elif choix == "5":
        afficher_pire_note()

    elif choix == "6":
        afficher_eleves_au_dessus_moyenne()

    elif choix == "0":
        print("Au revoir !")
        break   

