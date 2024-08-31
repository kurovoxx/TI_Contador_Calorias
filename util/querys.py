import sqlite3
import datetime

# Para María


def sql_insert(self, nomb, n_cal, sel):
    try:
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()

        if sel == 'Cuantas calorías hay en 100g':
            query = '''
            INSERT INTO alimentos (nombre, calorias_100g) VALUES (?, ?);
            '''
        else:
            query = '''
            INSERT INTO alimentos (nombre, calorias_porcion) VALUES (?, ?);
            '''

        cursor.execute(query, (nomb, n_cal))
        conn.commit()
        print('Alimento insertado con éxito!')

    except sqlite3.Error as error:
        print(f"Error al insertar en la base de datos: {error}")

    finally:
        if conn:
            conn.close()


# Para Hector


def insert(self):
    conn = sqlite3.connect('alimentos.db')
    cursor = conn.cursor()
    query = '''
            INSERT INTO consumo_diario (fecha, nombre) VALUES (?, ?);
            '''
    cursor.execute(query, (datetime.now().strftime('%d-%m-%Y'), self.seleccionar.get()))
    conn.commit()
    conn.close()
    self.ultimo_alimento.configure(text=self.get_ultimo_insertado())
    print('Alimento registrado!')
    try:
        self.get_total_calorias(str(datetime.now().strftime('%d-%m-%Y')))
    except:
        pass

