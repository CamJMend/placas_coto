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
    casa = input("Ingrese la casa a la que visita: ")
    nombre_visitante = input("Ingrese su nombre: ")

    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, telefono FROM Inquilinos WHERE casa = ?', (casa,))
    inquilino = cursor.fetchone()

    print(inquilino)
    
    if inquilino:
        inquilino_id, telefono = inquilino
        mensaje = f"{nombre_visitante} con placa {plate_text} solicita acceso. ¿Autoriza la entrada? (SI/NO)"
        
        autorizacion = input(mensaje + " ").strip().upper()
        
        if autorizacion == "SI":
            print("Acceso autorizado ✅")

            # Verificar si la placa ya está registrada como visita frecuente
            cursor.execute('SELECT 1 FROM VisitasFrecuentes WHERE placa = ?', (plate_text,))
            es_frecuente = cursor.fetchone()

            if not es_frecuente:  # Solo preguntar si la placa NO está en la base de datos
                registrar_frecuente = input("¿Desea registrar esta placa como visita frecuente? (SI/NO) ").strip().upper()
                if registrar_frecuente == "SI":
                    cursor.execute('INSERT INTO VisitasFrecuentes (placa, inquilino_id) VALUES (?, ?)', (plate_text, inquilino_id))
                    conn.commit()
                    print("Placa registrada como visita frecuente 📝")
                else:
                    print("Placa no registrada como visita frecuente.")
            else:
                print("Esta placa ya está registrada como visita frecuente. ✅")

        else:
            print("Acceso denegado ❌")

    else:
        print("No se encontró la casa en el registro. ❌")
    
    conn.close()

create_database()