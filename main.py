import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox,
    QTableWidgetItem, QInputDialog
)



from src.UI.vtnservicio import Ui_MainWindow
from src.conexion_sql import ConexionSQL
from src.servicio.modelo_servicio import Servicio


class VentanaPrincipal(QMainWindow):
    """Ventana principal con selección."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.servicios = []

        self.ui.tblServicios.setColumnCount(5)
        self.ui.tblServicios.setHorizontalHeaderLabels(["Cédula", "Cliente", "Servicio", "Costo", "Forma de Pago"])

        self.ui.btnGuardar.clicked.connect(self.guardar_servicio)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.ui.btnSalir.clicked.connect(self.close)
        self.ui.btnBuscar.clicked.connect(self.buscar_por_cedula)

    def guardar_servicio(self):
        cedula = self.ui.txtCedula.text().strip()
        cliente = self.ui.txtCliente.text().strip()
        descripcion = self.ui.txtServicio.text().strip()
        costo = self.ui.cmbCosto.currentText()
        forma_pago = self.ui.cmbFormaPago.currentText()

        if not cedula or not cedula.isdigit() or len(cedula) != 10:
            QMessageBox.warning(self, "Error", "La cédula debe tener exactamente 10 dígitos.")
            return

        if not cliente or not descripcion or costo == "Seleccionar" or forma_pago == "Seleccionar":
            QMessageBox.warning(self, "Datos incompletos", "Por favor, llene todos los datos.")
            return

        if costo == "Otro":
            nuevo_costo, ok = QInputDialog.getText(self, "Costo personalizado", "Ingrese el costo:")
            if not ok or not nuevo_costo.strip():
                return
            costo = nuevo_costo.strip()

        try:
            costo_float = float(costo)
        except ValueError:
            QMessageBox.warning(self, "Error", "Costo inválido.")
            return

        servicio = Servicio(cedula, cliente, descripcion, costo_float, forma_pago)
        servicio.cedula = cedula
        self.servicios.append(servicio)
        self.actualizar_tabla()
        #self.limpiar_campos()
        self.cargar_servicios_desde_bd()

    def cargar_servicios_desde_bd(self):
        conexion = ConexionSQL()
        conn = conexion.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT Cedula, Cliente, Descripcion, Costo, FormaPago FROM Servicios")
                registros = cursor.fetchall()
                self.servicios.clear()
                for fila in registros:
                    cedula, cliente, descripcion, costo, forma_pago = fila
                    servicio = Servicio(cedula, cliente, descripcion, costo, forma_pago)
                    self.servicios.append(servicio)
                self.actualizar_tabla()
            except Exception as e:
                QMessageBox.critical(self, "Error al cargar datos", str(e))
            finally:
                conexion.cerrar()


    def limpiar_campos(self, sin_confirmacion=False):
        if not sin_confirmacion:
            respuesta = QMessageBox.question(
                self,
                "Confirmar limpieza",
                "¿Estás seguro que deseas limpiar los campos?",
                QMessageBox.Yes | QMessageBox.No
            )
            if respuesta != QMessageBox.Yes:
                return
        self.ui.txtCedula.clear()
        self.ui.txtCliente.clear()
        self.ui.txtServicio.clear()
        self.ui.cmbCosto.setCurrentIndex(0)
        self.ui.cmbFormaPago.setCurrentIndex(0)





    def actualizar_tabla(self):
        self.ui.tblServicios.setRowCount(len(self.servicios))
        for i, s in enumerate(self.servicios):
            self.ui.tblServicios.setItem(i, 0, QTableWidgetItem(s.cedula))
            self.ui.tblServicios.setItem(i, 1, QTableWidgetItem(s.cliente))
            self.ui.tblServicios.setItem(i, 2, QTableWidgetItem(s.descripcion))
            self.ui.tblServicios.setItem(i, 3, QTableWidgetItem(f"${s.costo:.2f}"))
            self.ui.tblServicios.setItem(i, 4, QTableWidgetItem(s.forma_pago))

    def buscar_por_cedula(self):
        cedula = self.ui.txtCedula.text().strip()

        if not cedula or not cedula.isdigit() or len(cedula) != 10:
            QMessageBox.warning(self, "Error", "Ingrese una cédula válida de 10 dígitos.")
            return

        servicio_encontrado = None
        for servicio in self.servicios:
            if servicio.cedula == cedula:
                servicio_encontrado = servicio
                break

        if servicio_encontrado:
            self.ui.txtCliente.setText(servicio_encontrado.cliente)
            self.ui.txtServicio.setText(servicio_encontrado.descripcion)
            costo_str = f"{servicio_encontrado.costo:.2f}"
            idx_costo = self.ui.cmbCosto.findText(costo_str)
            self.ui.cmbCosto.setCurrentIndex(idx_costo if idx_costo != -1 else 0)

            idx_fp = self.ui.cmbFormaPago.findText(servicio_encontrado.forma_pago)
            self.ui.cmbFormaPago.setCurrentIndex(idx_fp if idx_fp != -1 else 0)
        else:
            QMessageBox.information(self, "No encontrado", f"No se encontró servicio con cédula: {cedula}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
