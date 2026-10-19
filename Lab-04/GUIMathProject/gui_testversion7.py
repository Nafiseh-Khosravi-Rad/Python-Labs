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

from StatisticCalculation import Statistic


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Math Project")
        self.setFixedSize(300, 250)

        self.x_label = QLabel("Enter a number x:")
        self.y_label = QLabel("Enter a number y:")
        self.avg_label = QLabel("Average:")

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.avg_output = QLineEdit()
        self.avg_output.setReadOnly(True)

        self.avg_button = QPushButton("Calculate Average")
        self.reset_button = QPushButton("Reset")

        self.avg_button.clicked.connect(
            self.calculate_average
        )

        self.reset_button.clicked.connect(
            self.reset_form
        )

        layout = QGridLayout()

        layout.addWidget(self.x_label, 0, 0)
        layout.addWidget(self.x_input, 0, 1)

        layout.addWidget(self.y_label, 1, 0)
        layout.addWidget(self.y_input, 1, 1)

        layout.addWidget(self.avg_label, 2, 0)
        layout.addWidget(self.avg_output, 2, 1)

        layout.addWidget(self.avg_button, 3, 0)
        layout.addWidget(self.reset_button, 3, 1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def calculate_average(self):

        x = float(self.x_input.text())
        y = float(self.y_input.text())

        stat_object = Statistic(x, y)

        average = stat_object.calculateAverage()

        self.avg_output.setText(
            str(average)
        )

    def reset_form(self):

        self.x_input.clear()
        self.y_input.clear()
        self.avg_output.clear()


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


main()