from src.dao.usuario_dao import UsuarioDAO
from src.models.usuario import Usuario


class UsuarioService:
    def crear_usuario(self, nombre, email):
        usuario = Usuario(id=0, nombre=nombre, email=email)
        UsuarioDAO.agregar_usuario(usuario)
        return usuario

    def listar_usuarios(self):
        return UsuarioDAO.obtener_todos()

    def obtener_usuario(self, id):
        return UsuarioDAO.buscar_por_id(id)

    def eliminar_usuario(self, id):
        UsuarioDAO.eliminar_usuario(id)

