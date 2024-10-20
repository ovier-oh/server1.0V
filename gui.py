import sys
import request
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit,QPushButton, QBoxLayout,QMessageBox


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login to Flask Server")
        self.setGeometry(100, 100, 300, 150)

        # Crear widgets
        self.label_email = QLabel("Email:")
        self.inout_email = QLineEdit()
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")