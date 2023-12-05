import tkinter as tk
from tkinter import Tk, Listbox, Radiobutton, StringVar, Button, Entry, messagebox, Label, scrolledtext
import string
import json
import ctypes

#Pour fermer une fenêtre
def fermer_fenetre(fenetre):
    fenetre.destroy()

 #Récuparation de la taille de l'écran de l'utilisateur
def taille_ecran(fenetre):
    taille = ctypes.windll.user32
    largeur= taille.GetSystemMetrics(0)
    hauteur= taille.GetSystemMetrics(1)
    return fenetre.geometry(f"{largeur}x{hauteur}")

#Récupérer le pseudo des joueurs
def recupere_pseudo():
    pseudo=entree.get()
    fermer_fenetre(fenetre_pseudo)
    liste_pseudo.append(pseudo)
    return liste_pseudo

#Vérifier si le nombre entrée est bien un nombre
def verif (nb):
    return nb.isdigit()

#Récupérer le nombre de joueur    
def recupere():

    global nb_joueur_val
    nb_joueur_val=entree.get()

    if verif(nb_joueur_val): 
        fermer_fenetre(fenetre_nb_joueur)
        
        #Conversention d'un str en integer
        nb_joueur_val=int(nb_joueur_val)
    else :
        messagebox.showerror("/!\ Erreur","Veuillez saisir un nombre entier")
    
    return(nb_joueur_val)

def sauvegarder_donnees():
    # Récupérer les données depuis les zones de texte
    num = entry_num.get()
    nom = entry_nom.get()
    description = entry_description.get()

    # Charger les données existantes depuis le fichier JSON
    with open("donnees.json", "r") as fichier_json:
        donnees_existantes = json.load(fichier_json)
    

    # Ajouter les nouvelles données au tableau existant
    nouvelle_donnee = {"num": num, "nom": nom, "description": description, "estimation": ""}
    donnees_existantes["tableau"].append(nouvelle_donnee)

    # Sauvegarder les données mises à jour dans le fichier JSON
    with open("donnees.json", "w") as fichier_json:
        json.dump(donnees_existantes, fichier_json, indent=4)

def recommencer_partie():
    # Effacer les zones de texte
    entry_num.delete(0, tk.END)
    entry_nom.delete(0, tk.END)
    entry_description.delete(0, tk.END)

    # Effacer les données du fichier JSON
    with open("donnees.json", "w") as fichier_json:
        json.dump({"tableau": []}, fichier_json, indent=4)


### Lancement de la fenêtre mode local ou distance
fenetre_LD = Tk()
fenetre_LD.title("Local ou Distance")
taille_ecran(fenetre_LD)


# Définission du choix mode local ou distance
value = StringVar(value="AucunChoix") 
local = Radiobutton(fenetre_LD, text="Local", variable=value, value="Local").pack()
distance = Radiobutton(fenetre_LD, text="Distance", variable=value, value="Distance").pack()

# Création d'un bouton fictif caché pour que local et distance ne soit pas coché par défaut
aucun_choix = Radiobutton(fenetre_LD, text="", variable=value, value="AucunChoix", state="disabled")
aucun_choix.pack_forget()  # Cacher le bouton 

#Création du bouton valider
bouton_valider = Button(fenetre_LD, text="Valider", command=lambda: fermer_fenetre(fenetre_LD)).pack()

fenetre_LD.mainloop()
# Fin de la fenêtre Local ou Distance


### Lancement de la fenêtre Mode de jeu
fenetre_mode = Tk()
fenetre_mode.title("Mode de jeu")
taille_ecran(fenetre_mode)

# Définition de la liste avec le choix du mode de jeu
liste = Listbox(fenetre_mode)
liste.insert(1, "Strict")
liste.insert(2, "Médiane")
liste.insert(3, "Moyenne")
liste.insert(4, "Majorité absolue")
liste.insert(5, "Majorité relative")
liste.pack()

#Création du bouton valider
bouton_valider_mode = Button(fenetre_mode, text="Valider", command=lambda: fermer_fenetre(fenetre_mode)).pack()

fenetre_mode.mainloop()
#Fin de la fenêtre Mode de jeu

### Lancement de la fenêtre nombre de joueur
fenetre_nb_joueur = Tk()
fenetre_nb_joueur.title("Nombre de joueur")
taille_ecran(fenetre_nb_joueur)

#Création de la zone de saisie pour le nombre de joueur
entree = Entry(fenetre_nb_joueur, textvariable=int, width=30) 
entree.pack()

#Création du bouton valider
bouton_valider_joueur = Button(fenetre_nb_joueur, text="Valider", command=recupere) #Utilisations de la fonction récupérer
bouton_valider_joueur.pack()

fenetre_nb_joueur.mainloop()
# Fin de la fenêtre Nombre de joueur

#Initialisation de la liste vide pour stocker les noms des joueurs
liste_pseudo=[]
for nb in range(nb_joueur_val): # La boucle va ouvrir une fenêtre pour les pseudos pour autant qu'il a de joueur

    ### Lancement de la fenêtre pseudo dans la boucle
    fenetre_pseudo = Tk()
    fenetre_pseudo.title("Pseudo")
    taille_ecran(fenetre_pseudo)

    # Création de la zone de texte pour les pseudos
    entree = Entry(fenetre_pseudo, textvariable=string, width=30)
    entree.pack()
    # Création du bouton pour valider
    bouton_valider_pseudo = Button(fenetre_pseudo, text="Valider", command=recupere_pseudo) # Utilisation de la fonction pour récupérer et stocker les pseudo par la suite
    bouton_valider_pseudo.pack()
    fenetre_pseudo.mainloop()
    # Fin de la fenêtre pseudo pour le ième joueur

### Lancement de la fenêtre pour les règles de jeu
fenetre_regle=Tk()
fenetre_regle.title("Règle de jeu")
taille_ecran(fenetre_regle)

Texte=f"Bienvenue à {liste_pseudo} pour cette nouvelle partie de Planning Poker. \n Les règles de jeu sont les suivantes :"

# Création de la zone avec l'affichage des différentes règles
aff_regle=Label(fenetre_regle, text=Texte).pack()

fenetre_regle.mainloop()
# Fin de la fenêtre Règle de jeu

### Lancement de la fenêtre principale
fenetre_principal = tk.Tk()
fenetre_principal.title("Principale")
taille_ecran(fenetre_principal)

# Création d'une zone de texte extensible avec une barre de défilement
zone_texte = scrolledtext.ScrolledText(fenetre_principal, wrap=tk.WORD, width=50, height=10)
zone_texte.pack(padx=10, pady=10)


# Création des zones de texte et des étiquettes correspondantes
label_num = Label(fenetre_principal, text="Numéro:")
entry_num = Entry(fenetre_principal)

label_nom = Label(fenetre_principal, text="Nom:")
entry_nom = Entry(fenetre_principal)

label_description = Label(fenetre_principal, text="Description:")
entry_description = Entry(fenetre_principal)

# Création d'un bouton pour sauvegarder les données
bouton_sauvegarder = Button(fenetre_principal, text="Sauvegarder", command=sauvegarder_donnees)

# Création d'un bouton pour recommencer la partie
bouton_recommencer = Button(fenetre_principal, text="Recommencer", command=recommencer_partie)


# Placement des étiquettes, zones de texte et bouton dans la fenêtre
label_num.pack(padx=5, pady=5, anchor=tk.W)
entry_num.pack(padx=5, pady=5)

label_nom.pack(padx=5, pady=5, anchor=tk.W)
entry_nom.pack(padx=5, pady=5)

label_description.pack(padx=5, pady=5, anchor=tk.W)
entry_description.pack(padx=5, pady=5)

bouton_sauvegarder.pack(pady=10)

bouton_recommencer.pack(pady=10)


fenetre_principal.mainloop()
# Fin de la fenêtre principale


##
