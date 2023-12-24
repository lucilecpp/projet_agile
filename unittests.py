import unittest
from unittest.mock import patch
from tkinter import Tk
import json
import os


from ApplicationPocker import Application  
class TestApplication(unittest.TestCase):

    def test_entrer_pseudos_valid(self):
        root = Tk()
        app = Application(root)

        # Appel manuel de la méthode avec une valeur fixe
        app.frame_nbJoueur.insert(0, "4")  # Simule la saisie utilisateur
        app.entrer_pseudos()

        self.assertEqual(app.nb_joueurs, 4)

    def test_entrer_pseudos_invalid(self):
        root = Tk()
        app = Application(root)

        with patch("builtins.input", side_effect=["invalid"]):
            app.entrer_pseudos()


'''    
def effacer_donnees_json(self):
    # Effacer les données dans le fichier JSON s'il n'est pas vide
    if os.path.exists("donnees.json") and os.path.getsize("donnees.json") > 0:
        with open("donnees.json", "w") as fichier_json:
            fichier_json.write("")'''
            
from ApplicationPocker import Mode_Strict
class TestModeStrict(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        # Désactiver la destruction automatique de la fenêtre pendant les tests
        self.root.withdraw()
        self.mode_strict = Mode_Strict(self.root, ["John", "Alice"], 2, self.root)

    def tearDown(self):
        # Détruire la fenêtre seulement si elle existe encore
        if self.root.winfo_exists():
            self.root.destroy()

    @patch("ApplicationPocker.messagebox.showinfo")     # Utilisation du décorateur patch
    def test_sauvegarder_donnees(self, mock_showinfo):
        # Simuler la saisie des données dans les zones de texte
        self.mode_strict.entree_num.insert(0, "1")
        self.mode_strict.entree_nom.insert(0, "Tache1")
        self.mode_strict.entree_description.insert(0, "Description1")

        # Appeler la méthode sauvegarder_donnees
        print("\nTest mode strict :")
        self.mode_strict.sauvegarder_donnees()

        # Vérifier que les données sont correctement sauvegardées dans le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees = json.load(fichier_json)
            derniere_donnee = donnees["tableau"][-1]
            self.assertEqual(derniere_donnee["numero_tache"], "1")
            self.assertEqual(derniere_donnee["nom_tache"], "Tache1")
            self.assertEqual(derniere_donnee["description_tache"], "Description1")
        
       # Vérifier que la boîte d'information est appelée
        mock_showinfo.assert_called_once_with("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

    def test_recommencer_partie_mode(self):
        # Appeler la méthode recommencer_partie_mode
        self.mode_strict.recommencer_partie_mode()

        # Vérifier que les champs de saisie et la liste d'estimation sont réinitialisés
        self.assertEqual(self.mode_strict.entree_num.get(), "")
        self.assertEqual(self.mode_strict.entree_nom.get(), "")
        self.assertEqual(self.mode_strict.entree_description.get(), "")
        self.assertEqual(self.mode_strict.estimation, [])

from ApplicationPocker import Mode_Moyenne  
class TestModeMoyenne(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        # Désactiver la destruction automatique de la fenêtre pendant les tests
        self.root.withdraw()
        self.mode_moyenne = Mode_Moyenne(self.root, ["John", "Alice", "Margot"], 3, self.root)
        self.mode_moyenne.estimation = [5, 8, 13]

    def tearDown(self):
        # Détruire la fenêtre seulement si elle existe encore
        if self.root.winfo_exists():
            self.root.destroy()

    def test_vote_estimation_moyenne(self):
        # Simuler le vote avec une valeur
        self.mode_moyenne.vote_estimation_moyenne(8)

        # Vérifier que la valeur a été ajoutée à la liste d'estimation
        self.assertEqual(self.mode_moyenne.estimation, [5, 8, 13, 8])

    def test_calcul_moyenne(self):
        print("\nTest estimation moyenne :")

        # Appeler la méthode de calcul de moyenne
        moyenne = self.mode_moyenne.calcul_moyenne()
        
        # Assurer que la moyenne est calculée correctement
        self.assertEqual(moyenne, 8.666666666666666)

    @patch("ApplicationPocker.messagebox.showinfo")     # Utilisation du décorateur patch
    def test_sauvegarder_estimation_moyenne(self, mock_showinfo):
        # Appeler la méthode sauvegarder_estimation_moyenne
        self.mode_moyenne.sauvegarder_estimation_moyenne()
        
        # Vérifier que la boîte d'information est appelée
        mock_showinfo.assert_called_once_with("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

from ApplicationPocker import Mode_Mediane
class TestModeMediane(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        # Désactiver la destruction automatique de la fenêtre pendant les tests
        self.root.withdraw()
        self.mode_mediane = Mode_Mediane(self.root, ["John", "Alice", "Margot"], 3, self.root)
        self.mode_mediane.estimation = [5, 8, 13]

    def tearDown(self):
        # Détruire la fenêtre seulement si elle existe encore
        if self.root.winfo_exists():
            self.root.destroy()

    def test_vote_estimation_mediane(self):
        # Simuler le vote
        self.mode_mediane.vote_estimation_mediane(8)

        # Vérifier que la valeur a été ajoutée à la liste d'estimation
        self.assertEqual(self.mode_mediane.estimation, [5, 8, 13, 8])

    def test_calcul_mediane(self):
        print("\nTest estimation mediane :")
        # Appeler la méthode de calcul de moyenne
        mediane = self.mode_mediane.calcul_mediane()
        
        # Assurer que la mediane est calculée correctement
        self.assertEqual(mediane, 8)


    @patch('ApplicationPocker.messagebox.showinfo')     # Utilisation du décorateur patch
    def test_sauvegarder_estimation_mediane(self, mock_showinfo):
        # Appeler la méthode sauvegarder_estimation_mediane
        self.mode_mediane.sauvegarder_estimation_mediane()
        
        # Vérifier que le message d'information est affiché
        mock_showinfo.assert_called_once_with("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

from ApplicationPocker import Mode_Majorite_Absolue
class TestModeMajoriteAbsolue(unittest.TestCase):
    def setUp(self):
        self.root = Tk()

        # Désactiver la destruction automatique de la fenêtre pendant les tests
        self.root.withdraw()
        self.mode_majorite_absolue = Mode_Majorite_Absolue(self.root, ["John", "Alice"], 2, self.root)
        self.mode_majorite_absolue.estimation = [5, 8]

    def tearDown(self):
        # Détruire la fenêtre seulement si elle existe encore
        if self.root.winfo_exists():
            self.root.destroy()

    def test_vote_estimation_majorite_abs(self):
        # Simuler le vote
        self.mode_majorite_absolue.vote_estimation_majorite_abs(5)

        # Vérifier que la valeur a été ajoutée à la liste d'estimation
        self.assertEqual(self.mode_majorite_absolue.estimation, [5, 8, 5])


    def test_calcul_majorite_abs(self):
        print("\nTest estimation majorite absolue :")
        # Appeler la méthode de calcul de moyenne
        majoriteAbs = self.mode_majorite_absolue.calcul_majorite_abs()
       
        # Assurer que la moyenne est calculée correctement
        self.assertEqual(majoriteAbs, 5)

    @patch('ApplicationPocker.messagebox.showinfo')     # Utilisation du décorateur patch
    def test_sauvegarder_estimation_majorite_abs(self, mock_showinfo):
        # Appeler la méthode sauvegarder_estimation_majorite_abs
        self.mode_majorite_absolue.sauvegarder_estimation_majorite_abs()
        
        # Vérifier que le message d'information est affiché
        mock_showinfo.assert_called_once_with("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

from ApplicationPocker import Mode_Majorite_Relative
class TestModeMajoriteRelative(unittest.TestCase):  
    def setUp(self):
        self.root = Tk()
        
        # Désactivez la destruction automatique de la fenêtre pendant les tests
        self.root.withdraw()
        self.mode_majorite_relative = Mode_Majorite_Relative(self.root, ["John", "Alice", "Margot", "Maxime", "Lucas", "Laura", "Nathan", "Alexandra"], 8, self.root)
        
        # Simuler des données dans la liste d'estimations
        self.mode_majorite_relative.estimation = [1, 2, 3, 1, 2, 3, 1, 1]

    def tearDown(self):
        # Détruire la fenêtre seulement si elle existe encore
        if self.root.winfo_exists():
            self.root.destroy()

    def test_vote_estimation_majorite_relative(self):
            # Simuler le vote
            self.mode_majorite_relative.vote_estimation_majorite_rel(5)

            # Vérifier que la valeur a été ajoutée à la liste d'estimation
            self.assertEqual(self.mode_majorite_relative.estimation, [1, 2, 3, 1, 2, 3, 1, 1, 5])

    def test_calcul_majorite_rel(self):
        print("\nTest estimation majorite relative :")

        # Testez la méthode calcul_majorite_rel avec une liste d'estimations
        result = self.mode_majorite_relative.calcul_majorite_rel()
        self.assertEqual(result, (1, 4))  

    @patch('ApplicationPocker.messagebox.showinfo')     # Utilisation du décorateur patch
    def test_sauvegarder_estimation_majorite_rel(self, mock_showinfo):
        # Appeler la méthode sauvegarder_estimation_majorite_rel
        self.mode_majorite_relative.sauvegarder_estimation_majorite_rel()

        # Vérifier que showinfo a été appelé
        mock_showinfo.assert_called_once_with("Mission réussie", "L'estimation est bien enregistrée \n Veuillez cliquer sur tâche suivante \n pour passer à la suite")

        # Vérifier que les données sont correctement sauvegardées dans le fichier JSON
        with open("donnees.json", "r") as fichier_json:
            donnees = json.load(fichier_json)
            derniere_donnee = donnees["tableau"][-1]["estimation_majorite_rel"]
            self.assertEqual(derniere_donnee, [1, 4])  

if __name__ == "__main__":
    unittest.main()
