import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox,
    QTableWidgetItem, QInputDialog
)



from src.UI.vtnservicio import Ui_MainWindow
from src.servicio.modelo_servicio import Servicio


class VentanaPrincipal(QMainWindow):
    """Ventana principal con selección."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.servicios = []

        self.ui.btnGuardar.clicked.connect(self.guardar_servicio)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.ui.btnSalir.clicked.connect(self.close)

    def guardar_servicio(self):
        cliente = self.ui.txtCliente.text().strip()
        descripcion = self.ui.txtServicio.text().strip()
        costo = self.ui.cmbCosto.currentText()
        forma_pago = self.ui.cmbFormaPago.currentText()

        if not cliente or not descripcion:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
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

        servicio = Servicio(cliente, descripcion, costo_float, forma_pago)
        self.servicios.append(servicio)
        self.actualizar_tabla()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.ui.txtCliente.clear()
        self.ui.txtServicio.clear()
        self.ui.cmbCosto.setCurrentIndex(0)
        self.ui.cmbFormaPago.setCurrentIndex(0)

    def actualizar_tabla(self):
        self.ui.tblServicios.setRowCount(len(self.servicios))
        for i, s in enumerate(self.servicios):
            self.ui.tblServicios.setItem(i, 0, QTableWidgetItem(s.cliente))
            self.ui.tblServicios.setItem(i, 1, QTableWidgetItem(s.descripcion))
            self.ui.tblServicios.setItem(i, 2, QTableWidgetItem(f"${s.costo:.2f}"))
            self.ui.tblServicios.setItem(i, 3, QTableWidgetItem(s.forma_pago))

    def seleccionar_servicio(self):
        fila = self.ui.tblServicios.currentRow()
        if fila < 0:
            QMessageBox.information(self, "Seleccionar", "Selecciona un servicio en la tabla.")
            return
        servicio = self.servicios[fila]
        self.ui.txtCliente.setText(servicio.cliente)
        self.ui.txtServicio.setText(servicio.descripcion)
        costo_str = f"{servicio.costo:.2f}"
        idx = self.ui.cmbCosto.findText(costo_str)
        self.ui.cmbCosto.setCurrentIndex(idx)
        idx_fp = self.ui.cmbFormaPago.findText(servicio.forma_pago)
        if idx_fp != -1:
            self.ui.cmbFormaPago.setCurrentIndex(idx_fp)
        else:
            self.ui.cmbFormaPago.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
