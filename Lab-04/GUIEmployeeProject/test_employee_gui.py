import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMessageBox
)

from employee_gui import EmployeeWindow
from employee_template import (
    Employee,
    Manager,
    Executive
)


class TestEmployeeWindow(EmployeeWindow):

    def __init__(self):
        super().__init__()

        self.calculate_button.clicked.connect(
            self.calculate_employee_bonus
        )

        self.reset_button.clicked.connect(
            self.reset_form
        )

        self.employee_list_button.clicked.connect(
            self.show_employee_list
        )

        self.manager_button.clicked.connect(
            self.show_manager
        )

        self.executive_button.clicked.connect(
            self.show_executive
        )

    def calculate_employee_bonus(self):

        if (
            self.emp_id_input.text() == ""
            or self.emp_name_input.text() == ""
            or self.extra_days_input.text() == ""
            or self.salary_input.text() == ""
        ):
            QMessageBox.warning(
                self,
                "Error",
                "All employee fields must be completed."
            )
            return

        emp_id = int(
            self.emp_id_input.text()
        )

        emp_name = self.emp_name_input.text()

        extra_days = int(
            self.extra_days_input.text()
        )

        salary = float(
            self.salary_input.text()
        )

        emp1 = Employee(
            emp_id,
            emp_name,
            extra_days,
            salary
        )

        bonus = emp1.CalculateEmpBonus()

        self.bonus_output.setText(
            str(bonus)
        )

        with open(
            "Employee.txt",
            "a"
        ) as emp_file:

            emp_file.write(
                f"{emp1.getEmpId()}\t"
                f"{emp1.getEmpName()}\t"
                f"{emp1.getEmpExtradays()}\t"
                f"{emp1.getEmpSalary()}\t"
                f"{bonus}\n"
            )

    def show_employee_list(self):

        try:
            with open(
                "Employee.txt",
                "r"
            ) as emp_file:

                lines = emp_file.readlines()

            employee_output = ""
            total_bonus = 0

            for line in lines:

                parts = line.strip().split()

                emp_id = parts[0]

                emp_name = (
                    parts[1]
                    + " "
                    + parts[2]
                )

                extra_days = parts[3]
                salary = parts[4]
                bonus = parts[5]

                employee_output += (
                    f"{emp_id} "
                    f"{emp_name} "
                    f"{extra_days} "
                    f"{salary}"
                    f" --> Bonus: "
                    f"{bonus}$\n\n"
                )

                total_bonus += float(
                    bonus
                )

            employee_output += (
                "All Employee Bonuses: "
                f"{total_bonus:.0f}$"
            )

            self.employee_list_text.setText(
                employee_output
            )

        except FileNotFoundError:

            QMessageBox.warning(
                self,
                "Error",
                "Employee.txt was not found."
            )

    def show_manager(self):

        empMan = Manager(
            1298,
            "Pandar Raoul",
            10,
            71000,
            100.5
        )

        manager_bonus = (
            empMan.CalculateEmpBonus()
        )

        manager_result = (
            f"{empMan.getEmpId()} // "
            f"{empMan.getEmpName()} // "
            f"{empMan.getEmpExtradays()} // "
            f"{empMan.getEmpSalary()} // "
            f"{empMan.getEmpExtraHours()}\n"
            f"Bonus: "
            f"{manager_bonus:.2f} $"
        )

        self.manager_text.setText(
            manager_result
        )

    def show_executive(self):

        empExe = Executive(
            5438,
            "Johnston Bob",
            15,
            89000,
            90.25
        )

        executive_bonus = (
            empExe.CalculateEmpBonus()
        )

        executive_result = (
            f"{empExe.getEmpId()} // "
            f"{empExe.getEmpName()} // "
            f"{empExe.getEmpExtradays()} // "
            f"{empExe.getEmpSalary()} // "
            f"{empExe.getEmpExtraHours()}\n"
            f"Bonus: "
            f"{executive_bonus:.2f} $"
        )

        self.executive_text.setText(
            executive_result
        )

    def reset_form(self):

        self.emp_id_input.clear()
        self.emp_name_input.clear()
        self.extra_days_input.clear()
        self.salary_input.clear()
        self.bonus_output.clear()


def main():

    app = QApplication(sys.argv)

    window = TestEmployeeWindow()
    window.show()

    app.exec()


main()