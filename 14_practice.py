# Create a sallary calculator

basic_salary = float(input("Enter your basic salary: "))
hra = basic_salary * 0.20   
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da

print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)

print("DA (10%):", da)
print("Gross Salary:", gross_salary)

