from tkinter import Tk, StringVar, Button, Entry, messagebox, Label, scrolledtext, Toplevel
import tkinter as tk
import os
import json
import ctypes
from collections import Counter
import statistics

"""
@file 
@brief Ce fichier est le fichier principal du projet
@author Lucile Perbet
@author Monica Mortelette
@date 2023
"""



def taille_ecran(fenetre):
    """ 
    @brief Fonction permettant de définir la taille de la fenêtre en fonction de la résolution de l'écran
    @param fenetre : la fenêtre à redimentionner
    @return : Les dimensions de la fenêtre
    """
    taille = ctypes.windll.user32
    largeur= taille.GetSystemMetrics(0)
    hauteur= taille.GetSystemMetrics(1)
    return fenetre.geometry(f"{largeur}x{hauteur}")
 
class Application:
     """
     @class Application
     @brief Class principale du projet

     Elle permet de récupérer les informations le nombre de joueur, les pseudos et le mode de jeu.
     """
     # Définition d'une variable de classe pour suivre les tours
     tour_actuel = 1

     def __init__(self, master):
        """
        @brief constructeur de la classe Application

        Ce constructeur définit l'interface de la classe Application avec les zones pour que l'utilisateur entre le nombre de joueur. 
        Mais également elle efface les données du json et dimmensionne la taille de la fenêtre principale 

        @param master : fenêtre princiaple de l'interface
        """
        # Stockage de master dans une varible
        self.master = master

        # Définition d'un nom pour la fenêtre
        master.title("Application")
        
        # Aggrandir la taille de la fenêtre
        taille_ecran(master)
       
       # A chaque nouvel appel la liste des pseudo est réinitialisé ainsi que le mode du jeu
        self.list_pseudos=[]
        self.mode=None

        # Appel de la fonction pour effacer les données du json à chaque appel de la classe Application
        self.effacer_donnee_json()

        # Affichage pour entrer le nombre de joueur
        self.label_nbJoueur = Label(master, text="Entrez le nombre de joueurs \n Veuillez entrer un entier : ")
        self.label_nbJoueur.pack()
        self.frame_nbJoueur = Entry(master, textvariable=int, width=30)
        self.frame_nbJoueur.pack()

        # Validation le choix du nombre de joueur
        self.bouton_valider = Button(master, text="Valider", command=lambda : self.entrer_pseudos())
        self.bouton_valider.pack()
        

     def entrer_pseudos(self):
        """
        @brief Méthode pour la fenêtre pseudo
        Cette méthode gère l'entrée de chaque pseudo.
        Elle récupère et stocke le nombre de joueur dans une variable et vérifie qu'il à entre 1 et 6 joueurs et que ce sont bien des chiffres qui sont saisis.
        Elle affiche les différents mode de jeu et les entrées des pseudos.
        """

        # Récupération du nombre de joueur saisi par l'utilisateur
        self.nb_joueurs = self.frame_nbJoueur.get()

        # Vérification que le nombre entrer est bien un chiffre
        if self.nb_joueurs.isdigit():

            # Convertion en entier
            self.nb_joueurs=int(self.nb_joueurs)

            # Vérification du nombre de joueur
            if 1 <= self.nb_joueurs <= 6:
                self.fenetre_pseudo = Toplevel(self.master)

                # Aggrandir la fenêtre
                taille_ecran(self.fenetre_pseudo)
                self.fenetre_pseudo.title("Pseudo")

                # Utiliser une liste pour stocker les StringVar
                self.liste_values = []
                for _ in range(self.nb_joueurs):

                    # Entrée des pseudos
                    value = StringVar()
                    self.liste_values.append(value)
                
                    self.label_pseudo = Label(self.fenetre_pseudo, text="Entrez le pseudo :")
                    self.label_pseudo.pack()
                    entree = Entry(self.fenetre_pseudo, textvariable=value, width=30)
                    entree.pack()
                
                # Définition du bouton de validation pour les pseudos 
                self.bouton_valider_pseudo = Button(self.fenetre_pseudo, text="Valider",command=self.recupere_pseudos)
                self.bouton_valider_pseudo.pack()
                 
                # Définition des boutons pour les différents modes de jeu
                self.label_instruction = Label(self.fenetre_pseudo, text="\n Choissisez le mode de jeu :")
                self.label_instruction.pack_forget()

                self.bouton_valider_Strict = Button(self.fenetre_pseudo, text="Mode Strict", command=self.recupere_mode_strict)
                self.bouton_valider_Strict.pack_forget()

                self.bouton_valider_Mediane = Button(self.fenetre_pseudo, text="Mode Mediane", command=self.recupere_mode_mediane)
                self.bouton_valider_Mediane.pack_forget()

                self.bouton_valider_Moyenne = Button(self.fenetre_pseudo, text="Mode Moyenne", command=self.recupere_mode_moyenne)
                self.bouton_valider_Moyenne.pack_forget()

                self.bouton_valider_Majorite_Abs = Button(self.fenetre_pseudo, text="Mode Majorité Absolue", command=self.recupere_mode_maj_abs)
                self.bouton_valider_Majorite_Abs.pack_forget()

                self.bouton_valider_Majorite_rel = Button(self.fenetre_pseudo, text="Mode Majorité Relative", command=self.recupere_mode_maj_rel)
                self.bouton_valider_Majorite_rel.pack_forget()

                # Bouton pour recommencer la partie
                self.label_instruction_partie = Label(self.fenetre_pseudo, text="\n Vous vous êtes trompés :")
                self.label_instruction_partie.pack(anchor="center")

                self.bouton_recommencer = Button(self.fenetre_pseudo, text="Recommencer la partie", command=lambda:self.recommencer_partie())
                self.bouton_recommencer.pack(anchor="center")

                # Masque la fenêtre du nombre de joueur
                self.master.withdraw()
                
            else : messagebox.showerror("/!\ Erreur","Il faut entre 1 et 6 joueurs")

        else : 
            messagebox.showerror("/!\ Erreur","Veuillez saisir un nombre entier")
    
     def recupere_mode_strict(self):

        """
        @brief Méthode qui instancie un objet de la classe Strict
        """

        # Cas pour le mode strict
        fenetre_strict=Tk()
        fenetre_strict.title("Mode Strict")

        # Instance de la classe Mode_Strict
        instance_stricte = Mode_Strict(fenetre_strict, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
        fenetre_strict.mainloop()

     def recupere_mode_mediane(self):  
            """
            @brief Méthode qui instancie un objet de la classe Médiane
            """  
            fenetre_mediane=Tk()
            fenetre_mediane.title("Mode Médiane")

            # Instance de la classe Mode_Mediane
            instance_mediane = Mode_Mediane(fenetre_mediane, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
            fenetre_mediane.mainloop()

     def recupere_mode_moyenne(self):  
        """
        @brief Méthode qui instancie un objet de la classe Moyenne
        """  
        fenetre_moyenne=Tk()
        fenetre_moyenne.title("Mode Moyenne")

        # Instance de la classe Mode_Moyenne
        instance_moy = Mode_Moyenne(fenetre_moyenne, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
        fenetre_moyenne.mainloop()
    
     def recupere_mode_maj_abs(self): 
        """
        @brief Méthode qui instancie un objet de la classe Majorité Absolue
        """   
        fenetre_maj_abs=Tk()
        fenetre_maj_abs.title("Mode Majorité Absolue")

        # Instance de la classe Mode_Majorite_Absolue
        instance_maj_abs = Mode_Majorite_Absolue(fenetre_maj_abs, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
        fenetre_maj_abs.mainloop()
    
     def recupere_mode_maj_rel(self):    
        """
        @brief Méthode qui instancie un objet de la classe Majorité Relative
        """
        fenetre_maj_rel=Tk()
        fenetre_maj_rel.title("Mode Majorité Relative")

        # Instance de la classe Mode_Majorite_Relative
        instance_maj_rel = Mode_Majorite_Relative(fenetre_maj_rel, self.list_pseudos,self.nb_joueurs,self.fenetre_pseudo)
        fenetre_maj_rel.mainloop()


     def recupere_pseudos(self):
        """
        @brief Méthode qui récupère les pseudos
        Les pseudos sont stockées dans une liste.
        Cette méthode gère l'appairiton des boutons du mode de je
        """

        # Récupérer les pseudos à partir de la liste des StringVar
        pseudos = [value.get() for value in self.liste_values]

        # Stocker les pseudos dans list_pseudo
        self.list_pseudos.extend(pseudos)

        self.fenetre_pseudo = self.bouton_valider.winfo_toplevel()
        self.bouton_recommencer = Button(self.master, text="Recommencer", command=lambda:self.recommencer_partie())
        self.bouton_recommencer.pack()

        # Passage du bouton en vert pour montrer qu'il a été validé
        self.bouton_valider_pseudo.configure(bg="#82977e", fg="white")

        # Apparition des boutons pour le choix du mode
        self.label_instruction.pack()
        self.bouton_valider_Strict.pack()
        self.bouton_valider_Mediane.pack()
        self.bouton_valider_Moyenne.pack()
        self.bouton_valider_Majorite_Abs.pack()
        self.bouton_valider_Majorite_rel.pack()

     def recommencer_partie(self):
        """
        @brief Méthode pour recommencer une partie
        Pour recommencer une partie une nouvelle fenêtre un nouvel objet de la classe Application est instancié.
        """

        # Destruction de la fenêtre actuelle
        self.master.destroy()

        # Lancement d'une nouvelle fenêtre pour recommencer la partie
        fenetre=Tk()
        app = Application(fenetre)
        fenetre.mainloop()

        # Efface les données du json
        self.effacer_donnee_json()

     def effacer_donnee_json(self):
        """
        @brief Méthode pour réinitialiser les données du json
        """

        # Effacer les données du fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump({"tableau": []}, fichier_json, indent=4)


class Mode_Strict(Application):
    """
    @ class Mode_Strict
    @brief Classe qui définit les conditions du mode de jeu strict
    Cette classe hérite de la classe Application

    """
    def __init__(self, master, pseudo, nb, fenetre) :
        """
        @brief Constructeur de la classe Strict
        Il gère l'affichage de l'interface du mode strict.

        @param master (tk.Tk) : fenêtre principale pour le mode strict
        @param pseudo (list) : liste des pseudos provenant de la classe Application
        @param nb (int) : nombre de joueur récupérer grâce à la classe mère
        @param fenetre (Tk) : la fenêtre définit pour la classe Application
        """
        self.master = master
        taille_ecran(master)
        master.title("Mode Strict")        

        # Stocker les pseudos et le nombre de joueur
        self.pseudo=pseudo
        self.nb=int(nb)

        # Pour stocker les estimations
        self.estimation=[]

        # Variable pour connaître l'affichage de la partie
        self.indice_rec=0
        
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
        self.bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:self.sauvegarder_donnees())

        # Création d'un bouton pour entrer une tâche
        self.bouton_tache=Button(master, text="Tâche suivante", command=lambda:self.tache_suivante())

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:self.recommencer_partie_mode())

        # Création d'un bouton pour afficher les données du json
        self.bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:self.afficher_donnees_json())

        # Bouton pour mettre fin à la partie
        self.bouton_fin_de_partie = Button(master, text="Fin de la partie", command=lambda :self.fin_de_partie(fenetre))

        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid()
        self.entree_description.grid()

        self.bouton_sauvegarder.grid()

        self.bouton_tache.grid_forget()

        self.bouton_recommencer.grid()

        self.bouton_afficher_json.grid()

        self.bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        self.liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]
        
    def vote_estimation(self, valeur):
        """
        @brief Méthode pour récupérer le vote de chaque joueur
        Execpté pour la valeur pause, chaque valeur de vote est stocké dans une liste.
        Une fois que le nombre d'élément de la liste est équivalente aux nombres de joueurs. La fonction sauvegarder_estimation est appelée
        @param valeur : la valeur de l'estimation du joueur
        """
        # Traitement de la valeur pause
        if valeur =="Pause":
            self.pause()
        else : 
            
            # Stockage des informations dans la liste estimation
            self.estimation.append(valeur)

            if len(self.estimation)==self.nb:
                self.sauvegarder_estimation()
                
    def verif_regle(self):
        """
        @brief Méthode pour vérfier que la règle du mode strict est bien respectée
        Si la règle est respectée la valeur est enregistrée dans le json sinon les joueurs doivent voter denouveau
        @return : Un booléan indiquant si la règle est respectée
        """
        # Initiation d'une variable pour connaître le statut de la fonction
        indice=False

        # Suppression des doublons
        self.estimation_final = set(self.estimation)

        # Vérification de la longueur de la liste soit égale à 1
        if len(self.estimation_final)==1:
            print(self.estimation_final, len(self.estimation_final))
            indice=True
        else:
            messagebox.showinfo("Attention","La règle stricte n'est pas respectée. \n Veuillez recommencez")

            # Passage de la liste des estimations à vides pour recommencer
            self.estimation=[]

        return indice

    def sauvegarder_estimation(self):
        """
        @brief Méthode pour enregistrer l'estimation dans le fichier JSON
        Lorsque l'enregistrement est terminé, le bouton tâche suivante s'active
        """    
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
                
                # Activer le clignotement du bouton tache suivante
                self.clignoter(True)
    
    def clignoter(self, statut):
        """
        @brief Méthode pour définir le clignotement du bouton tache suivante
        @param statut : booléan qui inique si le clignotement soit s'arrêter ou commencer

        """
        # Affectation de statut dans une variable
        etat_clignotement=statut

        # Extraction de la couleur du bouton tache suivante
        couleur = self.bouton_tache.cget("bg")
        
        # Changement de la couleur du bouton tache suivante
        if couleur == "#ececec":
            self.bouton_tache.configure(bg="#82977e", fg="white")
        else:
            self.bouton_tache.configure(bg="#ececec", fg="black")
        
        # Appel récursif de la fonction
        if etat_clignotement==True:            
            self.clignotement_id = self.master.after(500, self.clignoter,True)
        else:
            # Annulation de l'appel récurrent de la fonction clignoter
            self.master.after_cancel(self.clignotement_id)
            self.bouton_tache.configure(bg="#ececec", fg="black")

                
    def creer_fichier_json(self):
            """
            @brief Méthode pour créer le fichier json
            Si le fichier JSON n'existe pas il est crée avec un tableau vide dedans
            """
            chemin_fichier = "donnees.json"
            if not os.path.exists(chemin_fichier):
                with open(chemin_fichier, "w") as fichier_json:
                    json.dump({"tableau": []}, fichier_json, indent=4)

    def sauvegarder_donnees(self):
        """
        @brief Méthode pour sauvegarder les informations du backlog saisies par l'utilisateur.
        L'utilisateur entre un numéro, un nom et une description pour chaque tâche de son backlog.
        Ensuite les informations sont enregistrées dans le tableau du JSON
        """

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

        # Changement de couleur pour le bouton sauvegarder
        self.bouton_sauvegarder.configure(bg="#82977e", fg="white")

        # Définition des boutons de vote
        self.appel_bouton()

        # Apparition de bouton tâche suivante
        self.bouton_tache.grid()
    
    def appel_bouton(self):
        """
        @brief Méthode pour créer les boutons de vote
        Une fois créer les boutons sont stockées dans une liste
        """

        # Définition des boutons de vote
        self.boutons_vote = []
        for j, k in enumerate(self.pseudo):
            for i, value in enumerate(self.liste_valeur):
                # Affichage des pseudos
                label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                label_pseudo.grid(row=0, column=10 + j + 10)

                # Affichage des boutons
                button_vote = Button(self.master, text=value, command=lambda v=value: self.vote_estimation(v))
                button_vote.grid(row=i + 1, column=10 + j + 10)
                self.boutons_vote.append(button_vote)
        
    def recommencer_partie_mode(self):

        """
        @brief Méthode pour recommencer une partie
        La fonctione recommencer partie de la classe mère est appelée mais en plus la fonction tache suivante de cette classe est appelée
        """

        # Initialisation d'une variable pour connaître le statut de la partie
        self.indice_rec=1

        # Appel de la fonction tache_suivante pour réinitisaliser les paramètres de l'interface
        self.tache_suivante()
        
        # Utilsiation de la fonction recommencer_partie de la classe mère
        Application.recommencer_partie(self)
        self.master.destroy()
          
    def fin_de_partie(self, fenetre_app):
        """
        @brief Méthode pour mettre fin à la partie
        @param fenetre_app : Pour détruire les fenêtres ouvertes avec la classe Application
        """

        # Affichage d'un message d'au revoir
        messagebox.showinfo("Fin de partie","A bientôt !")

        # Ferme la fenêtre
        self.master.destroy()
        fenetre_app.destroy()
    
    def tache_suivante(self):
        """
        @brief Méthode pour la gestion du bouton de la tâche suivante
        Les zones de saisies pour entrer le numéro, nom et description du backlog sont réinitialisées
        La fonction clignoter est désactiver et le bouton tâche suivante disparaît
        """
        self.entree_num.delete(0, tk.END)
        self.entree_nom.delete(0, tk.END)
        self.entree_description.delete(0, tk.END)
        self.estimation=[]

        if self.indice_rec!=1:    
            
            # Disparition du bouton tâche suivante
            self.bouton_tache.grid_forget()

            # Passage du bouton sauvegarder en couleur classique
            self.bouton_sauvegarder.configure(bg="#ececec", fg="black")

            # Dispairiton des boutons de vote
            for i in self.boutons_vote:
                i.grid_forget()
        
            # Désactiver le clignotement du bouton tache suivante
            self.clignoter(False)
        else: 
             pass

        # Incrémentation de la variable tour_actuel
        Application.tour_actuel+=1
        print(Application.tour_actuel)
    
    def afficher_donnees_json(self):
        """
        @brief Méthode pour visaliser les données du JSON
        Elle montre le numéro, le nom, la description et l'estimation pour chaque tâche en créant une zone de texte
        A chaque clique sur le bouton les informations de la zone de texte sont effacées
        """

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
        """
        @brief Méthode pour gérer le bouton Pause
        Un message est affiché pour montrer que le jeu est en pause
        """
        messagebox.showinfo("Pause","Vous êtes en pause. \n Cliquez sur OK pour reprendre la partie")

class Mode_Moyenne(Mode_Strict):
    """
    @class Mode_Moyenne
    @brief Classe qui définit les règles du mode de jeu moyenne. Cette classe hérite de la classe Mode_Strict
    """
    def __init__(self, master, pseudo, nb, fenetre) :
        """
        @brief Constructeur de la classe Mode_Moyenne
        Il gère l'affichage de l'interface du mode moyenne.

        @param master (tk.Tk) : fenêtre principale pour le mode strict
        @param pseudo (list) : liste des pseudos provenant de la classe Application
        @param nb (int) : nombre de joueur récupérer grâce à la classe mère
        @param fenetre (Tk) : la fenêtre définit pour la classe Application
        """
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Moyenne")        

        # Pour stocker les estimations
        self.estimation=[]

        # Pour stocker les pseudos
        self.pseudo=pseudo

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Variable pour connaître l'affichage de la partie
        self.indice_rec=0


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
        self.bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        self.bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        self.bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        self.bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        self.bouton_sauvegarder.grid()

        self.bouton_tache.grid_forget()

        self.bouton_recommencer.grid()

        self.bouton_afficher_json.grid()

        self.bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        self.liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]

    def vote_estimation_moyenne(self, valeur):
        """
        @brief Méthode pour stocker la valeur votée par les joueurs
        Chaque valeur est ajoutée à la liste des estimations si elle n'est pas égale à Pause ou Ne Sais Pas
        Si le nombre d'élément de la liste est égale au nombre de joueur alors on sauvegrader l'estimation dans le json
        @param valeur : valeur votée par un joueur
        """
        # Gestion de la valeur pause
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
        """
        @brief Méthode pour calculer la moyenne des estimations
        @return : la moyenne des estimations
        """

        if len(self.estimation)==self.nb:
                moyenne=statistics.mean(self.estimation)
                print(moyenne)

        return moyenne

    def sauvegarder_estimation_moyenne(self):  
            """
            @brief Sauvegarder de la moyenne dans le fichier JSON
            Activation de la fonction clignoter pour le bouton tache suivant
            """  

            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_moyenne()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

                # Sauvegarder les données mises à jour dans le fichier JSON
                with open("donnees.json", "w") as fichier_json:
                    json.dump(donnees_existantes, fichier_json, indent=4)
                messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

                # Activation de la fonction clignoter
                self.clignoter(True)

    def appel_bouton(self):
        """
        @brief Méthode pour créer les boutons de vote
        La méthode lance la fonction vote_estimation_moyenne
        """

        # Définition des boutons de vote
        self.boutons_vote = []
        for j, k in enumerate(self.pseudo):
            for i, value in enumerate(self.liste_valeur):
                # Affichage des pseudos
                label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                label_pseudo.grid(row=0, column=10 + j + 10)
                
                # Affichage des boutons de vote
                button_vote = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_moyenne(v))
                button_vote.grid(row=i + 1, column=10 + j + 10)
                self.boutons_vote.append(button_vote)

class Mode_Mediane(Mode_Strict):
    """
    @class Mode_Mediane
    @brief Cette classe définit les règles et l'interface du mode médiane
    Elle hérite de Mode_Strict
    """
    def __init__(self, master, pseudo, nb, fenetre) :
        """
        @brief Constructeur de la classe Mode_Mediane
        Il gère l'affichage de l'interface du mode médiane.

        @param master (tk.Tk) : fenêtre principale pour le mode strict
        @param pseudo (list) : liste des pseudos provenant de la classe Application
        @param nb (int) : nombre de joueur récupérer grâce à la classe mère
        @param fenetre (Tk) : la fenêtre définit pour la classe Application
        """
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Médiane")        

        # Pour stocker les estimations
        self.estimation=[]            

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Stockage des pseudos dans une variable
        self.pseudo=pseudo

        # Variable pour connaître l'affichage de la partie
        self.indice_rec=0

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
        self.bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        self.bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        self.bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        self.bouton_fin_de_partie = Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        self.bouton_sauvegarder.grid()

        self.bouton_tache.grid_forget()

        self.bouton_recommencer.grid()

        self.bouton_afficher_json.grid()

        self.bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        self.liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]        
        
    def vote_estimation_mediane(self, valeur):
        """
        @brief Méthode pour stocker la valeur votée par les joueurs
        Chaque valeur est ajoutée à la liste des estimations si elle n'est pas égale à Pause ou Ne Sais Pas
        Si le nombre d'élément de la liste est égale au nombre de joueur alors on sauvegrader l'estimation dans le json
        @param valeur : valeur votée par un joueur
        """

       
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
        """
        @brief Méthode pour calculer la médiane des estimations
        @return : la médiane des estimations
        """

        if len(self.estimation)==self.nb:
                moyenne=statistics.median(self.estimation)
                print(moyenne)

        return moyenne

    def sauvegarder_estimation_mediane(self): 
            """
            @brief Sauvegarder de la médiane dans le fichier JSON
            Activation de la fonction clignoter pour le bouton tache suivant
            """   

            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_mediane()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

                # Sauvegarder les données mises à jour dans le fichier JSON
                with open("donnees.json", "w") as fichier_json:
                    json.dump(donnees_existantes, fichier_json, indent=4)
                messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

                # Activation de la fonction clignoter
                self.clignoter(True)

    def appel_bouton(self):
            """
            @brief Méthode pour créer les boutons de vote
            La méthode lance la fonction vote_estimation_mediane
            """

            # Définition des boutons de vote
            self.boutons_vote = []
            for j, k in enumerate(self.pseudo):
                for i, value in enumerate(self.liste_valeur):
                    label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                    label_pseudo.grid(row=0, column=10 + j + 10)
                    button_vote = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_mediane(v))
                    button_vote.grid(row=i + 1, column=10 + j + 10)
                    self.boutons_vote.append(button_vote)

class Mode_Majorite_Absolue(Mode_Strict):
    """
    @class Mode_Majorite_Absolue
    @brief Cette classe définit les règles et l'interface du mode majorite absolue
    Elle hérite de Mode_Strict 
    """
    def __init__(self, master, pseudo, nb, fenetre) :
        """
        @brief Constructeur de la classe mode_majorite_absolue
        Il gère l'affichage de l'interface du mode strict.

        @param master (tk.Tk) : fenêtre principale pour le mode strict
        @param pseudo (list) : liste des pseudos provenant de la classe Application
        @param nb (int) : nombre de joueur récupérer grâce à la classe mère
        @param fenetre (Tk) : la fenêtre définit pour la classe Application
        """
        
        self.master = master
        taille_ecran(master)
        master.title("Mode majorité absolue")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur dans une variable
        self.nb=int(nb)

        # Variable pour connaître l'affichage de la partie
        self.indice_rec=0

        # Pour stocker les pseudos
        self.pseudo=pseudo

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
        self.bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        self.bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        self.bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        self.bouton_fin_de_partie = tk.Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        self.bouton_sauvegarder.grid()

        self.bouton_tache.grid_forget()

        self.bouton_recommencer.grid()

        self.bouton_afficher_json.grid()

        self.bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        self.liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]


    def vote_estimation_majorite_abs(self, valeur):
        """
        @brief Méthode pour stocker la valeur voter par les joueurs
        Chaque valeur est ajoutée à la liste des estimations si elle n'est pas égale à Pause ou Ne Sais Pas
        Si le nombre d'élément de la liste est égale au nombre de joueur alors on sauvegrader l'estimation dans le json
        @param valeur : valeur votée par un joueur
        """
       
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
                self.sauvegarder_estimation_majorite_abs()

    def calcul_majorite_abs(self):
        """
        @brief Méthode pour calculer la majorite absolue des estimations
        @return : la majorite absolue des estimations
        """
        if len(self.estimation) == self.nb:

            # Comptage de chaque occurrences de chaque estimation
            compteur_estimations = Counter(self.estimation)

            # Valeur qui apparaît le plus fréquemment
            majorite_absolue = compteur_estimations.most_common(1)[0][0]

        return majorite_absolue

    def sauvegarder_estimation_majorite_abs(self):
            """
            @brief Sauvegarder de la valeur de la majorite absolue dans le fichier JSON
            Activation de la fonction clignoter pour le bouton tache suivant
            """
            
            # Charger les données existantes depuis le fichier JSON
            with open("donnees.json", "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)

                nouvelle_donnee = {"estimation": self.calcul_majorite_abs()}
                donnees_existantes["tableau"].append(nouvelle_donnee)

            # Sauvegarder les données mises à jour dans le fichier JSON
            with open("donnees.json", "w") as fichier_json:
                json.dump(donnees_existantes, fichier_json, indent=4)

            messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

            # Activation fonction clignotement
            self.clignoter(True)

    def appel_bouton(self):
        """
        @brief Méthode pour créer les boutons de vote
        La méthode lance la fonction vote_estimation_moyenne
        """

        # Définition des boutons de vote
        self.boutons_vote = []
        for j, k in enumerate(self.pseudo):
            for i, value in enumerate(self.liste_valeur):
                # Affichage des pseudos
                label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                label_pseudo.grid(row=0, column=10 + j + 10)

                # Affichage des boutons de vote
                button_vote = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_majorite_abs(v))
                button_vote.grid(row=i + 1, column=10 + j + 10)
                self.boutons_vote.append(button_vote)

class Mode_Majorite_Relative(Mode_Strict):
    """
    @class Mode_Majorite_Relative
    @brief Cette classe définit les règles et l'interface du mode majorite relative
    Elle hérite de Mode_Strict
    """
    def __init__(self, master, pseudo, nb, fenetre):
        """
        @brief Constructeur de la classe Mode_Majorite_Relative
        Il gère l'affichage de l'interface.

        @param master (tk.Tk) : fenêtre principale pour le mode strict
        @param pseudo (list) : liste des pseudos provenant de la classe Application
        @param nb (int) : nombre de joueur récupérer grâce à la classe mère
        @param fenetre (Tk) : la fenêtre définit pour la classe Application
        """
        
        self.master = master
        taille_ecran(master)
        master.title("Mode Majorité Relative")        

        # Pour stocker les estimations
        self.estimation=[]

        # Stockage du nombre de joueur et des pseudos dans une variable
        self.nb=int(nb)
        self.pseudo=pseudo

        # Variable pour connaître l'affichage de la partie
        self.indice_rec=0        

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
        self. bouton_sauvegarder = Button(master, text="Sauvegarder", command=lambda:Mode_Strict.sauvegarder_donnees(self))

        # Création d'un bouton pour entrer une tâche
        self.bouton_tache=Button(master, text="Tâche suivante", command=lambda:Mode_Strict.tache_suivante(self))

        # Création d'un bouton pour recommencer la partie
        self.bouton_recommencer = Button(master, text="Recommencer la partie", command=lambda:Mode_Strict.recommencer_partie_mode(self))

        # Création d'un bouton pour afficher les données du json
        self.bouton_afficher_json = Button(master, text="Afficher les données", command=lambda:Mode_Strict.afficher_donnees_json(self))

        # Bouton pour mettre fin à la partie
        self.bouton_fin_de_partie = Button(master, text="Fin de la partie", command=lambda :Mode_Strict.fin_de_partie(self, fenetre))


        # Placement des étiquettes, zones de texte et bouton dans la fenêtre
        self.label_num.grid()
        self.entree_num.grid()

        self.label_nom.grid()
        self.entree_nom.grid()

        self.label_description.grid
        self.entree_description.grid

        self.bouton_sauvegarder.grid()

        self.bouton_tache.grid_forget()

        self.bouton_recommencer.grid()

        self.bouton_afficher_json.grid()

        self.bouton_fin_de_partie.grid()

        # Définition de la liste contenant les valeurs des boutons
        self.liste_valeur=[0,1,2,3,5,8,13,20,40,100,"Ne Sais Pas", "Pause"]
        

    def vote_estimation_majorite_rel(self, valeur):
        """
        @brief Méthode pour stocker la valeur voter par les joueurs
        Chaque valeur est ajoutée à la liste des estimations si elle n'est pas égale à Pause ou Ne Sais Pas
        Si le nombre d'élément de la liste est égale au nombre de joueur alors on sauvegrader l'estimation dans le json
        @param valeur : valeur votée par un joueur
        """
       
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
                self.sauvegarder_estimation_majorite_rel()
        

    def calcul_majorite_rel(self):
        """
        @brief Méthode pour calculer la majorite relative des estimations
        @return : la majorite relative des estimations
        """

        if len(self.estimation)==self.nb: # Compteur des estimations
            compteur_estimations = Counter(self.estimation)

            # Les éléments sont triées par ordre décroissantes
            estimations_triees = sorted(compteur_estimations.items(), key=lambda x: x[1], reverse=True)

            # Stockage de la valeur la plus fréquente
            valeur_majoritaire = estimations_triees[0]

        return valeur_majoritaire
    
    def sauvegarder_estimation_majorite_rel(self):
        """
        @brief Sauvegarder de la majorite relative dans le fichier JSON
        Activation de la fonction clignoter pour le bouton tache suivant
        """
        # Charger les données existantes depuis le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees_existantes = json.load(fichier_json)

        nouvelle_donnee = {"estimation": self.calcul_majorite_rel()}
        donnees_existantes["tableau"].append(nouvelle_donnee)

        # Sauvegarder les données mises à jour dans le fichier JSON
        with open("donnees.json", "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)
        
        messagebox.showinfo("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

        # Activation clignotement bouton tache
        self.clignoter(True)

    def appel_bouton(self):
        """
        @brief Méthode pour créer les boutons de vote
        La méthode lance la fonction vote_estimation_majorite_relative
        """

        # Définition des boutons de vote
        self.boutons_vote = []
        for j, k in enumerate(self.pseudo):
            for i, value in enumerate(self.liste_valeur):
                # Affichage des pseudos
                label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                label_pseudo.grid(row=0, column=10 + j + 10)

                # Affichage des boutons de vote
                button_vote = Button(self.master, text=value, command=lambda v=value: self.vote_estimation_majorite_rel(v))
                button_vote.grid(row=i + 1, column=10 + j + 10)
                self.boutons_vote.append(button_vote)

# Lancement du programme avex l'instanciation d'un objet de la classe Application
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
