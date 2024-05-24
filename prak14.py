from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.name_textbox = QLineEdit()
        self.name_textbox.setFont(QFont('Arial'))
        self.name_textbox.setPlaceholderText("Nama")

        self.nim_textbox = QLineEdit()
        self.nim_textbox.setFont(QFont('Arial'))
        self.nim_textbox.setPlaceholderText("NIM")

        self.hobby_textbox = QLineEdit()
        self.hobby_textbox.setFont(QFont('Arial'))
        self.hobby_textbox.setPlaceholderText("Hobi")

        self.submit_button = QPushButton("Kirim")
        self.submit_button.setFont(QFont('Arial'))
        self.submit_button.setStyleSheet("background-color: #82E0AA;")
        self.submit_button.clicked.connect(self.handle_submit)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(QFont('Arial'))
        self.reset_button.setStyleSheet("background-color: #E9F5AA;")
        self.reset_button.clicked.connect(self.reset_fields)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_textbox)
        self.layout.addWidget(self.nim_textbox)
        self.layout.addWidget(self.hobby_textbox)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.reset_button)

    def handle_submit(self):
        name = self.name_textbox.text()
        nim = self.nim_textbox.text()
        hobby = self.hobby_textbox.text()

        if not name:
            self.show_alert("Nama harus diisi!")
            return
        if not nim:
            self.show_alert("NIM harus diisi!")
            return
        if not hobby:
            self.show_alert("Hobi harus diisi!")
            return
        if not nim.isdigit():
            self.show_alert("NIM harus berupa angka!")
            return

        self.label.setText(f"Halo, {name}!\nNIM Anda adalah {nim}\ndan hobi Anda adalah {hobby}.")

    def reset_fields(self):
        self.name_textbox.clear()
        self.nim_textbox.clear()
        self.hobby_textbox.clear()
        self.label.setText("Masukkan detail Anda:")

    def show_alert(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("Peringatan")
        alert.setText(message)
        alert.setIcon(QMessageBox.Warning)
        alert.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        
        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()