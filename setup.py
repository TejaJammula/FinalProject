import sqlite3

conn = sqlite3.connect('mobile_company.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS mobiles')
cursor.execute('DROP TABLE IF EXISTS companies')

cursor.execute('''
CREATE TABLE IF NOT EXISTS companies (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS mobiles (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 release_year INTEGER,
 company_id INTEGER,
 FOREIGN KEY (company_id) REFERENCES companies(id)
)
''')

cursor.execute("INSERT INTO companies (name) VALUES ('Samsung')")
cursor.execute("INSERT INTO companies (name) VALUES ('Apple')")
cursor.execute("INSERT INTO companies (name) VALUES ('Nexon')")
cursor.execute("INSERT INTO companies (name) VALUES ('Celkon')")
cursor.execute("INSERT INTO companies (name) VALUES ('moto')")
cursor.execute("INSERT INTO companies (name) VALUES ('blueberry')")
cursor.execute("INSERT INTO mobiles (title, release_year, company_id) VALUES ('Mobile 1', 2020, 1)")
cursor.execute("INSERT INTO mobiles (title, release_year, company_id) VALUES ('Mobile 2', 2021, 2)")

conn.commit()
