class Person:
    def __init__(self, nm, mk) -> None:
        self.name = nm
        self.mykad = mk

    def getName(self):
        return self.name

    def getMyKad(self):
        return self.mykad


class Student(Person):
    def __init__(self, nm, mk, sn) -> None:
        super().__init__(nm, mk)
        self.studnumber = sn

    def getStudNumber(self):
        return self.studnumber


class Lecturer(Person):
    def __init__(self, nm, mk, sn, sal) -> None:
        super().__init__(nm, mk)
        self.staffnumber = sn
        self.salary = sal

    def getStaffNumber(self):
        return self.staffnumber

    def getSalary(self):
        return self.salary
