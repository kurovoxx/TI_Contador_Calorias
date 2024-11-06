import sqlite3
from datetime import datetime
from CTkMessagebox import CTkMessagebox

class Recordatorio:
    def __init__(self, usuario):
        self.usuario = usuario
        self.ultimo_msj = None

    def mostrar_mensaje_recordatorio(self):
        CTkMessagebox(
            title="Recordatorio",
            message="No has registrado tu peso según la frecuencia establecida. Por favor, actualiza tu peso.",
            icon="warning", option_1="OK"
        )
    def mostrar_mensaje_recordatorio_unavez(self, cursor):
        fecha_hoy = datetime.now().date()

        if self.ultimo_msj != fecha_hoy:
            self.mostrar_mensaje_recordatorio()
            self.ultimo_msj = fecha_hoy
        
            cursor.execute("""
                UPDATE datos 
                SET recordatorio = 'mostrado_hoy' 
                WHERE nombre = ?
            """, (self.usuario,))

    def recordar_actualizar_peso(self):
            try:
                conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
                cursor = conn.cursor()

                cursor.execute("SELECT recordatorio, cantidad_dias FROM datos WHERE nombre = ?", (self.usuario,))
                config = cursor.fetchone()

                if config:
                    estado, frecuencia = config
                    frecuencia_dias = int(frecuencia.split()[0])

                    cursor.execute("SELECT fecha FROM peso ORDER BY fecha DESC LIMIT 1")
                    ultimo_registro = cursor.fetchone()

                    if ultimo_registro and ultimo_registro[0]:
                        ultima_fecha = datetime.strptime(ultimo_registro[0], '%d-%m-%Y')
                        dias_diferencia = (datetime.now() - ultima_fecha).days

                        if (dias_diferencia >= frecuencia_dias and estado != 'mostrado_hoy') or estado == 'mostrado':
                            self.mostrar_mensaje_recordatorio_unavez(cursor)
                        else:
                            cursor.execute("""
                                UPDATE datos 
                                SET recordatorio = 'on' 
                                WHERE nombre = ?
                            """, (self.usuario,))
                    else:
                    
                        if estado != 'mostrado_hoy':  
                            self.mostrar_mensaje_recordatorio_unavez(cursor)

                conn.commit()
                conn.close()

            except sqlite3.Error as e:
                CTkMessagebox(title="Error", message=f"Error al acceder a la base de datos: {e}", icon="info", option_1="OK")
            except Exception as e:
                CTkMessagebox(title="Error", message=f"Error inesperado: {e}", icon="info", option_1="OK")
                
    #Funcion para que el recordatorio este por defecto en 1dia            
    def recordatorio_por_defecto(usuario):
            conn = sqlite3.connect(f"./users/{usuario}/alimentos.db")
            cursor = conn.cursor()

            cursor.execute("SELECT cantidad_dias FROM datos WHERE nombre = ?", (usuario,))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute("""
                    UPDATE datos
                    SET cantidad_dias = '1 día'
                    WHERE nombre = ? AND (cantidad_dias IS NULL OR cantidad_dias = '')
                """, (usuario,))
            else:
                cursor.execute("""
                    INSERT INTO datos (nombre, recordatorio, cantidad_dias)
                    VALUES (?, 'off', '1 día')
                """, (usuario,))

            conn.commit()
            conn.close()

