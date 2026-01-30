python-data_structures

1️⃣ Qu’est-ce qu’une liste et comment l’utiliser

Une liste est une structure de données qui permet de stocker plusieurs valeurs dans une seule variable.

Caractéristiques :

Ordonnée

Modifiable

Peut contenir différents types

Exemple :

my_list = [1, "hello", 3.5]


Accès :

my_list[0]  # 1

2️⃣ Différences et similitudes entre chaînes et listes
Similitudes :

Ce sont des séquences

Indexables ([0])

On peut les parcourir avec une boucle

Différences :
Strings	Lists
Immuables	Modifiables
Contiennent du texte	Contiennent n’importe quel type
"abc"	['a', 'b', 'c']
3️⃣ Méthodes courantes des listes

append() → ajoute un élément

extend() → ajoute plusieurs éléments

insert() → insère à un index

remove() → supprime une valeur

pop() → supprime un index

sort() → trie

reverse() → inverse

Exemple :

my_list.append(4)

4️⃣ Utiliser les listes comme piles (stack) et files (queue)
Pile (LIFO) :
stack = []
stack.append(1)
stack.pop()

File (FIFO) :
queue = []
queue.append(1)
queue.pop(0)

5️⃣ Les compréhensions de listes

Permettent de créer une liste en une seule ligne.

Exemple :

squares = [x**2 for x in range(5)]


Avec condition :

evens = [x for x in range(10) if x % 2 == 0]

6️⃣ Qu’est-ce qu’un tuple et comment l’utiliser

Un tuple est une séquence immuable.

t = (1, 2, 3)


Avantages :

Plus rapide

Plus sûr

Idéal pour données fixes

7️⃣ Quand utiliser un tuple plutôt qu’une liste

Utilise un tuple quand :

Les données ne doivent pas changer

Tu veux éviter les modifications accidentelles

Tu représentes une paire ou un groupe fixe

8️⃣ Qu’est-ce qu’une séquence

Une séquence est un type de données ordonné et indexable.

Exemples :

String

List

Tuple

Range

9️⃣ Le tuple packing

C’est le fait de regrouper plusieurs valeurs dans un tuple.

t = 1, 2, 3

🔟 Le déballage de séquence (unpacking)

Permet d’assigner plusieurs valeurs en une seule ligne.

a, b, c = t

1️⃣1️⃣ L’instruction del

Permet de supprimer :

une variable

un élément

une liste entière

Exemples :

del my_list[0]
del my_list
