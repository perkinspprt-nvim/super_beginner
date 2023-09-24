import payroll_systemhr as hr

James = hr.SalaryEmployee("james wick", "001", 700);
Craig = hr.SalaryEmployee("craig duchee", "002", 1500);
Alton = hr.Hourly_Employee("alton heinzer", "003", 40, 30);
Jose = hr.Commission_Employee("jose alvarado", "004", 1000, 2000);

MadlibTech = [James, Craig, Alton, Jose];
MadlibTechTotal = hr.PayrollSysytem.calculate_company_payroll(MadlibTech);
WEEKS_IN_MONTH = 4.3;
hr.PayrollSysytem.calculate_monthly_payroll(WEEKS_IN_MONTH, MadlibTechTotal);
