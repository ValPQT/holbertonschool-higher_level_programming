import modules project

1️⃣ Pourquoi programmer en Python est génial

Python est apprécié parce que :

Sa syntaxe est simple et lisible

On écrit moins de code pour faire la même chose

Il est polyvalent (web, data, IA, scripts, automatisation)

Il possède une grande communauté

Beaucoup de bibliothèques sont déjà disponibles

👉 Python permet de se concentrer sur la logique plutôt que sur la syntaxe.

2️⃣ Importer des fonctions depuis un autre fichier

On peut utiliser du code écrit dans un autre fichier Python.

Exemple :

from math import sqrt


Ou importer tout le fichier :

import math

3️⃣ Utiliser les fonctions importées

Après l’import :

print(math.sqrt(16))


Ou avec import direct :

from math import sqrt
print(sqrt(16))

4️⃣ Créer un module

Un module est un simple fichier .py.

Exemple :

# my_module.py
def hello():
    print("Hello")


Utilisation :

import my_module
my_module.hello()

5️⃣ Utiliser la fonction intégrée dir()

dir() liste tout ce qui est disponible dans un module ou un objet.

import math
print(dir(math))


Utile pour :

découvrir des fonctions

déboguer

explorer une bibliothèque

6️⃣ Empêcher l’exécution d’un code lors de l’import

On utilise cette condition :

if __name__ == "__main__":


Cela signifie :

le code s’exécute uniquement si le fichier est lancé directement

pas s’il est importé

Exemple :

def main():
    print("Programme principal")

if __name__ == "__main__":
    main()

7️⃣ Utiliser les arguments en ligne de commande

Les arguments sont accessibles via sys.argv.

import sys
print(sys.argv)


sys.argv[0] → nom du script

sys.argv[1] → premier argument

Exemple :

python script.py 10 20

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
