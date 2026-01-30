python-more_data_structures

1️⃣ Pourquoi programmer en Python est génial

Python est apprécié parce que :

La syntaxe est simple et lisible

Le code est court

Il est très polyvalent (web, data, IA, scripts, automatisation)

Il a une énorme communauté et beaucoup de bibliothèques

Il est idéal pour apprendre la programmation

2️⃣ Les ensembles (sets) et comment les utiliser

Un set est une collection non ordonnée :

Sans doublons

Modifiable

Très rapide pour les tests d’appartenance

Création :

s = {1, 2, 3}

3️⃣ Méthodes courantes des sets

add() → ajoute un élément

remove() → supprime (erreur si absent)

discard() → supprime sans erreur

union() → union de sets

intersection() → éléments communs

difference() → différence

Exemple :

s.add(4)

4️⃣ Quand utiliser un set plutôt qu’une liste

Utilise un set quand :

Tu veux éviter les doublons

Tu dois tester rapidement si un élément existe

L’ordre n’a pas d’importance

Utilise une liste quand :

L’ordre est important

Tu as besoin d’index

5️⃣ Parcourir un set

On parcourt un set avec une boucle for :

for x in s:
    print(x)


⚠️ L’ordre n’est pas garanti.

6️⃣ Les dictionnaires et comment les utiliser

Un dictionnaire stocke des données sous forme de clé : valeur.

d = {"name": "Alice", "age": 25}


Accès :

d["name"]

7️⃣ Quand utiliser un dictionnaire plutôt qu’une liste ou un set

Utilise un dictionnaire quand :

Tu veux associer une valeur à une clé

Tu veux accéder rapidement à une donnée précise

Les données sont structurées

8️⃣ Qu’est-ce qu’une clé dans un dictionnaire

Une clé :

Identifie une valeur

Est unique

Est immuable (string, int, tuple)

Exemple :

d["age"] = 30

9️⃣ Parcourir un dictionnaire

Clés :

for key in d:
    print(key)


Valeurs :

for value in d.values():
    print(value)


Clés et valeurs :

for key, value in d.items():
    print(key, value)

🔟 Les fonctions lambda

Une fonction lambda est une fonction anonyme, écrite en une ligne.

add = lambda a, b: a + b


Utilisée pour des opérations simples.

1️⃣1️⃣ La fonction map

Applique une fonction à chaque élément d’un iterable.

list(map(lambda x: x * 2, [1, 2, 3]))

1️⃣2️⃣ La fonction filter

Filtre les éléments selon une condition.

list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

1️⃣3️⃣ La fonction reduce

Réduit une liste à une seule valeur.

from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3])
