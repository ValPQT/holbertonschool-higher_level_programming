🐍 Guide de Connexion MySQL avec Python & ORM
Ce guide explique comment connecter Python à une base de données MySQL, manipuler des données avec SQL brut, et utiliser un ORM (Object Relational Mapping).

1. Connexion à une base de données MySQL
Pour connecter Python à MySQL, on utilise généralement des bibliothèques comme mysql-connector-python ou PyMySQL.

🛠️ Installation du connecteur
Bash
pip install mysql-connector-python
💻 Exemple de connexion
Python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()
print("Connected to MySQL database")
📝 Explications
host : Emplacement du serveur de base de données.

user : Nom d'utilisateur MySQL.

password : Mot de passe MySQL.

database : Nom de la base de données.

2. Lire des données (SELECT)
Vous pouvez récupérer des données en utilisant la commande SQL SELECT.

💻 Exemple
Python
query = "SELECT * FROM users"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()
📝 Explications
cursor.execute(query) : Exécute la requête SQL.

fetchall() : Récupère toutes les lignes retournées par la requête.

Chaque ligne est retournée sous forme de tuple.

3. Insérer des données (INSERT)
Pour ajouter des données dans une table, utilisez la commande SQL INSERT.

💻 Exemple
Python
query = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("Alice", "alice@email.com")

cursor.execute(query, values)
connection.commit() # Très important !

print("Row inserted successfully")
[!IMPORTANT]
connection.commit() est obligatoire pour enregistrer les modifications dans la base de données.

4. Qu'est-ce qu'un ORM ?
ORM signifie Object Relational Mapping.

C'est une technique de programmation qui permet aux développeurs d'interagir avec une base de données en utilisant des objets au lieu de requêtes SQL brutes.

Sans ORM (SQL) : SELECT * FROM users;

Avec ORM (Python) : User.query.all()

✅ Avantages de l'ORM
Moins de code SQL à écrire.

Code plus propre et plus lisible.

Gestion simplifiée de la base de données.

Meilleure abstraction entre l'application et la base.

ORMs Python populaires : SQLAlchemy, Django ORM, Peewee.

5. Mapper une Classe Python à une table MySQL
Avec un ORM comme SQLAlchemy, vous pouvez lier directement vos classes Python à vos tables.

🛠️ Installation
Bash
pip install sqlalchemy pymysql
💻 Exemple de Mapping
Python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

# Connexion
engine = create_engine("mysql+pymysql://username:password@localhost/database")

# Création de la table
Base.metadata.create_all(engine)
📝 Explications
User : La classe Python.

users : Le nom de la table dans MySQL.

Column : Définit les colonnes de la table.

create_engine() : Connecte SQLAlchemy à MySQL.

create_all() : Crée la table automatiquement si elle n'existe pas.
