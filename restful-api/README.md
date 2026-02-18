# 🌐 API Development & Web Fundamentals

Ce guide regroupe les notions essentielles pour comprendre, consommer et développer des APIs, du protocole de base jusqu'à la sécurisation avancée.

---

## 🏗️ HTTP/HTTPS Basics
Le **HTTP** (*HyperText Transfer Protocol*) est le langage de communication du Web entre un client (navigateur) et un serveur.
* **Principes fondamentaux :** Fonctionne sur un cycle **Requête/Réponse**. Chaque échange est indépendant (stateless).
* **Transfert de données :** Les données transitent via des en-têtes (headers) et un corps (body).
* **Méthodes :** Utilisation de verbes standards comme `GET` (lecture), `POST` (création), `PUT` (mise à jour) et `DELETE` (suppression).
* **Sécurité :** Le **HTTPS** est la version sécurisée qui chiffre les données via **SSL/TLS**, empêchant l'interception des informations sensibles.

## 🐚 API Consumption with Command Line
Interagir avec une API via le terminal est la première étape pour comprendre la structure brute des données.
* **Outils :** Utilisation de commandes comme `curl` ou `httpie`.
* **Objectif :** Apprendre à envoyer des requêtes manuelles, manipuler les headers et visualiser les réponses JSON sans l'abstraction d'un langage de programmation.

## 🐍 API Consumption with Python
L'étape suivante consiste à automatiser la récupération de données en utilisant la puissance de Python.
* **Outils :** Bibliothèque `requests`.
* **Capacités :** Transformer des réponses JSON en dictionnaires Python, gérer les sessions, et traiter de gros volumes de données pour une analyse ou une manipulation complexe.

## 🛠️ API Development with http.server
Comprendre les mécanismes internes d'un serveur Web en partant de zéro.
* **Approche :** Utilisation du module natif `http.server` de Python.
* **Apprentissage :** Gestion manuelle des routes, des codes de statut (200, 404, 500) et des flux d'entrée/sortie, posant les bases de la logique serveur.

## 🌶️ API Development with Flask
Passage à un framework professionnel et léger pour construire des APIs robustes.
* **Focus :** Simplification du **routage**, gestion dynamique des paramètres d'URL, et intégration de la logique métier de manière organisée et scalable.

## 🔐 API Security & Authentication
La protection des données est un aspect critique du développement.
* **Mécanismes :** Mise en œuvre de clés d'API (**API Keys**), de jetons **JWT** (JSON Web Tokens) ou de protocoles **OAuth2**.
* **Objectif :** Garantir que seul un utilisateur autorisé peut accéder à une ressource spécifique et protéger le transfert contre les attaques malveillantes.

## 📑 API Standards & Documentation with OpenAPI
La maintenabilité d'une API repose sur sa documentation.
* **Standard :** Utilisation d'**OpenAPI** (Swagger) pour décrire les points de terminaison, les modèles de données et les exemples de réponses.
* **Bénéfice :** Permet une collaboration fluide entre les développeurs frontend et backend grâce à une documentation interactive et auto-générée.
