import worker_class as company

James = company.Secretary("james wick", "001", 700)
Craig = company.Manager("craig duchee", "002", 1500)
Alton = company.FactoryWorker("alton heinzer", "003", 40, 30)
Jose = company.Salesman("jose alvarado", "004", 1000, 2000)

MadlibTech = [James, Craig, Alton, Jose]
MadlibTechTotal = company.Company.calculate_company_payroll(MadlibTech)
WEEKS_IN_MONTH = 4.3
company.Company.calculate_monthly_payroll(WEEKS_IN_MONTH, MadlibTechTotal)

James.work(30)
Craig.work(20)
Alton.work(20)
Jose.work(35)
print("\n\n")
