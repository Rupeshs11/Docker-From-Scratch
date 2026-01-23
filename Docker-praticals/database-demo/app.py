# mysql_create_db.py

import mysql.connector

# STEP 1: connect to MySQL server (no database yet)
conn = mysql.connector.connect(
    host="mysqldb",
    user="knox",
    password="knoxpass",
    database="userinfo"
)

cursor = conn.cursor()

# # STEP 2: create database
# cursor.execute("CREATE DATABASE IF NOT EXISTS userdb")

# # STEP 3: use database
# cursor.execute("USE userdb")

# STEP 4: create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")

# STEP 5: take input and insert
name = input("Enter your name: ")
cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
conn.commit()

# STEP 6: show all users
choice = input("Do you want to see all users? (y/n): ").lower()

if choice == "y":
    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()
    print("\nStored Users:")
    for row in rows:
        print(row[0], "-", row[1])

# STEP 7: close connection
cursor.close()
conn.close()
