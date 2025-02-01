import sqlite3

def fetch_table_records(table_name):
    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(f'SELECT * FROM {table_name}')
        records = cursor.fetchall()
        
        if records:
            for record in records:
                print(record)
        else:
            print(f"La tabla '{table_name}' está vacía.")
    
    except sqlite3.Error as e:
        print(f"Error al obtener los datos: {e}")
    
    conn.close()

if __name__ == "__main__":
    print("Tablas disponibles: Inquilinos, Vehiculos, VisitasFrecuentes")
    table_name = input("Ingrese el nombre de la tabla que desea ver: ")
    fetch_table_records(table_name)
