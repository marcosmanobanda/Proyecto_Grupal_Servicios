from PySide6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEditNombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditNombre.setGeometry(QtCore.QRect(30, 20, 200, 30))
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.lineEditNombre.setPlaceholderText("Nombre")

        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(250, 20, 200, 30))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditEmail.setPlaceholderText("Email")

        self.pushButtonAgregar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAgregar.setGeometry(QtCore.QRect(470, 20, 100, 30))
        self.pushButtonAgregar.setObjectName("pushButtonAgregar")
        self.pushButtonAgregar.setText("Agregar")

        self.lineEditBuscar = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditBuscar.setGeometry(QtCore.QRect(30, 60, 300, 30))
        self.lineEditBuscar.setObjectName("lineEditBuscar")
        self.lineEditBuscar.setPlaceholderText("Buscar por nombre o email")

        self.pushButtonBuscar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBuscar.setGeometry(QtCore.QRect(340, 60, 100, 30))
        self.pushButtonBuscar.setObjectName("pushButtonBuscar")
        self.pushButtonBuscar.setText("Buscar")

        self.tableWidgetUsuarios = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidgetUsuarios.setGeometry(QtCore.QRect(30, 100, 540, 220))
        self.tableWidgetUsuarios.setObjectName("tableWidgetUsuarios")

        self.pushButtonEliminar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonEliminar.setGeometry(QtCore.QRect(30, 330, 200, 30))
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")
        self.pushButtonEliminar.setText("Eliminar Usuario Seleccionado")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Gestión de Usuarios")
