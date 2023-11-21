from tkinter import Tk, Listbox, Radiobutton, StringVar, Button, Entry, messagebox
import pandas as pd
import string

def fermer_fenetre(fenetre):
    fenetre.destroy()

# Définission du choix local ou distance

# Définission du choix local ou distance
fenetre_LD = Tk()
# Utilisez une chaîne arbitraire pour le bouton fictif (invisible et désactivé)
value = StringVar(value="AucunChoix") 
local = Radiobutton(fenetre_LD, text="Local", variable=value, value="Local")
distance = Radiobutton(fenetre_LD, text="Distance", variable=value, value="Distance")
# Bouton fictif invisible et désactivé
aucun_choix = Radiobutton(fenetre_LD, text="", variable=value, value="AucunChoix", state="disabled")
aucun_choix.pack_forget()  # Cacher le bouton 
local.pack()
distance.pack()
bouton_valider = Button(fenetre_LD, text="Valider", command=lambda: fermer_fenetre(fenetre_LD))
bouton_valider.pack()
fenetre_LD.mainloop()

'''
# Définition de la liste avec le choix du mode de jeu
fenetre_mode = Tk()
liste = Listbox(fenetre_mode)
liste.insert(1, "Strict")
liste.insert(2, "Médiane")
liste.insert(3, "Moyenne")
liste.insert(4, "Majorité absolue")
liste.insert(5, "Majorité relative")
liste.pack()

bouton_valider_mode = Button(fenetre_mode, text="Valider", command=lambda: fermer_fenetre(fenetre_mode))
bouton_valider_mode.pack()
fenetre_mode.mainloop()

# Nombre de joueur
def recupere():
    messagebox.showinfo("Alerte", entree.get())
  

fenetre_nb_joueur = Tk()
value = StringVar() 
value.set("nombre de joueurs")
entree = Entry(fenetre_nb_joueur, textvariable=value, width=30) 
entree.pack()

bouton_valider_joueur = Button(fenetre_nb_joueur, text="Valider", command=recupere)
bouton_valider_joueur.pack()

# Fermer la fenêtre précédente (fenetre_mode) lorsque celle-ci est ouverte
#bouton_valider_joueur.config(command=lambda: [fermer_fenetre(fenetre_mode), fermer_fenetre(fenetre_nb_joueur)])
fenetre_nb_joueur.mainloop()
'''
'''
# Entrée des pseudos
fenetre_pseudo = Tk()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre_pseudo, textvariable=string, width=30)
entree.pack()

bouton_valider_pseudo = Button(fenetre_pseudo, text="Valider", command=lambda: fermer_fenetre(fenetre_pseudo))
bouton_valider_pseudo.pack()
fenetre_pseudo.mainloop()'''
