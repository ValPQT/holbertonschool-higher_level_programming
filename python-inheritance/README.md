1️⃣ What is a superclass, base class or parent class
👉 Qu’est-ce qu’une superclasse / classe de base / classe parente ?

Une superclasse (ou classe parente / classe de base) est une classe :

dont les attributs et méthodes sont hérités

par une ou plusieurs classes enfants

class Animal:
    def speak(self):
        print("I make a sound")


Ici, Animal est la classe parente.

2️⃣ What is a subclass
👉 Qu’est-ce qu’une sous-classe / classe enfant ?

Une sous-classe est une classe qui :

hérite d’une autre classe

peut réutiliser, modifier ou étendre son comportement

class Dog(Animal):
    pass


Dog est une sous-classe de Animal.

3️⃣ How to list all attributes and methods
👉 Comment lister tous les attributs et méthodes d’une classe ou instance ?
✔ dir()
dir(obj)
dir(Class)

✔ __dict__
obj.__dict__
Class.__dict__


dir() → tout (hérité inclus)

__dict__ → seulement ce qui est défini localement

4️⃣ When can an instance have new attributes
👉 Quand une instance peut-elle avoir de nouveaux attributs ?

Une instance peut avoir de nouveaux attributs :

à tout moment

à l’exécution

obj.new_attr = 42


⚠️ sauf si __slots__ est utilisé.

5️⃣ How to inherit class from another
👉 Comment hériter d’une classe ?
class Child(Parent):
    pass

6️⃣ Multiple base classes
👉 Comment définir une classe avec plusieurs classes parentes ?
class C(A, B):
    pass


➡️ Python supporte l’héritage multiple.

7️⃣ Default base class
👉 De quelle classe toutes les classes héritent-elles par défaut ?

Toutes les classes héritent de :

object

class MyClass:
    pass


est équivalent à :

class MyClass(object):
    pass

8️⃣ Override method or attribute
👉 Comment redéfinir (override) une méthode ou un attribut ?

Il suffit de le redéfinir dans la sous-classe.

class Dog(Animal):
    def speak(self):
        print("Woof")

9️⃣ Inherited attributes and methods
👉 Quels attributs/méthodes sont hérités ?

✔ méthodes publiques
✔ méthodes protégées (_name)
❌ méthodes privées (__name) (name mangling)

🔟 Purpose of inheritance
👉 Quel est le but de l’héritage ?

réutilisation du code

spécialisation

organisation logique

relation « est-un »

Dog est un Animal

1️⃣1️⃣ isinstance, issubclass, type, super
👉 Fonctions intégrées liées à l’héritage
✔ isinstance()
isinstance(obj, Class)


✔ vérifie le type réel (héritage inclus)

✔ issubclass()
issubclass(Sub, Parent)

✔ type()
type(obj)


⚠️ vérifie le type exact

✔ super()

Permet d’appeler une méthode de la classe parente.

super().speak()
