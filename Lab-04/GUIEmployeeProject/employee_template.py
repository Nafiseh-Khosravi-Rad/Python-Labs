class Employee:

    def __init__(self, empId, empName, empExtradays, empSalary):
        self.__empId = empId
        self.__empName = empName
        self.__empExtradays = empExtradays
        self.__empSalary = empSalary

    def getEmpId(self):
        return self.__empId

    def getEmpName(self):
        return self.__empName

    def getEmpExtradays(self):
        return self.__empExtradays

    def getEmpSalary(self):
        return self.__empSalary

    def setEmpId(self, empId):
        self.__empId = empId

    def setEmpName(self, empName):
        self.__empName = empName

    def setEmpExtradays(self, empExtradays):
        self.__empExtradays = empExtradays

    def setEmpSalary(self, empSalary):
        self.__empSalary = empSalary

    def CalculateEmpBonus(self):
        return self.__empExtradays * 120


class Executive(Employee):

    def __init__(
        self,
        empId,
        empName,
        empExtradays,
        empSalary,
        empExtraHours
    ):
        super().__init__(
            empId,
            empName,
            empExtradays,
            empSalary
        )

        self.__empExtraHours = empExtraHours

    def getEmpExtraHours(self):
        return self.__empExtraHours

    def setEmpExtraHours(self, empExtraHours):
        self.__empExtraHours = empExtraHours

    def CalculateEmpBonus(self):
        return (
            self.getEmpExtradays() * 500
            + (self.__empExtraHours / 8) * 50
        )


class Manager(Employee):

    def __init__(
        self,
        empId,
        empName,
        empExtradays,
        empSalary,
        empExtraHours
    ):
        super().__init__(
            empId,
            empName,
            empExtradays,
            empSalary
        )

        self.__empExtraHours = empExtraHours

    def getEmpExtraHours(self):
        return self.__empExtraHours

    def setEmpExtraHours(self, empExtraHours):
        self.__empExtraHours = empExtraHours

    def CalculateEmpBonus(self):
        return (
            self.getEmpExtradays() * 350
            + (self.__empExtraHours / 8) * 35
        )