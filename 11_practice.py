# Calculate simple interest using the formula SI = (P * R * T) / 100, where P is the principal amount, R is the rate of interest, and T is the time in years.


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))  
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
