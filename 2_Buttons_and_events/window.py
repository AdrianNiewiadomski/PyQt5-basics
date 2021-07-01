from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# The function to be called when button is clicked.
def print_message():
    print("The button has been clicked.")


def display_window():
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

    my_button = QtWidgets.QPushButton(my_window)
    my_button.setText("Click me")
    my_button.move(180, 180)

    # To connect event to function use:
    my_button.clicked.connect(print_message)

    my_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    display_window()
