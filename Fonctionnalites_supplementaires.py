from tkinter import Tk, Label, Button, ttk
import tkinter as tk
from PIL import Image, ImageTk
import cairosvg
import os

# Classe pour remplacer les boutons de vote par une image
class BoutonImage:
    """
    @class BoutonImage
    @brief Importation des images pour les mettre sous forme de boutons
    """
    def __init__(self, master):
        """
        @brief Constructeur pour afficher les images en tant que bouton
        @param master : fenetre tkinter
        """
        self.master = master
        # Liste des valeurs présentes sur les cartes
        self.liste_valeur = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, "interro", "cafe"]
        
        # Déclaration du nombre de joueurs
        self.nb = 3

        # Chemin vers le dossier contenant les fichiers SVG
        self.dossier_cartes = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cartes")

        # Appel de la fonction pour afficher les boutons avec des images
        self.appel_bouton()

    def appel_bouton(self):
        """
        @brief Méthode pour afficher les boutons sous forme d'image
        Des pseudos et le nombre de joueurs ont été simulé pour recréer les mêmes conditions que la classe Application
        """
        for k in ("pseudo1", "pseudo2", "pseudo3"):
            for i, value in enumerate(self.liste_valeur):
                for j in range(int(self.nb)):

                    # Création du label pour chaque joueur
                    label_pseudo = Label(self.master, text=f"A \n {k} \n de voter")
                    label_pseudo.grid(row=0, column=10 + j + 10)

                    # Convertir le fichier SVG en PNG avec cairosvg
                    if isinstance(value, int):
                        svg_path = os.path.join(self.dossier_cartes, f"cartes_{value}.svg")
                    else:
                        svg_path = os.path.join(self.dossier_cartes, f"cartes_{value.replace(' ', '_')}.svg")
                    png_path = os.path.join(self.dossier_cartes, f"cartes_{value}.png")
                    cairosvg.svg2png(url=svg_path, write_to=png_path)

                    # Convertir l'image PNG en PhotoImage pour l'utiliser dans tkinter
                    tk_image = Image.open(png_path)
                    tk_image = tk_image.resize((50, 50))
                    tk_image = ImageTk.PhotoImage(tk_image)

                    # Création des boutons avec des images
                    button = Button(self.master, image=tk_image, command=lambda v=value: self.vote_estimation(v, int(self.nb)))
                    button.image = tk_image
                    button.grid(row=i + 1, column=10 + j + 10)

    def vote_estimation(self, value,nb):
        """
        @brief Méthode pour afficher la valeur sélectionnée par le joueur
        """
        print(f"Valeur sélectionnée : {value}")

# Instanciation d'un objet pour l'affichage des cartes
'''if __name__ == "__main__":
    root = Tk()
    app = BoutonImage(root)
    root.mainloop()'''


class CompteAReboursApp:
    """
    @class CompteAReboursApp
    @brief Définit un compte à rebours
    Les utilisateurs peuvent choisir la durée du minuteur
    """
    def __init__(self, fenetre):
        """
        @brief Constructeur qui affiche la minuteur
        @param fenetre : fenetre sur laquelle va s'afficher le minuteur
        """
        self.fenetre = fenetre
        self.fenetre.title("Compte à Rebours")

        self.temps_restant = tk.StringVar()

        # Affichage du temps restant sur la fenêtre principale
        self.label_temps = tk.Label(fenetre, textvariable=self.temps_restant, font=("Helvetica", 48))
        self.label_temps.pack(pady=20)

        # Création d'un bouton pour démarrer et arrêter le minuteur
        self.bouton_demarrer_arreter = tk.Button(fenetre, text="Démarrer", command=self.demarrer_arreter_compte_a_rebours)
        self.bouton_demarrer_arreter.pack(pady=10)

        # Initialisation des variables
        self.duree = 0
        self.temps_restant_sec = 0
        self.compte_a_rebours_actif = False

        self.selecteur_minutes = None
        self.selecteur_secondes = None

        # Appel de la méthode selecteur_temps
        self.creer_selecteur_temps()

    def format_duree(self, secondes):
        """
        @brief Méthode pour afficher les secondes selon le format mm:ss
        @param secondes : nombre de secondes
        @return : affichage au format minutes: secondes
        """
        minutes, secondes = divmod(secondes, 60)
        return f"{minutes:02}:{secondes:02}"

    def mise_a_jour_temps(self):
        """
        @brief Méthode pour mettre à jour le temps, afficher du minuteur
        Dès qu'un compte à rebours est actif, cette méthode décrémente le temps de 1 seconde toutes les secondes.
        """
        if self.compte_a_rebours_actif:
            self.temps_restant_sec -= 1
            self.temps_restant.set(self.format_duree(self.temps_restant_sec))

            if self.temps_restant_sec <= 0:
                self.arreter_compte_a_rebours()
            else:
                self.fenetre.after(1000, self.mise_a_jour_temps)

    def demarrer_arreter_compte_a_rebours(self):
        """
        @brief Pour lancer ou stoper le compte à rebours
        """
        if self.compte_a_rebours_actif:
            self.arreter_compte_a_rebours()
        else:
            self.demarrer_compte_a_rebours()

    def demarrer_compte_a_rebours(self):
        """
        @brief Pour démarer le compte à rebours

        """
        self.duree = int(self.selecteur_minutes.get()) * 60 + int(self.selecteur_secondes.get())
        self.temps_restant_sec = self.duree
        self.temps_restant.set(self.format_duree(self.duree))
        self.compte_a_rebours_actif = True
        self.bouton_demarrer_arreter.config(text="Arrêter", bg="red")
        self.mise_a_jour_temps()

    def arreter_compte_a_rebours(self):
        """
        @brief Pour éteindre le compte à rebours
        """
        self.compte_a_rebours_actif = False
        self.bouton_demarrer_arreter.config(text="Démarrer", bg="green")
        self.temps_restant_sec = self.duree
        self.temps_restant.set(self.format_duree(self.duree))

    def creer_selecteur_temps(self):
        """
        @brief Méthode pour permettre de choisir la durée du minuteur
        """
        frame_selecteur = ttk.Frame(self.fenetre)
        frame_selecteur.pack(pady=20)

        label_selecteur = ttk.Label(frame_selecteur, text="Durée du compte à rebours :")
        label_selecteur.grid(row=0, column=0, padx=10)

        # Pour choisir les minutes
        self.selecteur_minutes = ttk.Spinbox(frame_selecteur, from_=0, to=59, wrap=True, width=2)
        self.selecteur_minutes.grid(row=0, column=1, padx=10)

        label_minutes = ttk.Label(frame_selecteur, text="minutes")
        label_minutes.grid(row=0, column=2, padx=10)

        # Pour choisir les secondes
        self.selecteur_secondes = ttk.Spinbox(frame_selecteur, from_=0, to=59, wrap=True, width=2)
        self.selecteur_secondes.grid(row=0, column=3, padx=10)

        label_secondes = ttk.Label(frame_selecteur, text="secondes")
        label_secondes.grid(row=0, column=4, padx=10)

        self.selecteur_minutes.set(0)
        self.selecteur_secondes.set(0)


# Instanciation d'un objet pour le compte à rebours
if __name__ == "__main__":
    fenetre_principale = Tk()
    appCompteARebours = CompteAReboursApp(fenetre_principale)
    fenetre_principale.mainloop()


