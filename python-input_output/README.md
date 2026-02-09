- Pourquoi la programmation en Python est géniale

Python est apprécié parce qu’il est :

simple à lire et à écrire

très proche du langage humain

polyvalent (web, data, IA, scripts, automatisation…)

doté d’une énorme communauté et de nombreuses bibliothèques

idéal pour apprendre la programmation et pour des projets professionnels

- Comment ouvrir un fichier

On utilise la fonction open() :

en mode lecture ("r")

écriture ("w")

ajout ("a")

Exemple :

f = open("file.txt", "r")

-Comment écrire du texte dans un fichier

On utilise la méthode write() :

f = open("file.txt", "w")
f.write("Hello")
f.close()


⚠️ Le mode "w" écrase le contenu existant.

-Comment lire tout le contenu d’un fichier

Avec la méthode read() :

f = open("file.txt", "r")
content = f.read()
f.close()

-Comment lire un fichier ligne par ligne

Deux méthodes courantes :

for line in f:
    print(line)


ou :

lines = f.readlines()

-Comment déplacer le curseur dans un fichier

Avec seek() :

f.seek(0)  # revient au début du fichier


Et tell() permet de savoir où se trouve le curseur.

-Comment s’assurer qu’un fichier est bien fermé

Deux solutions :

utiliser close()

ou utiliser with (recommandé)

À quoi sert l’instruction with

Elle permet :

d’ouvrir un fichier

de le fermer automatiquement, même en cas d’erreur

Exemple :

with open("file.txt", "r") as f:
    print(f.read())


➡️ Pas besoin de close()

-Qu’est-ce que le JSON

JSON est un format de données :

lisible par les humains

compréhensible par les machines

très utilisé pour échanger des données (API, web, fichiers)

Exemple :

{"name": "Alice", "age": 25}

-Qu’est-ce que la sérialisation

C’est le fait de :
👉 transformer une structure Python (liste, dict…)
👉 en un format stockable ou transmissible (JSON, fichier, etc.)

-Qu’est-ce que la désérialisation

C’est l’opération inverse :
👉 transformer des données JSON
👉 en objets Python utilisables

-Comment convertir une structure Python en chaîne JSON

Avec le module json :

import json
json_string = json.dumps({"a": 1})

-Comment convertir une chaîne JSON en structure Python

Toujours avec json :

data = json.loads(json_string)

-Comment accéder aux paramètres de la ligne de commande

Avec le module sys :

import sys
sys.argv


sys.argv[0] → nom du script

sys.argv[1] → premier argument

sys.argv[2] → deuxième argument
