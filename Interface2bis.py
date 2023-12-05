from tkinter import Tk, Entry, Button, Label

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
    root = Tk()
    app = BlocNotes(root)
    root.mainloop()
