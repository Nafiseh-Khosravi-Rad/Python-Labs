import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUIMathProject")

        self.button = QPushButton("Press me")

        self.button.clicked.connect(
            self.first_button_action
        )

        self.button.clicked.connect(
            self.second_button_action
        )

        self.setFixedSize(300, 250)

        self.setCentralWidget(self.button)

    def first_button_action(self):
        print("calculateB was clicked")

    def second_button_action(self):
        print("GUIMathProject clicked")


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


main()