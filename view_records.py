import sqlite3

def fetch_records():
    conn = sqlite3.connect('plates.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Plates')
    records = cursor.fetchall()
    conn.close()
    return records

if __name__ == "__main__":
    records = fetch_records()
    for record in records:
        print(record)