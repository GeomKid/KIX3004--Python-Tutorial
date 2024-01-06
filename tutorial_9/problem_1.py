import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from ui_file import Ui_MainWindow


class MyForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.convert_values)

    def convert_values(self):
        farenheit_value = int(self.lineEdit.text())
        celcius_value = round((farenheit_value - 32) * 5 / 9, 4)
        self.label.setText(f"<html><head/><body><p>{farenheit_value} Farenheit is equivalent</p><p> to {celcius_value} Celcius</p></body></html>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()
    sys.exit(app.exec())
