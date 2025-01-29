import sqlite3

def create_database():
    conn = sqlite3.connect('plates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_text TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_plate(plate_text):
    conn = sqlite3.connect('plates.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Plates (plate_text) VALUES (?)', (plate_text,))
    conn.commit()
    conn.close()

# Ejecutar al iniciar
create_database()