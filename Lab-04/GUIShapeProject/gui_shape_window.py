from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QTextEdit
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shape Project")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QGridLayout()
        central_widget.setLayout(self.layout)

        # Labels
        self.length_label = QLabel("Enter length:")
        self.width_label = QLabel("Enter width:")
        self.height_label = QLabel("Enter height:")
        self.perimeter_label = QLabel("Perimeter:")
        self.rect_area_label = QLabel("Area Rectangle:")
        self.box_area_label = QLabel("Area Box:")
        self.volume_label = QLabel("Volume:")

        # Input widgets
        self.length_input = QLineEdit()
        self.width_input = QLineEdit()
        self.height_input = QLineEdit()

        # Output widgets
        self.perimeter_output = QLineEdit()
        self.rect_area_output = QLineEdit()
        self.box_area_output = QLineEdit()
        self.volume_output = QLineEdit()

        self.perimeter_output.setReadOnly(True)
        self.rect_area_output.setReadOnly(True)
        self.box_area_output.setReadOnly(True)
        self.volume_output.setReadOnly(True)

        # Buttons
        self.calculate_button = QPushButton("Calculate")
        self.reset_button = QPushButton("Reset")

        # Text area for inputs and outputs
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # Add widgets to grid
        self.layout.addWidget(self.length_label, 0, 0)
        self.layout.addWidget(self.length_input, 0, 1)

        self.layout.addWidget(self.width_label, 1, 0)
        self.layout.addWidget(self.width_input, 1, 1)

        self.layout.addWidget(self.height_label, 2, 0)
        self.layout.addWidget(self.height_input, 2, 1)

        self.layout.addWidget(self.perimeter_label, 3, 0)
        self.layout.addWidget(self.perimeter_output, 3, 1)

        self.layout.addWidget(self.rect_area_label, 4, 0)
        self.layout.addWidget(self.rect_area_output, 4, 1)

        self.layout.addWidget(self.box_area_label, 5, 0)
        self.layout.addWidget(self.box_area_output, 5, 1)

        self.layout.addWidget(self.volume_label, 6, 0)
        self.layout.addWidget(self.volume_output, 6, 1)

        self.layout.addWidget(self.calculate_button, 7, 0)
        self.layout.addWidget(self.reset_button, 7, 1)

        self.layout.addWidget(self.result_text, 0, 2, 8, 1)