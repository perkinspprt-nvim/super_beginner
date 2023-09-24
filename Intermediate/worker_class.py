# This is where the workey classes shall be defined.
# Managers = SalaryEmployee, Fairly high salary.
# Secretery = SalaryEmployee, Medium salary.
# Salesman = CommsionEmployee, Low-medium salary, varying commisions.
# FactoryWorker = HourlyEmployee, low-med hours, med pay.

import payroll_systemhr as hr


class Company:
    def calculate_company_payroll(employees):
        print("\n\nCalculating payroll . . . ")
        print("==========================")
        comp_total = 0
        for employee in employees:
            comp_total = comp_total + employee.calculate_payroll()
            print(f"Payroll for: {employee.id_num} <> {employee.name}")
            print(f"Pay-check amount : ${employee.calculate_payroll()}\n")
        print(f"Your company's weekly Total payroll is: ${comp_total}")
        return comp_total

    def calculate_monthly_payroll(weeks, company_total):
        monthly_total_payroll = weeks * company_total
        print(f"Your company's monthly total payroll is : ${monthly_total_payroll}\n")


class Manager(hr.SalaryEmployee):
    def work(self, hours):
        print(
            f"{self.name} spent {hours} hours overworking his employees\n",
            " they also spent the day yelling at his employees.\n",
        )


class Secretary(hr.SalaryEmployee):
    def work(self, hours):
        print(
            f"{self.name} spent {hours} hours being overworked\n",
            " they also did a lot of paper work.\n",
        )


class Salesman(hr.Commission_Employee):
    def work(self, hours):
        print(
            f"{self.name} spent {hours} hours selling the products\n",
            "they also spent the day lying to customers.\n",
        )


class FactoryWorker(hr.Hourly_Employee):
    def work(self, hours):
        print(
            f"{self.name} spent {hours} hours being overworked\n",
            "they almost chopped off his fingers.\n",
        )
