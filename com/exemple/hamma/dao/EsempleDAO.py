'''
Created on 28 déc. 2023

@author: courant
'''

import sqlite3
conn = ''
try:
    cursor = conn.cursor()
    cursor.execute("""
    DROP TABLE users
    """)
    conn.commit()

    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTERGER
)
""")
    conn.commit()
except sqlite3.OperationalError:
    print('Erreur la table existe déjà')
except Exception as e:
    print("Erreur")
    conn.rollback()
    # raise e
finally:
    conn.close()
