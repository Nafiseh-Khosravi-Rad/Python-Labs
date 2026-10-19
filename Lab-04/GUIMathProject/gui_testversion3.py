import sys

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton
)


def main():

    app = QApplication(sys.argv)

    window = QPushButton("Press me")
    window.setWindowTitle("GUIMathProject")
    window.resize(300, 250)

    window.show()

    app.exec()


main()