import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMessageBox
)

from PyQt6.QtGui import QDoubleValidator

from gui_shape_window import MainWindow
from rectangle_shape import Rectangle
from box_shape import Box


class ShapeWindow(MainWindow):

    def __init__(self):
        super().__init__()

        # Allow only positive numbers
        validator = QDoubleValidator()
        validator.setBottom(0.01)

        self.length_input.setValidator(validator)
        self.width_input.setValidator(validator)
        self.height_input.setValidator(validator)

        # Connect buttons
        self.calculate_button.clicked.connect(
            self.calculate_shape
        )

        self.reset_button.clicked.connect(
            self.reset_form
        )

    def calculate_shape(self):

        # Check empty inputs
        if self.length_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Input length cannot be empty!"
            )
            return

        if self.width_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Input width cannot be empty!"
            )
            return

        if self.height_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Input height cannot be empty!"
            )
            return

        # Read user inputs
        length = float(self.length_input.text())
        width = float(self.width_input.text())
        height = float(self.height_input.text())

        # Instantiate objects
        myrectobj = Rectangle(length, width)
        myboxobj = Box(length, width, height)

        # Calculate values
        perimeter = myrectobj.calcPerimeter()
        rectangle_area = myrectobj.calcArea()
        box_area = myboxobj.calcArea()
        volume = myboxobj.calcVolume()

        # Display results
        self.perimeter_output.setText(
            str(perimeter)
        )

        self.rect_area_output.setText(
            str(rectangle_area)
        )

        self.box_area_output.setText(
            str(box_area)
        )

        self.volume_output.setText(
            str(volume)
        )

        # Display inputs and outputs in QTextEdit
        result = (
            "Shape parameters:\n"
            f"Length = {length}\n"
            f"Width = {width}\n"
            f"Height = {height}\n\n"
            "Shape results:\n"
            f"Perimeter = {perimeter}\n"
            f"Rectangle Area = {rectangle_area}\n"
            f"Box Area = {box_area}\n"
            f"Volume = {volume}"
        )

        self.result_text.setText(result)

        # Store Rectangle data
        with open("Rect.txt", "a") as rect_file:
            rect_file.write(
                f"{length}\t{width}\t"
                f"{perimeter}\t{rectangle_area}\n"
            )

        # Store Box data
        with open("Box.txt", "a") as box_file:
            box_file.write(
                f"{length}\t{width}\t{height}\t"
                f"{box_area}\t{volume}\n"
            )

    def reset_form(self):

        self.length_input.clear()
        self.width_input.clear()
        self.height_input.clear()

        self.perimeter_output.clear()
        self.rect_area_output.clear()
        self.box_area_output.clear()
        self.volume_output.clear()

        self.result_text.clear()


def main():

    app = QApplication(sys.argv)

    window = ShapeWindow()
    window.show()

    sys.exit(app.exec())


main()