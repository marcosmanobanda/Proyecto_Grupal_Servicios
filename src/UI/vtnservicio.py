from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox,
    QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
)

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Soluciones PC")
        MainWindow.resize(520, 480)

        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.lblTitulo = QLabel("Soluciones PC")
        font = self.lblTitulo.font()
        font.setPointSize(14)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lblTitulo)

        self.cedulaLayout = QHBoxLayout()

        self.txtCedula = QLineEdit()
        self.txtCedula.setPlaceholderText("Ingrese cédula (10 dígitos)")
        self.txtCedula.setMaxLength(10)
        self.txtCedula.setValidator(QIntValidator(0, 1234567890))
        self.verticalLayout.addWidget(self.txtCedula)

        self.btnBuscar = QPushButton("🔍")
        self.btnBuscar.setToolTip("Buscar por cédula")
        self.cedulaLayout.addWidget(self.btnBuscar)

        self.verticalLayout.addLayout(self.cedulaLayout)

        self.txtCliente = QLineEdit()
        self.txtCliente.setPlaceholderText("Nombre del cliente")
        self.verticalLayout.addWidget(self.txtCliente)

        self.txtServicio = QLineEdit()
        self.txtServicio.setPlaceholderText("Descripción del servicio")
        self.verticalLayout.addWidget(self.txtServicio)

        self.cmbCosto = QComboBox()
        self.cmbCosto.addItems(["Seleccionar","30.00", "50.00", "80.00", "120.00","Otro"])
        self.verticalLayout.addWidget(self.cmbCosto)

        self.cmbFormaPago = QComboBox()
        self.cmbFormaPago.addItems([
            "Seleccionar","Efectivo", "Tarjeta de crédito", "Tarjeta de débito",
            "Transferencia bancaria", "Pago móvil"
        ])
        self.verticalLayout.addWidget(self.cmbFormaPago)

        self.botonesLayout = QHBoxLayout()
        self.btnGuardar = QPushButton("Guardar")
        self.btnLimpiar = QPushButton("Limpiar")
        self.btnSalir = QPushButton("Salir")
        self.botonesLayout.addWidget(self.btnGuardar)
        self.botonesLayout.addWidget(self.btnLimpiar)
        self.botonesLayout.addWidget(self.btnSalir)
        self.verticalLayout.addLayout(self.botonesLayout)

        self.tblServicios = QTableWidget()
        self.tblServicios.setColumnCount(5)
        self.tblServicios.setHorizontalHeaderLabels(["Cédula", "Cliente", "Servicio", "Costo", "Forma de Pago"])
        self.verticalLayout.addWidget(self.tblServicios)

        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)
