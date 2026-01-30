python-exceptions

1️⃣ Pourquoi programmer en Python est génial

Python est génial parce que :

Il est simple à lire et à écrire

Il permet de faire beaucoup avec peu de lignes

Il gère automatiquement la mémoire

Il possède un système d’exceptions très puissant

Il est utilisé partout (web, IA, scripts, automatisation)

2️⃣ Différence entre erreurs et exceptions

Erreur : problème qui empêche le programme de s’exécuter
👉 exemple : erreur de syntaxe

Exception : erreur détectée pendant l’exécution
👉 exemple : division par zéro

👉 Une erreur bloque le programme immédiatement
👉 Une exception peut être gérée

3️⃣ Qu’est-ce qu’une exception et comment l’utiliser

Une exception est un événement qui interrompt le flux normal du programme.

Exemples d’exceptions :

ValueError

TypeError

IndexError

ZeroDivisionError

On les utilise avec try / except.

4️⃣ Quand utiliser les exceptions

On utilise les exceptions quand :

Une erreur peut arriver normalement

Une entrée utilisateur est imprévisible

Un fichier peut ne pas exister

Une opération peut échouer

👉 Pas pour contrôler la logique normale du programme.

5️⃣ Comment gérer correctement une exception

Structure classique :

try → code à surveiller

except → gestion de l’erreur

else → s’exécute si aucune erreur

finally → toujours exécuté

Cela permet d’éviter le crash du programme.

6️⃣ Pourquoi attraper les exceptions

Attraper une exception permet de :

Empêcher le programme de planter

Afficher un message clair

Continuer l’exécution

Gérer proprement les erreurs

👉 Améliore la robustesse du programme.

7️⃣ Comment lever une exception intégrée

On peut forcer une exception avec raise :

raise ValueError("Message d'erreur")


Utile pour :

Vérifier des conditions

Bloquer un comportement invalide

Rendre le code plus clair

8️⃣ Quand faire une action de nettoyage après une exception

On fait un nettoyage quand :

On ouvre un fichier

On alloue des ressources

On modifie un état temporaire

👉 Utiliser finally pour garantir le nettoyage :

fermer un fichier

libérer une ressource

restaurer un état
