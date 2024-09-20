import sqlite3
from random import sample

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS projects;')

cursor.execute("""
    CREATE TABLE projects
    (url TEXT, descr TEXT, income INTEGER)
""")
cursor.execute("""INSERT INTO projects VALUES 
    ('giraffes.io', 'Uber, but with giraffes', 1900),
    ('dronesweaters.com', 'Clothes for cold drones', 3000),
    ('hummingpro.io', 'Online humming courses', 120000)
""")

cursor.execute('DROP TABLE IF EXISTS YA_projects;')

cursor.execute("""
    CREATE TABLE YA_projects
    (col1 INTEGER, col2 INTEGER, col3 INTEGER, col4 INTEGER, col5 INTEGER)
""")

insert_rows = []

for i in range(0, 100):
    insert_rows.append(tuple(sample(range(0, 99999), 5)))

cursor.execute(f"""INSERT INTO YA_projects VALUES 
    {str(insert_rows)[1:-1]}
""")

connection.commit()