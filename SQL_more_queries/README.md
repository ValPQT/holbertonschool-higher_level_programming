# 📚 Guide Complet : Bases de Données et MySQL

Ce guide couvre les fondamentaux du SQL, de la structure des bases de données relationnelles à l'administration avancée des utilisateurs.

---

## 📌 1. Concepts Fondamentaux

### Qu'est-ce qu'une base de données ?
Une **base de données** est un système permettant de stocker, organiser et gérer des données de manière structurée. Elle permet de **persister les données**, c'est-à-dire de les conserver même après l'arrêt du programme ou du serveur.

### Qu'est-ce qu'une base de données relationnelle ?
Elle organise les données sous forme de **tables** composées de :
* **Colonnes** : Champs avec un type défini (ex: INT, VARCHAR).
* **Lignes** : Enregistrements (données réelles).
Les tables sont reliées entre elles grâce à des **clés primaires** et **clés étrangères**.

---

## 🛠️ 2. Langage SQL et MySQL

### Définitions
* **SQL** (*Structured Query Language*) : Le langage utilisé pour créer, gérer et manipuler les bases de données.
* **MySQL** : Un Système de Gestion de Base de Données Relationnelle (SGBDR) parmi les plus utilisés au monde.

### DDL vs DML
| Catégorie | Signification | Actions | Exemples |
| :--- | :--- | :--- | :--- |
| **DDL** | Data Definition Language | Définit la structure | `CREATE`, `ALTER`, `DROP` |
| **DML** | Data Manipulation Language | Agit sur les données | `INSERT`, `SELECT`, `UPDATE`, `DELETE` |

---

## 🔐 3. Administration et Privilèges

### Gestion des Utilisateurs
Pour créer un utilisateur et définir d'où il peut se connecter :
```sql
CREATE USER 'nom_utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';

Gestion des Privilèges
On utilise GRANT pour donner des accès et REVOKE pour les retirer.

Donner tous les droits : GRANT ALL PRIVILEGES ON base.* TO 'user'@'localhost';

Appliquer les changements : FLUSH PRIVILEGES;

🏗️ 4. Structure et Contraintes (Keys)
PRIMARY KEY (Clé Primaire)
C'est l'identifiant unique d'une ligne.

Elle garantit l'unicité des enregistrements.

Elle est obligatoirement NOT NULL.

FOREIGN KEY (Clé Étrangère)
Colonne qui pointe vers la PRIMARY KEY d'une autre table.

Crée des liens logiques entre les tables.

Garantit l'intégrité référentielle.

Contraintes NOT NULL et UNIQUE
NOT NULL : Empêche une colonne d'être vide (champs critiques).

UNIQUE : Garantit que toutes les valeurs sont distinctes (ex: email), mais peut accepter NULL.

🔍 5. Requêtes Avancées
Jointures (JOIN) vs UNION
JOIN : Combine les colonnes de deux tables horizontalement via un lien logique.

UNION : Combine les résultats (lignes) de deux requêtes verticalement.

Sous-requêtes (Subqueries)
Une requête imbriquée dans une autre pour filtrer des résultats complexes.

SQL
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders);
Fonctions MySQL
Agrégation : COUNT(), SUM(), AVG().

Chaînes : UPPER(), LOWER().

Dates : NOW(), CURDATE().

✅ Conclusion
La maîtrise de MySQL repose sur la compréhension de la structure relationnelle, la rigueur des contraintes (Keys) et la capacité à extraire des données complexes via les jointures et les sous-requêtes.
