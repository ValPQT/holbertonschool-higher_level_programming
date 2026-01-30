python- if/else, loops, functions

1️⃣ Pourquoi l’indentation est très importante en Python

En Python, l’indentation remplace les accolades {} utilisées dans d’autres langages.

Elle définit les blocs de code.

if x > 0:
    print("positif")
    print("toujours dans le if")


Sans indentation correcte → erreur ou comportement incorrect.

👉 Une indentation incorrecte provoque une IndentationError.

2️⃣ Utiliser if et if ... else

Le if permet d’exécuter du code selon une condition.

if x > 0:
    print("positif")


Avec else :

if x > 0:
    print("positif")
else:
    print("négatif ou zéro")

3️⃣ Utiliser les commentaires

Les commentaires servent à expliquer le code et ne sont pas exécutés.

# Ceci est un commentaire


Commentaires sur plusieurs lignes :

"""
Commentaire
multiligne
"""

4️⃣ Affecter des valeurs à des variables

On utilise le signe = :

age = 20
name = "Alice"
pi = 3.14


Python détecte automatiquement le type.

5️⃣ Utiliser les boucles while et for
Boucle while

Répète tant que la condition est vraie.

i = 0
while i < 3:
    print(i)
    i += 1

Boucle for

Parcourt une séquence.

for i in range(3):
    print(i)

6️⃣ Utiliser break et continue

break → sort de la boucle

continue → passe à l’itération suivante

for i in range(5):
    if i == 3:
        break

for i in range(5):
    if i == 2:
        continue
    print(i)

7️⃣ Utiliser else avec les boucles

Le else s’exécute si la boucle se termine sans break.

for i in range(3):
    print(i)
else:
    print("Boucle terminée normalement")

8️⃣ Le rôle de pass

pass signifie ne rien faire.

Utilisé quand une structure est obligatoire mais vide.

if x > 0:
    pass

9️⃣ Utiliser range

range() génère une suite de nombres.

range(5)        # 0 à 4
range(1, 5)     # 1 à 4
range(1, 10, 2) # 1, 3, 5, 7, 9

🔟 Les fonctions et leur utilisation

Une fonction est un bloc de code réutilisable.

def add(a, b):
    return a + b


Appel :

result = add(2, 3)

1️⃣1️⃣ Fonction sans return

Si une fonction n’a pas de return, elle retourne automatiquement :

None

1️⃣2️⃣ Portée des variables (scope)

Locale : définie dans une fonction

Globale : définie en dehors

x = 10  # globale

def test():
    x = 5  # locale

1️⃣3️⃣ Qu’est-ce qu’un traceback

Un traceback est un message d’erreur qui montre :

où l’erreur s’est produite

le chemin d’exécution du programme

Exemple :

ZeroDivisionError: division by zero

1️⃣4️⃣ Opérateurs arithmétiques
Opérateur	Rôle
+	addition
-	soustraction
*	multiplication
/	division
//	division entière
%	modulo
**	puissance

Exemples :

5 + 2   # 7
5 // 2  # 2
5 % 2   # 1
2 ** 3  # 8
