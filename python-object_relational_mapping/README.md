# 🐍 Python & MySQL Guide

This guide explains:

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python class to a MySQL table

---

# 1. How to connect to a MySQL database from a Python script

To connect Python to a MySQL database, you can use the library **mysql-connector-python**.

## Installation

```bash
pip install mysql-connector-python
```

## Python connection example

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()

print("Connected to MySQL database")
```

### Explanation

- **host**: The database server location.
- **user**: Your MySQL username.
- **password**: Your MySQL password.
- **database**: The database you want to use.

---

# 2. How to SELECT rows in a MySQL table from a Python script

You can retrieve data using the SQL `SELECT` statement.

## Example

```python
query = "SELECT * FROM users"

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()
```

### Explanation

- `cursor.execute(query)` runs the SQL query.
- `fetchall()` retrieves all rows returned by the query.
- Each row is returned as a **tuple**.

---

# 3. How to INSERT rows in a MySQL table from a Python script

To insert data into a table, use the SQL `INSERT` statement.

## Example

```python
query = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("Alice", "alice@email.com")

cursor.execute(query, values)

connection.commit()

print("Row inserted successfully")
```

### Important

`connection.commit()` is required to save the changes in the database.

---

# 4. What ORM means

**ORM** stands for **Object Relational Mapping**.

It is a programming technique that allows developers to interact with a database using **objects instead of writing SQL queries directly**.

## Example

### Without ORM

```sql
SELECT * FROM users;
```

### With ORM

```python
User.query.all()
```

### Advantages of ORM

- Less SQL code to write
- Cleaner and more readable code
- Easier database management
- Better abstraction between application and database

Popular Python ORMs include:

- SQLAlchemy
- Django ORM
- Peewee

---

# 5. How to map a Python Class to a MySQL table

Using an ORM like **SQLAlchemy**, you can map a Python class to a database table.

## Installation

```bash
pip install sqlalchemy pymysql
```

## Example

```python
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
```

### Explanation

- **User**: Python class representing the table.
- **users**: Name of the MySQL table.
- **Column**: Defines table columns.
- **create_engine()**: Connects SQLAlchemy to MySQL.
- **create_all()**: Creates the table if it does not exist.
