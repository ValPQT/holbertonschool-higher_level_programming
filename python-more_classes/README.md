Python - more_classes

1️⃣ Pourquoi Python est génial

Python est apprécié parce qu’il est :

Simple à lire et à écrire

Orienté objet

Flexible et puissant

Très utilisé dans le monde professionnel

Il permet de se concentrer sur la logique plutôt que sur la syntaxe.

2️⃣ Qu’est-ce que la programmation orientée objet (OOP)

L’OOP est une façon d’organiser le code autour de classes et objets.
Elle permet de :

Structurer le code

Réutiliser facilement

Représenter des objets du monde réel

3️⃣ « First-class everything »

En Python, tout est un objet :

Fonctions

Classes

Types

Variables

👉 On peut les stocker, les passer en paramètre, les retourner.

4️⃣ Qu’est-ce qu’une classe

Une classe est un plan (modèle) qui définit :

Des attributs (données)

Des méthodes (comportements)

5️⃣ Qu’est-ce qu’un objet / une instance

Un objet (ou instance) est une création concrète d’une classe.
La classe définit la structure, l’objet contient les valeurs réelles.

6️⃣ Différence entre classe et objet

Classe : le modèle

Objet : un exemplaire de ce modèle

7️⃣ Qu’est-ce qu’un attribut

Un attribut est une variable attachée à :

Un objet

Ou une classe

Il représente une donnée.

8️⃣ Attributs publics, protégés et privés

Public : accessible partout (name)

Protégé : convention interne (_name)

Privé : inaccessible directement (__name)

👉 En Python, c’est surtout une convention, pas une restriction stricte.

9️⃣ Qu’est-ce que self

self représente l’instance courante.
Il permet d’accéder aux attributs et méthodes de l’objet.

🔟 Qu’est-ce qu’une méthode

Une méthode est une fonction définie dans une classe.
Elle agit sur les données de l’objet via self.

1️⃣1️⃣ Le constructeur __init__

__init__ est une méthode spéciale :

Appelée automatiquement à la création de l’objet

Sert à initialiser les attributs

1️⃣2️⃣ Abstraction, Encapsulation, Information Hiding

Abstraction : montrer l’essentiel, cacher le détail

Encapsulation : regrouper données + comportements

Information hiding : protéger l’accès aux données sensibles

1️⃣3️⃣ Qu’est-ce qu’une propriété

Une propriété permet :

D’accéder à une méthode comme un attribut

De contrôler lecture et écriture

1️⃣4️⃣ Attribut vs propriété

Attribut : accès direct à une variable

Propriété : accès contrôlé via des méthodes

1️⃣5️⃣ Getters et setters « pythonic »

En Python, on utilise :

@property

@attribut.setter

👉 On évite les méthodes get_x() et set_x().

1️⃣6️⃣ Méthodes spéciales __str__ et __repr__

__str__ : affichage lisible pour l’utilisateur

__repr__ : représentation technique pour le développeur

1️⃣7️⃣ Différence entre __str__ et __repr__

__str__ → humain

__repr__ → développeur / debug

1️⃣8️⃣ Attribut de classe

Un attribut de classe :

Appartient à la classe

Est partagé par toutes les instances

1️⃣9️⃣ Attribut d’objet vs attribut de classe

Attribut d’objet → propre à chaque instance

Attribut de classe → commun à toutes

2️⃣0️⃣ Méthode de classe

Une méthode de classe :

Utilise cls

Agit sur la classe

Modifie les attributs de classe

2️⃣1️⃣ Méthode statique

Une méthode statique :

N’utilise ni self ni cls

Est liée logiquement à la classe

2️⃣2️⃣ Création dynamique d’attributs

Python permet d’ajouter :

Des attributs à un objet

Des attributs à une classe
à n’importe quel moment.

2️⃣3️⃣ Lier des attributs aux objets et classes

Attribut ajouté à l’objet → visible uniquement sur cet objet

Attribut ajouté à la classe → visible sur tous les objets

2️⃣4️⃣ Le __dict__

__dict__ contient :

Tous les attributs d’un objet ou d’une classe

Sous forme de dictionnaire

2️⃣5️⃣ Comment Python cherche un attribut

Python cherche dans cet ordre :

L’objet

La classe

Les classes parentes

2️⃣6️⃣ getattr

getattr permet :

D’accéder dynamiquement à un attribut

D’éviter des erreurs si l’attribut n’existe pas

