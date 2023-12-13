from tkinter import Tk, Listbox, StringVar, Button, Entry, messagebox, Label, scrolledtext, Toplevel
import tkinter as tk
import os
import json
import ctypes
import statistics



 #Récuparation de la taille de l'écran de l'utilisateur
def taille_ecran(fenetre):
    taille = ctypes.windll.user32
    largeur= taille.GetSystemMetrics(0)
    hauteur= taille.GetSystemMetrics(1)
    return fenetre.geometry(f"{largeur}x{hauteur}")


class Application:
    def __init__(self, master):
        self.master = master
        master.title("Application")

        self.nb_joueurs = None
        self.mode_jeu = None

        # Partie 1: Mode de jeu
        self.label_mode_jeu = Label(master, text="Sélectionnez le Mode de jeu:")
        self.label_mode_jeu.pack()
        self.frame_mode_jeu = Listbox(master)
        self.frame_mode_jeu.insert(1, "Strict")
        self.frame_mode_jeu.insert(2, "Médiane")
        self.frame_mode_jeu.insert(3, "Moyenne")
        self.frame_mode_jeu.insert(4, "Majorité absolue")
        self.frame_mode_jeu.insert(5, "Majorité relative")
        self.frame_mode_jeu.pack()

        # Partie 2: Nombre de joueur
        self.label_nbJoueur = Label(master, text="Entrez le nombre de joueurs:")
        self.label_nbJoueur.pack()
        self.frame_nbJoueur = Entry(master, textvariable=int, width=30)
        self.frame_nbJoueur.pack()

        #valider le choix du nombre de joueur
        self.bouton_valider = Button(master, text="Valider", command=self.entrer_pseudos)
        self.bouton_valider.pack()

        # aggrandir la taille de la fenetre
        taille_ecran(master)

    def entrer_pseudos(self):
        self.nb_joueurs = int(self.frame_nbJoueur.get())
        fenetre_pseudo = Toplevel(self.master)
        fenetre_pseudo.title("Pseudo")

        # Utiliser une liste pour stocker les StringVar
        self.liste_values = []
        for nb in range(self.nb_joueurs):
            # Entrée des pseudos
            value = StringVar()
            self.liste_values.append(value)
            entree = Entry(fenetre_pseudo, textvariable=value, width=30)
            entree.pack()

        bouton_valider_pseudo = Button(fenetre_pseudo, text="Valider", command=self.recupere_pseudos)
        bouton_valider_pseudo.pack()

        # Maximiser la fenêtre
        taille_ecran(fenetre_pseudo)

    def recupere_mode(self):
        # Récupérer ici le mode de jeu sélectionné
        self.mode_jeu = self.frame_mode_jeu.get(self.frame_mode_jeu.curselection())
        print("Mode de jeu:", self.mode_jeu)

        # Vérifier le mode de jeu
        if self.mode_jeu == "Strict":
            fenetre_strict=Tk()
            fenetre_strict.title("Mode Strict")
            # Instancier la classe mode_stricte
            instance_stricte = mode_stricte(fenetre_strict)
            fenetre_strict.mainloop()

    def recupere_nb_joueur(self):
        # Récupérer ici le nombre de joueurs
        self.nb_joueurs = self.frame_nbJoueur.get()
        print("Nombre de joueurs:", self.nb_joueurs)
        return self.nb_joueurs

    def recupere_pseudos(self):
        self.recupere_mode()
        self.recupere_nb_joueur()
        # Récupérer les pseudos à partir de la liste des StringVar
        pseudos = [value.get() for value in self.liste_values]
        print("Pseudos:", pseudos)
        fenetre_pseudo = self.bouton_valider.winfo_toplevel()
        fenetre_pseudo.destroy()

class gestion_json():
    def __init__(self, master):
        taille_ecran(master)
        self.creer_fichier_json()

        # Création d'une zone de texte extensible avec une barre de défilement
        zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=10)
        zone_texte.pack(padx=10, pady=10)

        # Création des zones de texte et des étiquettes correspondantes
        self.label_num = Label(master, text="Numéro:")
        self.label_num.pack(anchor=tk.W)
        self.entree_num = Entry(master)
        self.entree_num.pack(anchor=tk.W)

        self.label_nom = Label(master, text="Nom:")
        self.label_nom.pack(anchor=tk.W)
        self.entree_nom = Entry(master)
        self.entree_nom.pack(anchor=tk.W)

        self.label_description = Label(master, text="Description:")
        self.label_description.pack(anchor=tk.W)
        self.entree_description = Entry(master)
        self.entree_description.pack(anchor=tk.W)

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:self.sauvegarder_donnees(self.entree_num,self.entree_nom,self.entree_description))

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer", command=lambda:self.recommencer_partie(self.entree_num,self.entree_nom,self.entree_description))

        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_num.pack(padx=5, pady=5,anchor=tk.W)

        self.label_nom.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_nom.pack(padx=5, pady=5,anchor=tk.W)

        self.label_description.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_description.pack(padx=5, pady=5,anchor=tk.W)

        bouton_sauvegarder.pack(pady=10, anchor=tk.W)

        bouton_recommencer.pack(pady=10, anchor=tk.W)

    def creer_fichier_json(self):
        chemin_fichier = "donnees.json"
        if not os.path.exists(chemin_fichier):
            with open(chemin_fichier, "w") as fichier_json:
                json.dump({"tableau": []}, fichier_json, indent=4)


    def sauvegarder_donnees(self, entry_num, entry_nom, entry_description):
        # Récupérer les données depuis les zones de texte
        num = entry_num.get()
        nom = entry_nom.get()
        description = entry_description.get()

        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        # Ajouter les nouvelles données au tableau existant
        nouvelle_donnee = {"num": num, "nom": nom, "description": description, "estimation": self.estimation}
        donnees_existantes["tableau"].append(nouvelle_donnee)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)

    def recommencer_partie(self, entry_num, entry_nom, entry_description):
        # Effacer les zones de texte
        entry_num.delete(0, tk.END)
        entry_nom.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        # Effacer les données du fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump({"tableau": []}, fichier_json, indent=4)

class mode_stricte():
    def __init__(self, master) :
        
        self.master = master
        taille_ecran(master)
        master.title("Choix_vote")
    
        self.estimation=[]
        self.ensemble_estimation=[]

        #Bouton de Vote
        bouton_valider0 = Button(master, text=0,command=lambda : self.sauvegarder_estimation(0))
        bouton_valider0.pack()

        bouton_valider1 = Button(master, text=1,command=lambda : self.sauvegarder_estimation(1))
        bouton_valider1.pack()

        bouton_valider2 = Button(master, text=2,command=lambda : self.sauvegarder_estimation(2))
        bouton_valider2.pack()

        bouton_valider3 = Button(master, text=3,command=lambda : self.sauvegarder_estimation(3))
        bouton_valider3.pack()

        bouton_valider5 = Button(master, text=5,command=lambda : self.sauvegarder_estimation(5))
        bouton_valider5.pack()

        bouton_valider8 = Button(master, text=8,command=lambda : self.sauvegarder_estimation(8))
        bouton_valider8.pack()

        bouton_valider13 = Button(master, text=13,command=lambda : self.sauvegarder_estimation(13))
        bouton_valider13.pack()

        bouton_valider20 = Button(master, text=20,command=lambda : self.sauvegarder_estimation(20))
        bouton_valider20.pack()

        bouton_valider40 = Button(master, text=40,command=lambda : self.sauvegarder_estimation(40))
        bouton_valider40.pack()

        bouton_valider100 = Button(master, text=100,command=lambda : self.sauvegarder_estimation(100))
        bouton_valider100.pack()

        bouton_valider_nsp = Button(master, text="Ne Nais Pas",command=lambda : self.sauvegarder_estimation("Ne Sais Pas"))
        bouton_valider_nsp.pack()

        bouton_validerpause= Button(master, text="Pause",command=lambda : self.sauvegarder_estimation("Pause"))
        bouton_validerpause.pack()

        self.regle_strict()
        self.sauv_estim_json()


    def sauvegarder_estimation(self, valeur):

        # Stockage des informations dans la liste estimation
        self.estimation.append(valeur)
        print(self.estimation)
        
    def regle_strict(self):
        self.ensemble_estimation = set(self.estimation)
        if len(self.ensemble_estimation)==1:
            print("uuuuuuuuu")
        else:
            print("vvvvvvvvvvv")
    
    def sauv_estim_json(self):
        
        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        if len(self.ensemble_estimation) == 1:
            nouvelle_donnee = {"estimation": (self.ensemble_estimation)}
            donnees_existantes["tableau"].append(nouvelle_donnee)
        else:
            print("La regle strict n'est pas satisfaite. Ne sauvegarde pas dans le fichier JSON.")

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)
        

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()

    principale=Tk()
    app2=gestion_json(principale)
    principale.mainloop()