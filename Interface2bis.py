from tkinter import tk, Entry, Button, Label

class BlocNotes:
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
    app = BlocNotes(root)
    root.mainloop()


class MinuterieApp:
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
    app = MinuterieApp(fenetre_principale, duree_minuterie)
    fenetre_principale.mainloop()
