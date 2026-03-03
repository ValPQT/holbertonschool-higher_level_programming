# 📚 Notions de Base sur les Bases de Données et MySQL

## 📌 Qu'est-ce qu'une base de données ?

Une **base de données** est un système permettant de **stocker,
organiser et gérer des données** de manière structurée afin de pouvoir
les consulter, les modifier et les supprimer efficacement.

Elle permet de **persister les données**, c'est-à-dire de les conserver
même après l'arrêt du programme ou du serveur.

------------------------------------------------------------------------

## 📌 Qu'est-ce qu'une base de données relationnelle ?

Une **base de données relationnelle** organise les données sous forme de
**tables** composées de :

-   **Colonnes** (champs avec un type défini)
-   **Lignes** (enregistrements)

Les tables peuvent être reliées entre elles grâce à des **clés
primaires** et **clés étrangères**.

Exemples : MySQL, PostgreSQL, Oracle.

------------------------------------------------------------------------

## 📌 Que signifie SQL ?

**SQL** signifie **Structured Query Language** (Langage de Requête
Structuré).

C'est le langage utilisé pour : - Créer des bases de données - Gérer les
tables - Manipuler les données

------------------------------------------------------------------------

## 📌 Qu'est-ce que MySQL ?

**MySQL** est un **système de gestion de base de données relationnelle
(SGBDR)**.

Il permet de : - Créer des bases de données - Gérer des tables -
Exécuter des requêtes SQL

C'est l'un des SGBDR les plus utilisés au monde.

------------------------------------------------------------------------

## 📌 Comment créer une base de données dans MySQL ?

``` sql
CREATE DATABASE nom_de_la_base;
```

Pour utiliser la base de données :

``` sql
USE nom_de_la_base;
```

------------------------------------------------------------------------

## 📌 Que signifient DDL et DML ?

### 🔹 DDL --- Data Definition Language

Langage de Définition des Données.\
Permet de définir ou modifier la structure de la base.

Exemples : - `CREATE` - `ALTER` - `DROP` - `TRUNCATE`

### 🔹 DML --- Data Manipulation Language

Langage de Manipulation des Données.\
Permet d'agir sur les données.

Exemples : - `INSERT` - `SELECT` - `UPDATE` - `DELETE`

------------------------------------------------------------------------

## 📌 Comment CREATE ou ALTER une table ?

### Créer une table :

``` sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### Modifier une table :

``` sql
ALTER TABLE users ADD age INT;
```

------------------------------------------------------------------------

## 📌 Comment SELECT des données ?

``` sql
SELECT * FROM users;
```

Avec condition :

``` sql
SELECT name, email FROM users WHERE age > 18;
```

------------------------------------------------------------------------

## 📌 Comment INSERT, UPDATE ou DELETE des données ?

### INSERT :

``` sql
INSERT INTO users (name, email, age)
VALUES ('John', 'john@email.com', 25);
```

### UPDATE :

``` sql
UPDATE users
SET age = 26
WHERE id = 1;
```

### DELETE :

``` sql
DELETE FROM users
WHERE id = 1;
```

------------------------------------------------------------------------

## 📌 Qu'est-ce qu'une sous-requête (subquery) ?

Une **sous-requête** est une requête SQL imbriquée dans une autre
requête.

Exemple :

``` sql
SELECT name
FROM users
WHERE id IN (
    SELECT user_id FROM orders
);
```

Elle permet d'utiliser le résultat d'une requête dans une autre.

------------------------------------------------------------------------

## 📌 Comment utiliser les fonctions MySQL ?

MySQL propose des fonctions intégrées pour manipuler les données.

### Fonctions d'agrégation :

``` sql
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
```

### Fonctions sur les chaînes de caractères :

``` sql
SELECT UPPER(name) FROM users;
```

### Fonctions sur les dates :

``` sql
SELECT NOW();
```

------------------------------------------------------------------------

# ✅ Conclusion

Pour bien maîtriser MySQL, il faut comprendre :

-   La structure des bases relationnelles
-   La différence entre DDL et DML
-   Les opérations CRUD
-   Les sous-requêtes
-   Les fonctions SQL

La pratique régulière des requêtes SQL est essentielle pour progresser.

