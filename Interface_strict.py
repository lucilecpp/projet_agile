from tkinter import Tk, Listbox, StringVar, Button, Entry, messagebox, Label, scrolledtext, Toplevel
import tkinter as tk
import os
import json
import ctypes
from collections import Counter
import statistics


def taille_ecran(fenetre):
    taille = ctypes.windll.user32
    largeur= taille.GetSystemMetrics(0)
    hauteur= taille.GetSystemMetrics(1)
    return fenetre.geometry(f"{largeur}x{hauteur}")

class Application:

    # Définition d'une variable de classe pour suivre les tours

    tour_actuel = 1
    def __init__(self, master):
        self.master = master
        master.title("Application")
        
        # Aggrandir la taille de la fenêtre
        taille_ecran(master)
       
       # A chaque nouvel appel la liste des pseudo est réinitialisé ainsi que le mode du jeu
        self.list_pseudos=[]
        self.mode=None

        self.effacer_donnee_json()

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
        self.label_nbJoueur = Label(master, text="Entrez le nombre de joueurs \n Veuillez entrer un entier : ")
        self.label_nbJoueur.pack()
        self.frame_nbJoueur = Entry(master, textvariable=int, width=30)
        self.frame_nbJoueur.pack()

        # Valider le choix du nombre de joueur
        self.bouton_valider = Button(master, text="Valider", command=lambda : self.entrer_pseudos())
        self.bouton_valider.pack()

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer", command=lambda:self.recommencer_partie())
        self.bouton_recommencer.pack()
        

    def entrer_pseudos(self):
        # Récupération du nombre de joueur saisi par l'utilisateur
        self.nb_joueurs = self.frame_nbJoueur.get()

        # Vérification que le nombre entrer est bien un chiffre
        if self.nb_joueurs.isdigit():

            # Convertion en entier
            self.nb_joueurs=int(self.nb_joueurs)

            # Vérification du nombre de joueur
            if 1 <= self.nb_joueurs <= 6:
                fenetre_pseudo = Toplevel(self.master)

                # Aggrandir la fenêtre
                taille_ecran(fenetre_pseudo)
                fenetre_pseudo.title("Pseudo")

                # Utiliser une liste pour stocker les StringVar
                self.liste_values = []
                for _ in range(self.nb_joueurs):

                    # Entrée des pseudos
                    value = StringVar()
                    self.liste_values.append(value)
                    self.label_pseudo = Label(fenetre_pseudo, text="Entrez le pseudo :")
                    self.label_pseudo.pack()
                    entree = Entry(fenetre_pseudo, textvariable=value, width=30)
                    entree.pack()
                
                bouton_valider_pseudo = Button(fenetre_pseudo, text="Valider", command=self.recupere_pseudos)
                bouton_valider_pseudo.pack()

                self.bouton_recommencer = Button(fenetre_pseudo, text="Recommencer", command=lambda:self.recommencer_partie())
                self.bouton_recommencer.pack()

                self.master.withdraw()
                
            else : messagebox.showerror("/!\ Erreur","Il faut entre 1 et 6 joueurs")

        else : 
            messagebox.showerror("/!\ Erreur","Veuillez saisir un nombre entier")

    def recupere_mode(self):
        # Récupérer ici le mode de jeu sélectionné

        print("arriver")
    
        print("arriver")
        self.mode_jeu = self.frame_mode_jeu.get(self.frame_mode_jeu.curselection())
        print("arriver")
        self.mode=self.mode_jeu
        print("Mode de jeu:", self.mode_jeu)
        

        if self.tour_actuel == 1:
            # Au premier tour, utiliser toujours le mode strict
            self.mode = "Strict"

        # Cas pour le mode strict
        if self.mode_jeu == "Strict":
            fenetre_strict=Tk()
            fenetre_strict.title("Mode Strict")

            # Instance de la classe Mode_Strict
            instance_stricte = Mode_Strict(fenetre_strict, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_strict.mainloop()

        # Cas pour le mode Moyenne
        elif self.mode_jeu == "Moyenne":
            fenetre_moyenne=Tk()
            fenetre_moyenne.title("Mode Moyenne")

            # Instance de la classe Mode_Moyenne
            instance_moyenne = Mode_Moyenne(fenetre_moyenne, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_moyenne.mainloop()

        # Cas pour le mode Médiane
        elif self.mode_jeu == "Médiane":
            fenetre_mediane=Tk()
            fenetre_mediane.title("Mode Médiane")

            # Instance de la classe Mode_Médiane
            instance_mediane = Mode_Mediane(fenetre_mediane, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_mediane.mainloop()

        # Cas pour la majorité absolue
        elif self.mode_jeu == "Majorité absolue":
            fenetre_maj_abs=Tk()
            fenetre_maj_abs.title("Mode Majorité Absolue")

            # Instance de la classe Mode_Majorité_Absolue
            instance_maj_abs = Mode_Majorite_Absolue(fenetre_maj_abs, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_maj_abs.mainloop()

        # Cas pour la majorité relative
        elif self.mode_jeu == "Majorité relative":
            fenetre_maj_rel=Tk()
            fenetre_maj_rel.title("Mode Majorité relative")

            # Instance de la classe Mode_Majorité_Relative
            instance_maj_rel = Mode_Majorite_Relative(fenetre_maj_rel, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_maj_rel.mainloop()

    def recupere_nb_joueur(self):

        # Récupérer le nombre de joueurs
        self.nb_joueurs = self.frame_nbJoueur.get()
        if (self.nb_joueurs.isdigit()):
            pass
        else : 
            messagebox.showerror("/!\ Erreur","Veuillez saisir un nombre entier")
        print("Nombre de joueurs:", self.nb_joueurs)
        return self.nb_joueurs

    def recupere_pseudos(self):
        self.recupere_nb_joueur()

        # Récupérer les pseudos à partir de la liste des StringVar
        pseudos = [value.get() for value in self.liste_values]

        # Stocker les pseudos dans list_pseudo
        self.list_pseudos.extend(pseudos)

        print("Pseudos:", pseudos)
        self.fenetre_pseudo = self.bouton_valider.winfo_toplevel()
        self.bouton_recommencer = Button(self.master, text="Recommencer", command=lambda:self.recommencer_partie())
        self.bouton_recommencer.pack()     
        
    
        # Appeler la méthode recupere_mode
        self.recupere_mode()
        
    def recommencer_partie(self):
        # Destruction de la fenêtre actuelle
        self.master.destroy()

        # Lancement d'une nouvelle fenêtre pour recommencer la partie
        fenetre=Tk()
        app = Application(fenetre)
        fenetre.mainloop()

        self.effacer_donnee_json()

    def effacer_donnee_json(self):
        # Effacer les données du fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump({"tableau": []}, fichier_json, indent=4)


class Mode_Strict():
    def __init__(self, master, pseudo, nb, fenetre) :
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Strict")        

        # Pour stocker les estimations
        self.estimation=[]
        
        # Pour créer le json s'il n'est pas déjà présent
        self.creer_fichier_json()

        # Création d'une zone de texte extensible en tant que bloc-note
        self.zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.zone_texte.grid(row=0, column=999)

        # Ajout du texte par défaut
        self.zone_texte.insert(tk.END, "Cette zone est un bloc-note, Servez-vous en pour noter vos idées.")


        # Création d'un Label pour expliquer les règles
        regle="Bienvenue dans cette partie de planning poker. Pour que la partie se déroule correctement veuillez suivre les instructions suivantes : \n - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description. Cliquez sur sauvegarder ! \n - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. \n - /!\ Si vous cliquez sur recommencer les tâches et estimations enregistrées seront perdues \n - Pour visualiser les tâches et estimations validées cliquez sur afficher les données \n - Toutes vos estimations sont faites ? Appuyez sur Fin de la Partie pour quitter l'interface. "
        self.zone_texte = Label(master, text=regle, font=("Arial",10),anchor=tk.W, justify=tk.LEFT)
        self.zone_texte.grid(row=0, column=0)

        
        # Création des zones de texte et des étiquettes correspondantes

        # Pour le numéro de la tâche
        self.label_num = Label(master, text="Numéro :")
        self.label_num.grid()
        self.entree_num = Entry(master)
        self.entree_num.grid()

        # Pour le nom de la tâche
        self.label_nom = Label(master, text="Nom :")
        self.label_nom.grid()
        self.entree_nom = Entry(master)
        self.entree_nom.grid()

        # Pour la description de la tâche
        self.label_description = Label(master, text="Description :")
        self.label_description.grid()
        self.entree_description = Entry(master)
        self.entree_description.grid()

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:self.sauvegarder_donnees())

        # Création d'un bouton pour entrer une tâche
        bouton_tache=Button(master, text="Tâche suivante", command=lambda:self.tache_suivante())

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:self.recommencer_partie_mode())

        # Création d'un bouton pour afficher les données du json
        bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:self.afficher_donnees_json())

        # Bouton pour mettre fin à la partie
        bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :self.fin_de_partie(fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        bouton_sauvegarder.grid()

        bouton_tache.grid()

        bouton_recommencer.grid()

        bouton_afficher_json.grid()

        bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

        # Définition des boutons de vote
        for k in (pseudo) :
            for i, value in enumerate(liste_valeur):
                for j in range(int(nb)) :    
                        self.label_pseudo = Label(master, text=f"A \n {k} \n de voter")
                        self.label_pseudo.grid(row=0, column=10+j+10)
                        button = Button(self.master, text=value, command=lambda v=value: self.vote_estimation(v, int(nb)))
                        button.grid(row=i + 1, column=10+j+10)
        
    def vote_estimation(self, valeur, nb_j):

        if valeur =="Pause":
            self.pause()
        else : 
            # Stockage des informations dans la liste estimation
            self.estimation.append(valeur)
            print(self.estimation)

            if len(self.estimation)==nb_j:
                self.sauvegarder_estimation()
            else:
                pass
    
    def verif_regle(self):

        # Initiation d'une variable pour connaitre le statut de la fonction
        indice=False

        # Suppression des doublons
        self.estimation_final = set(self.estimation)

        # Vérification de la longueur de la liste soit égale à 1"
        if len(self.estimation_final)==1:
            print(self.estimation_final, len(self.estimation_final))
            indice=True
        else : 
            print("Y a un souci", len(self.estimation_final))
            messagebox.showinfo("Attention","La règle stricte n'est pas respectée. \n Veuillez recommencez")

            # Passage de la liste des estimations à vides pour recommencer
            self.estimation=[]
        return indice

    def sauvegarder_estimation(self):    
        if self.verif_regle()==True:

            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": str(self.estimation_final)}
                donnees_existantes["tableau"].append(nouvelle_donnee)

                # Sauvegarder les données mises à jour dans le fichier JSON
                with open("donnees.json", "w") as fichier_json:
                    json.dump(donnees_existantes, fichier_json, indent=4)
                messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")
                
    def creer_fichier_json(self):
            chemin_fichier = "donnees.json"
            if not os.path.exists(chemin_fichier):
                with open(chemin_fichier, "w") as fichier_json:
                    json.dump({"tableau": []}, fichier_json, indent=4)

    def sauvegarder_donnees(self):
        print("Sauv dans le Json")
        # Récupérer les données depuis les zones de texte
        num = self.entree_num.get()
        nom = self.entree_nom.get()
        description = self.entree_description.get()

        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        # Ajouter les nouvelles données au tableau existant
        nouvelle_donnee = {"num": num, "nom": nom, "description": description}
        donnees_existantes["tableau"].append(nouvelle_donnee)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)

    def recommencer_partie_mode(self):

        # Appel de la fonction tache_suivante pour réinitisaliser les paramètres de l'interface
        self.tache_suivante()
        
        # Utilsiation de la fonction recommencer_partie de la classe mère
        Application.recommencer_partie(self)
        self.master.destroy()
          
    def fin_de_partie(self, fenetre_app):

        # Affichage d'un message d'au revoir
        messagebox.showinfo("Fin de partie","A bientôt !")

        # Ferme la fenêtre
        self.master.destroy()
        fenetre_app.destroy()
    
    def tache_suivante(self):
        self.entree_num.delete(0, tk.END)
        self.entree_nom.delete(0, tk.END)
        self.entree_description.delete(0, tk.END)
        self.estimation=[]

        # Incrémentation de la variable tour_actuel
        Application.tour_actuel+=1
        print(Application.tour_actuel)
    
    def afficher_donnees_json(self):

        # Charger les données depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees = json.load(fichier_json)

        # Convertir les données en une chaîne de caractères
        donnees_str = json.dumps(donnees, indent=4)
        donnnee_json=Tk()
        donnnee_json.title("Données Json")

        # Création d'une zone pour afficher les données du json
        self.zone_json_texte=scrolledtext.ScrolledText(donnnee_json, wrap=tk.WORD, width=50, height=20)
        self.zone_json_texte.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Afficher les données dans la zone de texte
        self.zone_json_texte.delete(1.0, tk.END)  # Efface le contenu existant
        self.zone_json_texte.insert(tk.END, donnees_str)
    
    def pause(self):
        messagebox.showinfo("Pause","Vous êtes en pause. \n Cliquez sur OK pour reprendre la partie")

class Mode_Moyenne(Mode_Strict):
    def __init__(self, master, pseudo, nb, fenetre) :
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Moyenne")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)


        # Création d'une zone de texte extensible en tant que bloc-note
        self.zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.zone_texte.grid(row=0, column=999)

        # Ajout du texte par défaut
        self.zone_texte.insert(tk.END, "Cette zone est un bloc-note, Servez-vous en pour noter vos idées.")


        # Création d'un Label pour expliquer les règles
        regle="Bienvenue dans cette partie de planning poker. Pour que la partie se déroule correctement veuillez suivre les instructions suivantes : \n - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description. Cliquez sur sauvegarder ! \n - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. \n - /!\ Si vous cliquez sur recommencer les tâches et estimations enregistrées seront perdues \n - Pour visualiser les tâches et estimations validées cliquez sur afficher les données \n - Toutes vos estimations sont faites ? Appuyez sur Fin de la Partie pour quitter l'interface. "
        self.zone_texte = Label(master, text=regle, font=("Arial",10),anchor=tk.W, justify=tk.LEFT)
        self.zone_texte.grid(row=0, column=0)

        
        # Création des zones de texte et des étiquettes correspondantes

        # Pour le numéro de la tâche
        self.label_num = Label(master, text="Numéro :")
        self.label_num.grid()
        self.entree_num = Entry(master)
        self.entree_num.grid()

        # Pour le nom de la tâche
        self.label_nom = Label(master, text="Nom :")
        self.label_nom.grid()
        self.entree_nom = Entry(master)
        self.entree_nom.grid()

        # Pour la description de la tâche
        self.label_description = Label(master, text="Description :")
        self.label_description.grid()
        self.entree_description = Entry(master)
        self.entree_description.grid()

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        bouton_sauvegarder.grid()

        bouton_tache.grid()

        bouton_recommencer.grid()

        bouton_afficher_json.grid()

        bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

        # Définition des boutons de vote
        for k in (pseudo) :
            for i, value in enumerate(liste_valeur):
                for j in range(int(nb)) :    
                        self.label_pseudo = Label(master, text=f"A \n {k} \n de voter")
                        self.label_pseudo.grid(row=0, column=10+j+10)
                        button = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_moyenne(v))
                        button.grid(row=i + 1, column=10+j+10)
        
    def vote_estimation_moyenne(self, valeur):
       
        if valeur =="Pause":
            Mode_Strict.pause(self)
        else : 
            # Vérification que la valeur Ne Sais Pas ne soit pas ajouter à la liste
            if valeur != "Ne Sais Pas":
                self.estimation.append(valeur)
                print(self.estimation)

            # Si la valeur est Ne Sais Pas, on décrémente le nombre de joueur de 1
            if valeur == "Ne Sais Pas":
                self.nb -= 1

            if len(self.estimation) == self.nb:
                self.sauvegarder_estimation_moyenne()
        
    def calcul_moyenne(self):

        if len(self.estimation)==self.nb:
                moyenne=statistics.mean(self.estimation)
                print(moyenne)

        return moyenne

    def sauvegarder_estimation_moyenne(self):    

            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_moyenne()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

                # Sauvegarder les données mises à jour dans le fichier JSON
                with open("donnees.json", "w") as fichier_json:
                    json.dump(donnees_existantes, fichier_json, indent=4)
                messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

class Mode_Mediane(Mode_Strict):
    def __init__(self, master, pseudo, nb, fenetre) :
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Médiane")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Création d'une zone de texte extensible en tant que bloc-note
        self.zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.zone_texte.grid(row=0, column=999)

        # Ajout du texte par défaut
        self.zone_texte.insert(tk.END, "Cette zone est un bloc-note, Servez-vous en pour noter vos idées.")


        # Création d'un Label pour expliquer les règles
        regle="Bienvenue dans cette partie de planning poker. Pour que la partie se déroule correctement veuillez suivre les instructions suivantes : \n - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description. Cliquez sur sauvegarder ! \n - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. \n - /!\ Si vous cliquez sur recommencer les tâches et estimations enregistrées seront perdues \n - Pour visualiser les tâches et estimations validées cliquez sur afficher les données \n - Toutes vos estimations sont faites ? Appuyez sur Fin de la Partie pour quitter l'interface. "
        self.zone_texte = Label(master, text=regle, font=("Arial",10),anchor=tk.W, justify=tk.LEFT)
        self.zone_texte.grid(row=0, column=0)

        
        # Création des zones de texte et des étiquettes correspondantes

        # Pour le numéro de la tâche
        self.label_num = Label(master, text="Numéro :")
        self.label_num.grid()
        self.entree_num = Entry(master)
        self.entree_num.grid()

        # Pour le nom de la tâche
        self.label_nom = Label(master, text="Nom :")
        self.label_nom.grid()
        self.entree_nom = Entry(master)
        self.entree_nom.grid()

        # Pour la description de la tâche
        self.label_description = Label(master, text="Description :")
        self.label_description.grid()
        self.entree_description = Entry(master)
        self.entree_description.grid()

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        bouton_sauvegarder.grid()

        bouton_tache.grid()

        bouton_recommencer.grid()

        bouton_afficher_json.grid()

        bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

        # Définition des boutons de vote
        for k in (pseudo) :
            for i, value in enumerate(liste_valeur):
                for j in range(int(nb)) :    
                        self.label_pseudo = Label(master, text=f"A \n {k} \n de voter")
                        self.label_pseudo.grid(row=0, column=10+j+10)
                        button = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_mediane(v))
                        button.grid(row=i + 1, column=10+j+10)
        
    def vote_estimation_mediane(self, valeur):
       
        if valeur =="Pause":
            Mode_Strict.pause(self)
        else : 
            # Vérification que la valeur Ne Sais Pas ne soit pas ajouter à la liste
            if valeur != "Ne Sais Pas":
                self.estimation.append(valeur)
                print(self.estimation)

            # Si la valeur est Ne Sais Pas, on décrémente le nombre de joueur de 1
            if valeur == "Ne Sais Pas":
                self.nb -= 1

            if len(self.estimation) == self.nb:
                self.sauvegarder_estimation_mediane()
        
    def calcul_mediane(self):

        if len(self.estimation)==self.nb:
                moyenne=statistics.median(self.estimation)
                print(moyenne)

        return moyenne

    def sauvegarder_estimation_mediane(self):    

            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_mediane()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

                # Sauvegarder les données mises à jour dans le fichier JSON
                with open("donnees.json", "w") as fichier_json:
                    json.dump(donnees_existantes, fichier_json, indent=4)
                messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")
                
class Mode_Majorite_Absolue(Mode_Strict):
    def __init__(self, master, pseudo, nb, fenetre) :
        
        self.master = master
        taille_ecran(master)
        master.title("Mode majorité absolue")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Création d'une zone de texte extensible en tant que bloc-note
        self.zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.zone_texte.grid(row=0, column=999)

        # Ajout du texte par défaut
        self.zone_texte.insert(tk.END, "Cette zone est un bloc-note, Servez-vous en pour noter vos idées.")


        # Création d'un Label pour expliquer les règles
        regle="Bienvenue dans cette partie de planning poker. Pour que la partie se déroule correctement veuillez suivre les instructions suivantes : \n - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description. Cliquez sur sauvegarder ! \n - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. \n - /!\ Si vous cliquez sur recommencer les tâches et estimations enregistrées seront perdues \n - Pour visualiser les tâches et estimations validées cliquez sur afficher les données \n - Toutes vos estimations sont faites ? Appuyez sur Fin de la Partie pour quitter l'interface. "
        self.zone_texte = Label(master, text=regle, font=("Arial",10),anchor=tk.W, justify=tk.LEFT)
        self.zone_texte.grid(row=0, column=0)

        
        # Création des zones de texte et des étiquettes correspondantes

        # Pour le numéro de la tâche
        self.label_num = Label(master, text="Numéro :")
        self.label_num.grid()
        self.entree_num = Entry(master)
        self.entree_num.grid()

        # Pour le nom de la tâche
        self.label_nom = Label(master, text="Nom :")
        self.label_nom.grid()
        self.entree_nom = Entry(master)
        self.entree_nom.grid()

        # Pour la description de la tâche
        self.label_description = Label(master, text="Description :")
        self.label_description.grid()
        self.entree_description = Entry(master)
        self.entree_description.grid()

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        bouton_sauvegarder.grid()

        bouton_tache.grid()

        bouton_recommencer.grid()

        bouton_afficher_json.grid()

        bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

        # Définition des boutons de vote
        for k in (pseudo) :
            for i, value in enumerate(liste_valeur):
                for j in range(int(nb)) :    
                        self.label_pseudo = Label(master, text=f"A \n {k} \n de voter")
                        self.label_pseudo.grid(row=0, column=10+j+10)
                        button = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_majorite_abs(v))
                        button.grid(row=i + 1, column=10+j+10)

    def vote_estimation_majorite_abs(self, valeur):
       
        if valeur =="Pause":
            Mode_Strict.pause(self)
        else : 
            # Vérification que la valeur Ne Sais Pas ne soit pas ajouter à la liste
            if valeur != "Ne Sais Pas":
                self.estimation.append(valeur)
                print(self.estimation)

            # Si la valeur est Ne Sais Pas, on décrémente le nombre de joueur de 1
            if valeur == "Ne Sais Pas":
                self.nb -= 1

            len(self.estimation) == self.nb
            self.sauvegarder_estimation_majorite_abs()

    def calcul_majorite_abs(self):
        if len(self.estimation) == self.nb:

            # Comptage de chaque occurrences de chaque estimation
            compteur_estimations = Counter(self.estimation)

            # Valeur qui apparaît le plus fréquemment
            majorite_absolue = compteur_estimations.most_common(1)[0][0]

        return majorite_absolue

    def sauvegarder_estimation_majorite_abs(self):
            
            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_majorite_abs()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

            # Sauvegarder les données mises à jour dans le fichier JSON
            with open("donnees.json", "w") as fichier_json:
                json.dump(donnees_existantes, fichier_json, indent=4)

            messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

class Mode_Majorite_Relative(Mode_Strict):
    def __init__(self, master, pseudo, nb, fenetre):
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Majorité Relative")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Création d'une zone de texte extensible en tant que bloc-note
        self.zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.zone_texte.grid(row=0, column=999)

        # Ajout du texte par défaut
        self.zone_texte.insert(tk.END, "Cette zone est un bloc-note, Servez-vous en pour noter vos idées.")

        # Création d'un Label pour expliquer les règles
        regle="Bienvenue dans cette partie de planning poker. Pour que la partie se déroule correctement veuillez suivre les instructions suivantes : \n - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description. Cliquez sur sauvegarder ! \n - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. \n - /!\ Si vous cliquez sur recommencer les tâches et estimations enregistrées seront perdues \n - Pour visualiser les tâches et estimations validées cliquez sur afficher les données \n - Toutes vos estimations sont faites ? Appuyez sur Fin de la Partie pour quitter l'interface. "
        self.zone_texte = Label(master, text=regle, font=("Arial",10),anchor=tk.W, justify=tk.LEFT)
        self.zone_texte.grid(row=0, column=0)

        # Création des zones de texte et des étiquettes correspondantes

        # Pour le numéro de la tâche
        self.label_num = Label(master, text="Numéro :")
        self.label_num.grid()
        self.entree_num = Entry(master)
        self.entree_num.grid()

        # Pour le nom de la tâche
        self.label_nom = Label(master, text="Nom :")
        self.label_nom.grid()
        self.entree_nom = Entry(master)
        self.entree_nom.grid()

        # Pour la description de la tâche
        self.label_description = Label(master, text="Description :")
        self.label_description.grid()
        self.entree_description = Entry(master)
        self.entree_description.grid()

        # Création d'un bouton pour sauvegarder les données
        bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        bouton_sauvegarder.grid()

        bouton_tache.grid()

        bouton_recommencer.grid()

        bouton_afficher_json.grid()

        bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

        # Définition des boutons de vote
        for k in (pseudo) :
            for i, value in enumerate(liste_valeur):
                for j in range(int(nb)) :    
                        self.label_pseudo = Label(master, text=f"A \n {k} \n de voter")
                        self.label_pseudo.grid(row=0, column=10+j+10)
                        button = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_majorite_rel(v))
                        button.grid(row=i + 1, column=10+j+10)

    def vote_estimation_majorite_rel(self, valeur):
       
        if valeur =="Pause":
            Mode_Strict.pause(self)
        else : 
            # Vérification que la valeur Ne Sais Pas ne soit pas ajouter à la liste
            if valeur != "Ne Sais Pas":
                self.estimation.append(valeur)
                print(self.estimation)

            # Si la valeur est Ne Sais Pas, on décrémente le nombre de joueur de 1
            if valeur == "Ne Sais Pas":
                self.nb -= 1

            len(self.estimation) == self.nb
            self.sauvegarder_estimation_majorite_rel()
        

    def calcul_majorite_rel(self):

        # Compteur des estimations
        compteur_estimations = Counter(self.estimation)

        # Les éléments sont triées par ordre décroissantes
        estimations_triees = sorted(compteur_estimations.items(), key=lambda x: x[1], reverse=True)

        # Stockage de la valeur la plus fréquente
        valeur_majoritaire = estimations_triees[0]

        return valeur_majoritaire
    
    def sauvegarder_estimation_majorite_rel(self):

        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        nouvelle_donnee = {"estimation": self.calcul_majorite_rel()}
        donnees_existantes["tableau"].append(nouvelle_donnee)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)
        
        messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")



if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
    
    '''principale2=Tk()
    app2=Mode_Majorite_Absolue(principale2, ["mm","ll","sdf","qsdf","zer","zerty"], 6, None)
    principale2.mainloop()'''

    '''principale2=Tk()
    app2=Mode_Majorite_Relative(principale2, ["mm","ll","sdf","qsdf","zer","zerty"], 6, None)
    principale2.mainloop()'''

    '''principale2=Tk()
    app2=Mode_Strict(principale2, ["mm"], app)
    principale2.mainloop()'''
    
    '''principale=Tk()
    app2=Mode_Moyenne(principale, ["mm"],1 , None)
    principale.mainloop()
    '''



'''class gestion_json():
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

class Mode_Strict(Application):
    def __init__(self, master, pseudo) :
        
        self.master = master
        taille_ecran(master)
        master.title("Choix vote")        
        
        self.estimation=[]
        
        for k in (pseudo) :
                        self.label_pseudo = Label(master, text=f"A {k} de voter")
                        self.label_pseudo.pack()
  
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

                        self.bouton_recommencer = Button(master, text="Recommencer", command=lambda:self.recommencer_partie())
                        self.bouton_recommencer.pack()

    def sauvegarder_estimation(self, valeur):

        # Stockage des informations dans la liste estimation
        self.estimation.append(valeur)

        self.estimation_final = set(self.estimation)

        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        if len(self.estimation_final) == 1:
            nouvelle_donnee = {"estimation": sum(self.estimation_final)}
            donnees_existantes["tableau"].append(nouvelle_donnee)
        else:
            print(self.estimation)
            messagebox.showinfo("Attention","La règle stricte n'est pas respectée. \n Veuillez recommencez")
            self.estimation=[]
            print("La règle strict n'est pas satisfaite.", self.estimation)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)'''


'''class Mode_Strict(Application):
    def __init__(self, master, pseudo, fenetre) :
        
        self.master = master
        taille_ecran(master)
        master.title("Choix vote")        
        
        # Pour stocker les estimations
        self.estimation=[]

        # Pour créer le json s'il n'est pas déjà présent
        self.creer_fichier_json()

        # Création d'une zone de texte extensible avec une barre de défilement
        zone_texte = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=10)
        zone_texte.pack(padx=10, pady=10, anchor=tk.W)

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

        bouton_fin_de_partie = tk.Button(master, text="Fin de Partie", command=lambda :self.fin_de_partie(fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_num.pack(padx=5, pady=5,anchor=tk.W)

        self.label_nom.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_nom.pack(padx=5, pady=5,anchor=tk.W)

        self.label_description.pack(padx=5, pady=5,anchor=tk.W)
        self.entree_description.pack(padx=5, pady=5,anchor=tk.W)

        bouton_sauvegarder.pack(pady=10, anchor=tk.W)

        bouton_recommencer.pack(pady=10, anchor=tk.W)

        bouton_fin_de_partie.pack(pady=10, anchor=tk.W)

        # Affichage des boutons de vote     
        for k in (pseudo) :
            self.label_pseudo = Label(master, text=f"A {k} de voter")
            self.label_pseudo.pack(side="top", anchor="center")

            #Bouton de Vote
            bouton_valider0 = Button(master, text=0,command=lambda : self.vote_estimation(0))
            bouton_valider0.pack(side="top", anchor="center")

            bouton_valider1 = Button(master, text=1,command=lambda : self.vote_estimation(1))
            bouton_valider1.pack(side="top", anchor="center")

            bouton_valider2 = Button(master, text=2,command=lambda : self.vote_estimation(2))
            bouton_valider2.pack(side="top", anchor="center")

            bouton_valider3 = Button(master, text=3,command=lambda : self.vote_estimation(3))
            bouton_valider3.pack(side="top", anchor="center")

            bouton_valider5 = Button(master, text=5,command=lambda : self.vote_estimation(5))
            bouton_valider5.pack(side="top", anchor="center")

            bouton_valider8 = Button(master, text=8,command=lambda : self.vote_estimation(8))
            bouton_valider8.pack(side="top", anchor="center")

            bouton_valider13 = Button(master, text=13,command=lambda : self.vote_estimation(13))
            bouton_valider13.pack(side="top", anchor="center")

            bouton_valider20 = Button(master, text=20,command=lambda : self.vote_estimation(20))
            bouton_valider20.pack(side="top", anchor="center")

            bouton_valider40 = Button(master, text=40,command=lambda : self.vote_estimation(40))
            bouton_valider40.pack(side="top", anchor="center")

            bouton_valider100 = Button(master, text=100,command=lambda : self.vote_estimation(100))
            bouton_valider100.pack(side="top", anchor="center")

            bouton_valider_nsp = Button(master, text="Ne Nais Pas",command=lambda : self.vote_estimation("Ne Sais Pas"))
            bouton_valider_nsp.pack(side="top", anchor="center")

            bouton_validerpause= Button(master, text="Pause",command=lambda : self.vote_estimation("Pause"))
            bouton_validerpause.pack(side="top", anchor="center")
    
    def vote_estimation(self, valeur):
        # Stockage des informations dans la liste estimation
        self.estimation.append(valeur)
        print(self.estimation)

    def sauvegarder_estimation(self):     

        self.estimation_final = set(self.estimation)

        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        if len(self.estimation_final) == 1:
            nouvelle_donnee = {"estimation": sum(self.estimation_final)}
            donnees_existantes["tableau"].append(nouvelle_donnee)
        else:
            print(self.estimation)
            messagebox.showinfo("Attention","La règle stricte n'est pas respectée. \n Veuillez recommencez")
            self.estimation=[]
            print("La règle strict n'est pas satisfaite.", self.estimation)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)
                
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

    def fin_de_partie(self, fenetre_app):
        # Ferme la fenêtre
        self.master.destroy()
        fenetre_app.destroy()'''