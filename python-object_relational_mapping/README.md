1. Connect to a MySQL database from a Python script

To connect Python to MySQL, you usually use a library such as mysql-connector-python or PyMySQL.

Install the connector
pip install mysql-connector-python
Example connection
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

print("Connected to MySQL database")
Explanation

host → database server location

user → MySQL username

password → MySQL password

database → name of the database

2. SELECT rows in a MySQL table from a Python script

You can retrieve data using the SQL SELECT command.

Example
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

query = "SELECT * FROM users"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()
Explanation

cursor.execute(query) runs the SQL query

fetchall() retrieves all rows returned by the query

Each row is returned as a tuple

3. INSERT rows in a MySQL table from a Python script

To add data into a table, use the SQL INSERT command.

Example
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

query = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("Alice", "alice@email.com")

cursor.execute(query, values)

connection.commit()

print("Row inserted successfully")

cursor.close()
connection.close()
Important

connection.commit() is required to save the changes to the database.

4. What ORM means

ORM stands for Object Relational Mapping.

It is a programming technique that allows developers to interact with a database using objects instead of SQL queries.

Instead of writing SQL like:

SELECT * FROM users;

You interact with Python objects like:

User.query.all()
Benefits of ORM

Less SQL code to write

Cleaner and more readable code

Easier database management

Better abstraction between application and database

Common Python ORMs:

SQLAlchemy

Django ORM

Peewee

5. Map a Python Class to a MySQL table

Using an ORM like SQLAlchemy, you can map Python classes to database tables.

Install SQLAlchemy
pip install sqlalchemy pymysql
Example mapping
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

engine = create_engine("mysql+pymysql://username:password@localhost/database")

Base.metadata.create_all(engine)
Explanation

User is a Python class

users is the MySQL table

Column defines table columns

create_engine() connects SQLAlchemy to MySQL

create_all() creates the table if it doesn't exist
