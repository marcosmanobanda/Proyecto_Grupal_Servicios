import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)

from src.UI.ventana_ui import Ui_MainWindow
from src.services.usuario_service import UsuarioService


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.servicio = UsuarioService()

        self.ui.pushButtonAgregar.clicked.connect(self.agregar_usuario)
        self.ui.pushButtonBuscar.clicked.connect(self.buscar_usuario)
        self.ui.pushButtonEliminar.clicked.connect(self.eliminar_usuario)

        self.mostrar_usuarios()

    def agregar_usuario(self):
        nombre = self.ui.lineEditNombre.text()
        email = self.ui.lineEditEmail.text()
        if not nombre or not email:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        self.servicio.crear_usuario(nombre, email)
        self.ui.lineEditNombre.clear()
        self.ui.lineEditEmail.clear()
        self.mostrar_usuarios()

    def mostrar_usuarios(self, usuarios=None):
        if usuarios is None:
            usuarios = self.servicio.listar_usuarios()
        self.ui.tableWidgetUsuarios.setRowCount(len(usuarios))
        self.ui.tableWidgetUsuarios.setColumnCount(3)
        self.ui.tableWidgetUsuarios.setHorizontalHeaderLabels(["ID", "Nombre", "Email"])
        for i, usuario in enumerate(usuarios):
            self.ui.tableWidgetUsuarios.setItem(i, 0, QTableWidgetItem(str(usuario.id)))
            self.ui.tableWidgetUsuarios.setItem(i, 1, QTableWidgetItem(usuario.nombre))
            self.ui.tableWidgetUsuarios.setItem(i, 2, QTableWidgetItem(usuario.email))

    def buscar_usuario(self):
        termino = self.ui.lineEditBuscar.text().lower()
        usuarios = self.servicio.listar_usuarios()
        filtrados = [u for u in usuarios if termino in u.nombre.lower() or termino in u.email.lower()]
        self.mostrar_usuarios(filtrados)

    def eliminar_usuario(self):
        fila = self.ui.tableWidgetUsuarios.currentRow()
        if fila == -1:
            QMessageBox.information(self, "Info", "Selecciona un usuario.")
            return
        id_item = self.ui.tableWidgetUsuarios.item(fila, 0)
        if not id_item:
            return
        id_usuario = int(id_item.text())
        self.servicio.eliminar_usuario(id_usuario)
        self.mostrar_usuarios()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
