class Employee:
    'Common based class for all employee'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print("Total employee %d" %Employee.empCount)

    def display_employee(self):
        print("Name: ", self.name, "Salary: ", self.salary)
    