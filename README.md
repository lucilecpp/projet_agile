# Application de Planning Poker Agile

Ce projet a pour but de mettre en place une application de Planning Poker. C'est un jeu utilisé dans les méthodes agiles pour estimer l'effort nécessaire à la réalisation des tâches. Ce planning poker se joue à 6 joueurs maximum.

## Table des matières

1. [Pré-requis](#pré-requis)
2. [Utilisation](#utilisation)
3. [Tests Unitaires](#tests-unitaires)

## Pré-requis

Avant d'utiliser l'application, il est important d'avoir Python d'installé. Pour le télécharger c'est ici : [python.org](https://www.python.org/downloads/).

Pour que l'application fonctionne correctement, vous devez également installer les bibliothèques Python suivantes :
- tkinter
- os
- json
- ctypes
- collections
- statistics
- PIL
- cairosvg
- unittest

### Commandes d'installation

```bash
pip install tk
pip install json
pip install ctypes
pip install collections
pip install statistics
pip install os
pip install Pillow 
pip install cairosvg
pip install unittest
```
## Utilisation

Le code de ce projet est présent dans le fichier ApplicationPocker.py
Pour lancer l'application, exécutez ce fichier à l'aide de la commande suivante :

```bash
python ApplicationPocker.py
```

### Fonctionnement interface et règles du jeu

Quelques informations sur l'interface et les règles de ce jeu : 
 L'interface s'ouvre sur le nombre de joueur de la partie, puis ensuite saisissez les pseudos et enfin choissisez le mode de jeu souhaitez.

#### Les modes de jeu 

 5 mode de jeu sont disponibles : 
 - Strict : On recommence tant que tous les joueurs n'ont pas mis la même estimation.
 - Moyenne : La moyenne des estimations des joueurs correspond à l'estimation finale.
 - Médiane : La médiane des estimations des joueurs correspond à l'estimation finale.
 - Majorité aboslue : La majorité absolue des estimations des joueurs correspond à l'estimation finale.
 - Majorité relative : La majorité relative des estimations des joueurs correspond à l'estimation finale.

#### Les règles 

 Pour que la partie se déroule correctement il faut suivres les instructions suivantes : 
 - Pour chaque tâche de vôtre backlog entrez un numéro, un nom et une description.  
 - Chaque joueur donne son estimation via les boutons. Une fois vôtre tâche enregistrée passez à la suivante. 
 - Si le bouton recommencer est sélectionné, les informations du json seront perdues.
 - Pour quitter la partie, appuyez sur Fin de la Partie pour quitter l'interface.

Si vous quittez la partie vous pouvez retrouvez votre backlog et les estimations associées dans le fichier JSON : donnees.json
/!\ Mais si vous relancez une partie le fichier JSON est réinitialisé. 

## Les tests unitaires

Les tests unitaires du projet sont présents dans le fichier unittests.py. Vous pouvez les exécuter avec la commande suivante : 

```bash
python unittests.py
```

Voici la liste des fonctions qui sont testées grâce aux tests unitaires : 
- TestApplication :
    - test_entrer_pseudos_valid : tester si lors de la saisie d'un entier, on peut continuer sur l'application
    - test_entrer_pseudos_invalid : tester si lors de la saisie de caractères (hors entiers), l'application s'arrête
    
- TestModeStrict : 
    - test_sauvegarder_donnees : tester si les données entrées sont bien enregistrées dans le JSON
    - test_recommencer_partie_mode : tester si les données sont supprimées quand on clique sur le bouton "recommencer partie"

- TestModeMoyenne :
    - test_vote_estimation_moyenne : tester si l'estimation est récupérée
    - test_calcul_moyenne : tester si la moyenne est calculée correctement
    - test_sauvegarder_estimation_moyenne :  tester si la moyenne est bien enregistrée dans le JSON

- TestModeMediane :
    - test_vote_estimation_mediane : tester si l'estimation est récupérée
    - test_calcul_mediane : tester si la médiane est calculée correctement
    - test_sauvegarder_estimation_mediane : tester si la médiane est bien enregistrée dans le JSON

- TestModeMajoriteAbsolue :
    - test_vote_estimation_majorite_abs : tester si l'estimation est récupérée
    - test_calcul_majorite_abs : tester si la majorité absolue est calculée correctement
    - test_sauvegarder_estimation_majorite_abs : tester si la majorité absolue est bien enregistrée dans le JSON

- TestModeMajoriteRelative :
    - test_vote_estimation_majorite_relative : tester si l'estimation est récupérée
    - test_calcul_majorite_rel : tester si la majorité relative est calculée correctement
    - test_sauvegarder_estimation_majorite_rel : tester si la majorité absolue est bien enregistrée dans le JSON



A vous de jouez maintenant !









