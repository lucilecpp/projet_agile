from tkinter import Tk, Listbox, StringVar, Button, Entry, Label, Toplevel


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

        #valider les choix
        self.bouton_valider = Button(master, text="Valider", command=self.entrer_pseudos)
        self.bouton_valider.pack()

        # aggrandir la taille de la fenetre
        master.geometry("800x600")

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
        fenetre_pseudo.geometry("800x600")

    def recupere_partie1(self):
        # Récupérer ici le mode de jeu sélectionné
        self.mode_jeu = self.frame_mode_jeu.get(self.frame_mode_jeu.curselection())  # Modifier selon votre logique
        print("Mode de jeu:", self.mode_jeu)

    def recupere_partie2(self):
        # Récupérer ici le nombre de joueurs
        self.nb_joueurs = int(self.frame_nbJoueur.get())
        print("Nombre de joueurs:", self.nb_joueurs)

    def recupere_pseudos(self):
        # Récupérer les pseudos à partir de la liste des StringVar
        pseudos = [value.get() for value in self.liste_values]
        print("Pseudos:", pseudos)
        fenetre_pseudo = self.bouton_valider.winfo_toplevel()
        fenetre_pseudo.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
