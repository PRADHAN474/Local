# database.py

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def fetch_notes_from_database(class_number):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute("SELECT notes FROM notes_table WHERE class_number = %s", (class_number,))
    notes = cursor.fetchone()[0]
    conn.close()
    return notes
  
