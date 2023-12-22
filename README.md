# Application de Planning Poker Agile

Ce projet a pour but de mettre en place une application de Planning Poker. C'est un jeu utilisé dans les méthodes agiles pour estimer l'effort nécessaire à la réalisation des tâches. Ce planning poker se joue à 6 joueurs maximum

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

### Commandes d'installation

```bash
pip install tk
pip install json
pip install ctypes
pip install collections
pip install statistics
pip install os
```
## Utilisation

Le code de ce projet est présent dans le fichier interface_strict.py
Pour lancer l'application, exécutez ce fichier à l'aide de la commande suivante :

```bash
python interface_strict.py
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

### Les règles 

 Pour que la partie se déroule correctement il faut suivres les instructions suivantes : 
 - Pour chaque tâche de votre backlog entrez un numéro, un nom et une description.  
 - Chaque joueur donne son estimation via les boutons. Une fois votre tâche enregistrée passer à la suivante. 
 - Si le bouton recommencer est sélectionner les informations du json seront perdues
 - Pour quitter la partie appuyez sur Fin de la Partie pour quitter l'interface.

Si vous quittez la partie vous pouvez retrouvez votre backlog et les estimations associés dans le fichier JSON : donnees.json
/!\ Mais si vous relancez une partie le fichier JSON est réinitialisé. 

## Les tests unitaires

Les tests unitaires du projet sont présents dans le fichier unittest.py. Vous pouvez les exécuter avec la commande suivante : 

```bash
python unittest.py
```

Voici la liste des fonctions qui sont testées grâce aux tests unitaires : 
- 
- 
- 
- 



A vous de jouez maintenant !









