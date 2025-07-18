import pyodbc


class ConexionSQL:
    def __init__(self):
        self.server = '192.168.1.10'  # IP del servidor
        self.database = 'ServiciosPC'
        self.connection = None

    def conectar(self):
        try:
            self.connection = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'Trusted_Connection=yes;'
            )
            print("✅ Conexión exitosa con autenticación de Windows")
            return self.connection
        except Exception as e:
            print("❌ Error al conectar:", e)
            return None


    def cerrar(self):
        if self.connection:
            self.connection.close()
            print("🔒 Conexión cerrada")
            self.connection = None

# Prueba directa
if __name__ == "__main__":
    conexion = ConexionSQL()
    conn = conexion.conectar()
    if conn:
        conexion.cerrar()
