# Trying to understand inheritance in python.
# Parent & Child classes.
# I should write more documentation to prepare for when i do c++


class Employee:
    # Very base class from which the other employee classes will be defined.
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    # Has a definite salary at the end of the week. (Fixed value);
    def __init__(self, name, id_num, weekly_salary):
        super().__init__(name, id_num)
        self.weekly_salary = int(weekly_salary)

    def calculate_payroll(self):
        return self.weekly_salary


class Hourly_Employee(Employee):
    # How much they earn per hour and multiply by the number of hours per week.
    def __init__(self, name, id_num, hours_worked, hourly_pay):
        super().__init__(name, id_num)
        self.hours_worked = int(hours_worked)
        self.hourly_pay = int(hourly_pay)

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_pay


class Commission_Employee(SalaryEmployee):
    # A salary man who also gets seperate commisions.
    def __init__(self, name, id_num, weekly_salary, commission):
        super().__init__(name, id_num, weekly_salary)
        self.commission = int(commission)

    def calculate_payroll(self):
        return self.weekly_salary + self.commission
