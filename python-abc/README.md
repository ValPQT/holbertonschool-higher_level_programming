1️⃣ Classes abstraites (Abstract Classes)
👉 De quoi il s’agit

Les classes abstraites servent à définir une structure commune pour plusieurs classes, sans forcément fournir toutes les implémentations.

Elles permettent :

d’imposer certaines méthodes obligatoires

d’éviter l’instanciation directe d’une classe incomplète

👉 À quoi ça sert

On les utilise quand plusieurs classes doivent respecter les mêmes règles, mais avec des comportements différents.

👉 Exemple
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


Toute classe qui hérite de Animal doit implémenter speak().

2️⃣ Interfaces et Duck Typing
👉 Interfaces (concept)

Une interface définit ce qu’un objet doit savoir faire, pas comment.

En Python, il n’y a pas d’interface stricte comme en Java, mais on utilise :

des classes abstraites

ou simplement des conventions

👉 Duck Typing

Principe fondamental en Python :

Si ça se comporte comme un canard, alors c’est un canard.

👉 Peu importe le type réel de l’objet, tant qu’il possède les méthodes attendues.

👉 Exemple
def make_sound(animal):
    animal.speak()


Tout objet ayant une méthode speak() fonctionne, même s’il n’hérite pas d’une classe précise.

3️⃣ Héritage des classes de base standard
👉 De quoi il s’agit

Python permet d’hériter de classes intégrées comme :

list

dict

set

iterator

👉 Pourquoi faire ça

Pour créer des structures personnalisées tout en gardant les fonctionnalités de base.

👉 Exemple
class MyList(list):
    def print_sorted(self):
        print(sorted(self))


Tu ajoutes un comportement sans perdre les avantages de list.

4️⃣ Redéfinition de méthodes (Method Overriding)
👉 De quoi il s’agit

C’est le fait de réécrire une méthode d’une classe parente dans une classe enfant.

👉 Pourquoi

Modifier un comportement

L’adapter

L’enrichir

👉 Exemple
class Square(Rectangle):
    def area(self):
        return self.size * self.size


La méthode area() remplace celle du parent.

5️⃣ Héritage multiple (Multiple Inheritance)
👉 De quoi il s’agit

Une classe peut hériter de plusieurs classes à la fois.

👉 Pourquoi

Pour combiner plusieurs comportements dans une seule classe.

👉 Exemple
class Flyable:
    def fly(self):
        print("I can fly")

class Swimmable:
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    pass


La classe Duck hérite des deux comportements.

⚠️ À utiliser avec prudence (ordre de résolution des méthodes).

6️⃣ Mixins
👉 Qu’est-ce qu’un mixin

Un mixin est une petite classe spécialisée, utilisée uniquement pour ajouter une fonctionnalité.

👉 Elle :

n’est pas conçue pour être instanciée seule

sert à enrichir d’autres classes

👉 Exemple
class JsonMixin:
    def to_json(self):
        return {"data": self.__dict__}


Utilisation :

class User(JsonMixin):
    def __init__(self, name):
        self.name = name


👉 User gagne la méthode to_json().
