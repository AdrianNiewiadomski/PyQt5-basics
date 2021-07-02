from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 480, 320)
        self.setWindowTitle("My new window")
        self.text = None
        self.my_button = None
        self.init_ui()

    def init_ui(self):
        self.text = QtWidgets.QLabel(self)
        self.text.setText("Hello world")
        self.text.move(180, 140)

        self.my_button = QtWidgets.QPushButton(self)
        self.my_button.setText("Click me")
        self.my_button.move(180, 180)

        self.my_button.clicked.connect(self.print_message)

    def print_message(self):
        self.text.setText("The button has been clicked.")
        # To adjust size of label to display whole text.
        self.text.adjustSize()


def display_window():
    app = QApplication(sys.argv)
    my_window = MyWindow()

    my_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    display_window()
