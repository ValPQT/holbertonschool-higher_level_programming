Python - Classes

1️⃣ What is OOP
👉 Qu’est-ce que la Programmation Orientée Objet (POO / OOP) ?

La POO est un paradigme de programmation basé sur :

des classes

des objets

la modélisation du monde réel

Objectifs principaux :

organiser le code

le rendre réutilisable

faciliter la maintenance

Concepts clés :

encapsulation

abstraction

héritage

polymorphisme

2️⃣ “first-class everything”
👉 Que signifie « tout est de première classe » en Python ?

En Python, tout est un objet :

fonctions

classes

modules

types

Cela signifie qu’on peut :

les assigner à une variable

les passer en argument

les retourner depuis une fonction

def f(): pass
x = f

3️⃣ What is a class
👉 Qu’est-ce qu’une classe ?

Une classe est un plan (blueprint) pour créer des objets.

Elle définit :

des attributs

des méthodes

class Person:
    pass

4️⃣ What is an object and an instance
👉 Qu’est-ce qu’un objet et une instance ?

Un objet est une entité concrète en mémoire

Une instance est un objet créé à partir d’une classe

p = Person()  # p est une instance de Person

5️⃣ Difference class vs object
👉 Différence entre classe et objet ?
Classe	Objet
modèle	instance
abstraite	concrète
pas en mémoire active	en mémoire
6️⃣ What is an attribute
👉 Qu’est-ce qu’un attribut ?

Un attribut est une variable attachée à :

une classe

une instance

p.name = "Ali"

7️⃣ Public / Protected / Private
👉 Attributs publics, protégés et privés

Python utilise une convention, pas une protection réelle.

Type	Syntaxe	Signification
Public	name	accessible partout
Protected	_name	usage interne
Private	__name	name mangling
self._age
self.__salary

8️⃣ What is self
👉 Qu’est-ce que self ?

self est :

la référence à l’instance courante

passé automatiquement aux méthodes

def speak(self):
    print(self.name)

9️⃣ What is a method
👉 Qu’est-ce qu’une méthode ?

Une méthode est une fonction définie dans une classe.

class A:
    def f(self):
        pass

🔟 init
👉 Qu’est-ce que la méthode spéciale __init__ ?

C’est le constructeur :

appelé à la création de l’objet

initialise les attributs

def __init__(self, name):
    self.name = name

1️⃣1️⃣ Abstraction / Encapsulation / Information Hiding
👉 Ces notions expliquées

Abstraction : montrer l’essentiel

Encapsulation : regrouper données + méthodes

Information Hiding : cacher les détails internes

1️⃣2️⃣ What is a property
👉 Qu’est-ce qu’une propriété ?

Une property permet d’accéder à un attribut via une méthode.

@property
def age(self):
    return self._age

1️⃣3️⃣ Attribute vs Property
👉 Différence attribut / propriété
Attribut	Propriété
accès direct	accès contrôlé
pas de logique	logique possible
1️⃣4️⃣ Pythonic getters and setters
👉 Façon Pythonique de faire getters/setters

❌ Java style
✔ @property

@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    self._age = value

1️⃣5️⃣ Dynamic attributes
👉 Créer dynamiquement des attributs
obj.new_attr = 42


Python le permet à l’exécution.

1️⃣6️⃣ Bind attributes
👉 Lier des attributs aux objets et classes
Class.attr = 10
obj.attr = 20

1️⃣7️⃣ dict
👉 Qu’est-ce que __dict__ ?

__dict__ contient :

les attributs d’un objet

sous forme de dictionnaire

obj.__dict__
Class.__dict__

1️⃣8️⃣ Attribute lookup
👉 Comment Python trouve un attribut ?

Ordre :

instance

classe

classes parentes

→ MRO (Method Resolution Order)

1️⃣9️⃣ getattr
👉 Comment utiliser getattr() ?
getattr(obj, "attr", default)


accès dynamique

évite AttributeError
