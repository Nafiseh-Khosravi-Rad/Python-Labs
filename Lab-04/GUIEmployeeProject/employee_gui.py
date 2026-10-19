from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout
)


class EmployeeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Project")
        self.resize(650, 700)

        # -------------------------
        # Employee Grid Layout
        # -------------------------

        self.emp_id_label = QLabel("Enter Emp ID:")
        self.emp_name_label = QLabel("Enter Emp Name:")
        self.extra_days_label = QLabel("Enter Emp Extra days:")
        self.salary_label = QLabel("Enter Emp Salary:")
        self.bonus_label = QLabel("Emp Bonus:")

        self.emp_id_input = QLineEdit()
        self.emp_name_input = QLineEdit()
        self.extra_days_input = QLineEdit()
        self.salary_input = QLineEdit()

        self.bonus_output = QLineEdit()
        self.bonus_output.setReadOnly(True)

        self.calculate_button = QPushButton(
            "Calculate Emp Bonus"
        )

        self.reset_button = QPushButton(
            "Reset"
        )

        employee_grid = QGridLayout()

        employee_grid.addWidget(
            self.emp_id_label, 0, 0
        )
        employee_grid.addWidget(
            self.emp_id_input, 0, 1
        )

        employee_grid.addWidget(
            self.emp_name_label, 1, 0
        )
        employee_grid.addWidget(
            self.emp_name_input, 1, 1
        )

        employee_grid.addWidget(
            self.extra_days_label, 2, 0
        )
        employee_grid.addWidget(
            self.extra_days_input, 2, 1
        )

        employee_grid.addWidget(
            self.salary_label, 3, 0
        )
        employee_grid.addWidget(
            self.salary_input, 3, 1
        )

        employee_grid.addWidget(
            self.bonus_label, 4, 0
        )
        employee_grid.addWidget(
            self.bonus_output, 4, 1
        )

        employee_grid.addWidget(
            self.calculate_button, 5, 0
        )

        employee_grid.addWidget(
            self.reset_button, 5, 1
        )

        # -------------------------
        # Employee List
        # -------------------------

        self.employee_list_title = QLabel(
            "Employee List"
        )

        self.employee_list_text = QTextEdit()
        self.employee_list_text.setReadOnly(True)

        self.employee_list_button = QPushButton(
            "Employee List"
        )

        employee_list_layout = QVBoxLayout()

        employee_list_layout.addWidget(
            self.employee_list_title
        )

        employee_list_layout.addWidget(
            self.employee_list_text
        )

        employee_list_layout.addWidget(
            self.employee_list_button
        )

        # -------------------------
        # Manager Section
        # -------------------------

        self.manager_title = QLabel("Manager")

        self.manager_text = QTextEdit()
        self.manager_text.setReadOnly(True)

        self.manager_button = QPushButton(
            "Manager Bonus"
        )

        manager_layout = QVBoxLayout()

        manager_layout.addWidget(
            self.manager_title
        )

        manager_layout.addWidget(
            self.manager_text
        )

        manager_layout.addWidget(
            self.manager_button
        )

        # -------------------------
        # Executive Section
        # -------------------------

        self.executive_title = QLabel("Executive")

        self.executive_text = QTextEdit()
        self.executive_text.setReadOnly(True)

        self.executive_button = QPushButton(
            "Executive Bonus"
        )

        executive_layout = QVBoxLayout()

        executive_layout.addWidget(
            self.executive_title
        )

        executive_layout.addWidget(
            self.executive_text
        )

        executive_layout.addWidget(
            self.executive_button
        )

        # -------------------------
        # Manager + Executive Row
        # -------------------------

        bottom_layout = QHBoxLayout()

        bottom_layout.addLayout(
            manager_layout
        )

        bottom_layout.addLayout(
            executive_layout
        )

        # -------------------------
        # Main Nested Layout
        # -------------------------

        main_layout = QVBoxLayout()

        main_layout.addLayout(
            employee_grid
        )

        main_layout.addLayout(
            employee_list_layout
        )

        main_layout.addLayout(
            bottom_layout
        )

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)