1️⃣ Utiliser l’interpréteur Python

L’interpréteur Python permet d’exécuter du code Python.

Mode interactif

Dans le terminal :

python3


On peut alors taper directement des instructions :

>>> 1 + 1
2
>>> print("Hello")
Hello


Pour quitter :

exit()

Exécuter un fichier Python
python3 script.py

2️⃣ Afficher du texte et des variables avec print

print() permet d’afficher des informations à l’écran.

print("Bonjour")


Avec une variable :

age = 18
print(age)


Texte + variable :

print("Age:", age)


Ou avec formatage moderne :

print(f"Age: {age}")

3️⃣ Utiliser les chaînes de caractères (strings)

Une string est du texte entouré de guillemets :

name = "Alice"


Opérations courantes :

len(name)        # longueur
name.upper()     # majuscules
name.lower()     # minuscules


Concaténation :

message = "Hello " + name

4️⃣ Indexation et slicing

Chaque caractère d’une string possède un index (à partir de 0).

word = "Python"
word[0]   # 'P'
word[1]   # 'y'
word[-1]  # 'n'


Le slicing permet d’extraire une partie :

word[0:2]   # 'Py'
word[2:]    # 'thon'
word[:4]    # 'Pyth'

5️⃣ Style de code Python et pycodestyle

Python suit un style officiel appelé PEP 8.

Règles importantes :

Indentation avec 4 espaces

Lignes de maximum 79 caractères

Noms de fonctions en snake_case

Espaces autour des opérateurs

Pour vérifier le respect du style :

pip install pycodestyle
pycodestyle fichier.py
