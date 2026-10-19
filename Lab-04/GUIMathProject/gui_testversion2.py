import sys

from PyQt6.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("GUIMathProject")
    window.show()

    app.exec()


main()
