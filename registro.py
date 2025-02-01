import sqlite3

def register_tenant():
    conn = sqlite3.connect('residencial.db')
    cursor = conn.cursor()

    # Solicitar datos del inquilino
    casa = input("Número de casa: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")

    # Insertar en la tabla Inquilinos
    cursor.execute('''
        INSERT INTO Inquilinos (casa, nombre, apellido, telefono)
        VALUES (?, ?, ?, ?)
    ''', (casa, nombre, apellido, telefono))
    inquilino_id = cursor.lastrowid  # Obtener el ID del inquilino recién insertado

    print("\nAhora ingrese los vehículos del inquilino.")
    while True:
        placa = input("Placa del vehículo (dejar vacío para terminar): ")
        if not placa:
            break  # Salir del bucle si no hay más vehículos

        color = input("Color del vehículo: ")
        modelo = input("Modelo del vehículo: ")
        conductor = input("Conductor principal: ")

        # Insertar en la tabla Vehiculos
        cursor.execute('''
            INSERT INTO Vehiculos (placa, color, modelo, conductor, inquilino_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (placa, color, modelo, conductor, inquilino_id))

    conn.commit()
    conn.close()
    print("\n✅ Inquilino y vehículos registrados con éxito.")

if __name__ == "__main__":
    register_tenant()
