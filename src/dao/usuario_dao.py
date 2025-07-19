

from src.conexion_sql import get_connection
from src.models.usuario import Usuario


class UsuarioDAO:
    @classmethod
    def agregar_usuario(cls, usuario: Usuario):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios (nombre, email) VALUES (?, ?)",
            usuario.nombre, usuario.email
        )
        conn.commit()
        conn.close()

    @classmethod
    def obtener_todos(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM Usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(id=row[0], nombre=row[1], email=row[2]) for row in rows]

    @classmethod
    def buscar_por_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM Usuarios WHERE id = ?", id)
        row = cursor.fetchone()
        conn.close()
        return Usuario(id=row[0], nombre=row[1], email=row[2]) if row else None

    @classmethod
    def eliminar_usuario(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id = ?", id)
        conn.commit()
        conn.close()


