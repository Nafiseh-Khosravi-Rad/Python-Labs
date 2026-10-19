import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUIMathProject")

        self.calculate_button = QPushButton("Calculate")
        self.number_label = QLabel("Enter a number")
        self.number_input = QLineEdit()

        self.calculate_button.clicked.connect(
            self.first_action
        )

        self.calculate_button.clicked.connect(
            self.second_action
        )

        self.setFixedSize(300, 250)

        layout = QGridLayout()

        layout.addWidget(self.number_label, 0, 0)
        layout.addWidget(self.number_input, 0, 1)

        layout.addWidget(
            self.calculate_button,
            1,
            0,
            1,
            2
        )

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def first_action(self):
        print("Calculate button was clicked")

    def second_action(self):
        print("Entered value:", self.number_input.text())


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


main()