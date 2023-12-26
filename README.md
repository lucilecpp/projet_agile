# Application de Planning Poker Agile

Ce projet a pour but de mettre en place une application de Planning Poker. C'est un jeu utilisé dans les méthodes agiles pour estimer l'effort nécessaire à la réalisation des tâches. Ce planning poker se joue à 6 joueurs maximum.

## Table des matières

1. [Pré-requis](#pré-requis)
2. [Utilisation](#utilisation)
3. [Tests Unitaires](#tests-unitaires)
4. [Fonctionnalités Supplémentaires](#fonctionnalites-supplementaires)

## Pré-requis

Avant d'utiliser l'application, il est important d'avoir Python d'installé. Pour le télécharger, c'est ici : [python.org](https://www.python.org/downloads/).

Pour que l'application fonctionne correctement, vous devez également installer les bibliothèques Python suivantes :
- tkinter
- os
- json
- ctypes
- collections
- statistics
- unittest

### Commandes d'installation

```bash
pip install tk
pip install json
pip install ctypes
pip install collections
pip install statistics
pip install os
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
 L'interface s'ouvre sur le nombre de joueurs de la partie, puis ensuite saisissez les pseudos et enfin choisissez le mode de jeu souhaitez.

#### Les modes de jeu 

 5 modes de jeu sont disponibles : 
 - Strict : on recommence tant que tous les joueurs n'ont pas mis la même estimation.
 - Moyenne : la moyenne des estimations des joueurs correspond à l'estimation finale.
 - Médiane : la médiane des estimations des joueurs correspond à l'estimation finale.
 - Majorité aboslue : la majorité absolue des estimations des joueurs correspond à l'estimation finale.
 - Majorité relative : la majorité relative des estimations des joueurs correspond à l'estimation finale.

#### Les règles 

 Pour que la partie se déroule correctement, il faut suivre les instructions suivantes : 
 - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description.  
 - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passez à la suivante. 
 - Si le bouton recommencer est sélectionné, les informations du json seront perdues.
 - Pour quitter la partie, appuyez sur Fin de la Partie pour quitter l'interface.

Si vous quittez la partie, vous pouvez retrouver votre backlog et les estimations associées dans le fichier JSON : donnees.json
/!\ Mais si vous relancez une partie le fichier JSON est réinitialisé. 

## Tests Unitaires

Les tests unitaires du projet sont présents dans le fichier unittests.py. Vous pouvez les exécuter avec la commande suivante : 

```bash
python unittests.py
```

Voici la liste des fonctions qui sont testées grâce aux tests unitaires : 
- TestApplication :
    - test_entrer_pseudos_valid
    - test_entrer_pseudos_invalid
    
- TestModeStrict : 
    - test_sauvegarder_donnees
    - test_recommencer_partie_mode

- TestModeMoyenne :
    - test_vote_estimation_moyenne
    - test_calcul_moyenne
    - test_sauvegarder_estimation_moyenne

- TestModeMediane :
    - test_vote_estimation_mediane 
    - test_calcul_mediane
    - test_sauvegarder_estimation_mediane

- TestModeMajoriteAbsolue :
    - test_vote_estimation_majorite_abs
    - test_calcul_majorite_abs 
    - test_sauvegarder_estimation_majorite_abs

- TestModeMajoriteRelative :
    - test_vote_estimation_majorite_relative
    - test_calcul_majorite_rel
    - test_sauvegarder_estimation_majorite_rel

## Fonctionnalités Supplémentaires
Certaines fonctionnalités n'ont pas réussi à être implémentées dans le code, mais sur le dépôt il y a une trace des essai pour développer ces fonctionnalités.

Les packages nécessaires pour que ce fichier fonctionne sont les suivants :

### Installation
```bash
pip install Pillow 
pip install cairosvg
pip install tk
pip intsall os
conda install -c conda-forge librsvg
```
et pour lancer le fichier voici la commande suivante : 

```bash
python Fonctionnalites_supplementaires.py
```

### La liste des ajouts
Dans ce fichier de code, nous retrouvons les fonctionnalités concernant l'affichage de carte cliquable, qui fonctionnerait comme des boutons et également un compte à rebours pour chronométrer les joueurs pendant leur partie. 


A vous de jouez maintenant !








