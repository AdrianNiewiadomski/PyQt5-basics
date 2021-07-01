from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    my_window = QMainWindow()
    x_position = 0
    y_position = 0
    width = 480
    height = 320
    my_window.setGeometry(x_position, y_position, width, height)
    my_window.setWindowTitle("My new window")

    text = QtWidgets.QLabel(my_window)
    text.setText("Hello world")
    text.move(180, 140)

    # To show window
    my_window.show()

    # app.exec() runs the application while sys.exit ensures that process is finished
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
