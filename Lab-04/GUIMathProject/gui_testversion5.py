import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QWidget,
    QHBoxLayout
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUIMathProject")

        self.label = QLabel("Enter a number")
        self.button = QPushButton("Press me")

        self.button.clicked.connect(
            self.first_button_action
        )

        self.button.clicked.connect(
            self.second_button_action
        )

        self.setFixedSize(300, 250)

        layout = QHBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

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