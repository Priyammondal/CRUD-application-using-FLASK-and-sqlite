import sqlite3
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
connection = sqlite3.connect(currentDirectory + "\phonebook.db")
print("Opened database successfully")
query1 = "CREATE TABLE students(name TEXT, addr TEXT, city TEXT, pin TEXT)"
cursor = connection.cursor()
cursor.execute(query1)
print("table created successfully")
connection.close()
