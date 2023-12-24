from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import cairosvg
import os

'''class MaClasse:
    def __init__(self, master):
        self.master = master
        self.liste_valeur = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, "interro", "cafe"]
        self.nb = 3

        # Chemin vers le dossier contenant les fichiers SVG
        self.dossier_cartes = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cartes")

        # Appel de la fonction pour afficher les boutons avec des images
        self.appel_bouton()

    def appel_bouton(self):
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

    def vote_estimation(self, value, nb):
        print(f"Valeur sélectionnée : {value}")
if __name__ == "__main__":
    root = Tk()
    app = MaClasse(root)
    root.mainloop()'''

'''class BlocNotes:
    def __init__(self, master):
        self.master = master
        master.title("Block note")

        self.texte = ""

        # Zone de saisie
        self.entree_texte = Entry(master, width=30)
        self.entree_texte.pack(pady=20)

        # Bouton pour valider le texte
        self.bouton_valider = Button(master, text="Valider", command=self.afficher_texte)
        self.bouton_valider.pack()

        # Label pour afficher le texte validé
        self.label_texte = Label(master, text="")
        self.label_texte.pack(pady=20)

        # Agrandir la fenêtre
        master.geometry("600x500")

    def afficher_texte(self):
        # Récupérer le texte de la zone de saisie
        nouveau_texte = self.entree_texte.get()

        # Ajouter le nouveau texte au texte existant
        self.texte += "\n" + nouveau_texte

        # Afficher le texte dans le label
        self.label_texte.config(text=self.texte)

        # Effacer le texte de la zone de saisie
        self.entree_texte.delete(0, "end")
if __name__ == "__main__":
    root = tk()
    appBlocNotes = BlocNotes(root)
    root.mainloop()'''


'''class MinuterieApp:
    def __init__(self, fenetre, duree):
        self.fenetre = fenetre
        self.fenetre.title("Minuterie")

        self.temps_restant = tk.StringVar()
        self.temps_restant.set(self.format_duree(duree))

        self.label_temps = tk.Label(fenetre, textvariable=self.temps_restant, font=("Helvetica", 48))
        self.label_temps.pack(pady=20)

        self.bouton_demarrer = tk.Button(fenetre, text="Démarrer", command=self.demarrer_minuterie)
        self.bouton_demarrer.pack(pady=10)

        self.bouton_arreter = tk.Button(fenetre, text="Arrêter", command=self.arreter_minuterie, state=tk.DISABLED)
        self.bouton_arreter.pack(pady=10)

        self.duree = duree
        self.temps_restant_sec = duree
        self.minuterie_active = False

    def format_duree(self, secondes):
        minutes, secondes = divmod(secondes, 60)
        return f"{minutes:02}:{secondes:02}"

    def mise_a_jour_temps(self):
        self.temps_restant_sec -= 1
        self.temps_restant.set(self.format_duree(self.temps_restant_sec))

        if self.temps_restant_sec <= 0:
            self.arreter_minuterie()

        if self.minuterie_active:
            self.fenetre.after(1000, self.mise_a_jour_temps)

    def demarrer_minuterie(self):
        self.minuterie_active = True
        self.bouton_demarrer.config(state=tk.DISABLED)
        self.bouton_arreter.config(state=tk.NORMAL)
        self.mise_a_jour_temps()

    def arreter_minuterie(self):
        self.minuterie_active = False
        self.bouton_demarrer.config(state=tk.NORMAL)
        self.bouton_arreter.config(state=tk.DISABLED)
        self.temps_restant_sec = self.duree
        self.temps_restant.set(self.format_duree(self.duree))
if __name__ == "__main__":
    duree_minuterie = 300  # 5 minutes
    fenetre_principale = tk.tk()
    appMinuterie = MinuterieApp(fenetre_principale, duree_minuterie)
    fenetre_principale.mainloop()'''

