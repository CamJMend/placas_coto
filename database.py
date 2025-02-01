import sqlite3
#from whatsapp import send_whatsapp_message

def create_database():
    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inquilinos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            casa TEXT,
            nombre TEXT,
            apellido TEXT,
            telefono TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT UNIQUE,
            color TEXT,
            modelo TEXT,
            conductor TEXT,
            inquilino_id INTEGER,
            FOREIGN KEY(inquilino_id) REFERENCES Inquilinos(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS VisitasFrecuentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT UNIQUE,
            inquilino_id INTEGER,
            FOREIGN KEY(inquilino_id) REFERENCES Inquilinos(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def check_plate(plate_text):
    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT I.nombre, I.telefono FROM Inquilinos I
        JOIN Vehiculos V ON I.id = V.inquilino_id
        WHERE V.placa = ?
    ''', (plate_text,))
    
    owner_info = cursor.fetchone()
    conn.close()
    
    if owner_info:
        return {"name": owner_info[0], "phone": owner_info[1]}
    return None

def register_visit(plate_text):
    inquilino_id = input("Ingrese la casa a la que visita: ")
    nombre_visitante = input("Ingrese su nombre: ")
    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT telefono FROM Inquilinos WHERE casa = ?
    ''', (inquilino_id,))
    inquilino = cursor.fetchone()
    
    if inquilino:
        telefono = inquilino[0]
        mensaje = f"{nombre_visitante} con placa {plate_text} solicita acceso. ¿Autoriza la entrada? (SI/NO)"
        #send_whatsapp_message(telefono, mensaje)
    
    conn.close()

create_database()