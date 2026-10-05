# Take marks of 5 subjects and calculate total and percentage

English=float(input("Enter marks of English: "))
Maths=float(input("Enter marks of Maths: "))
Science=float(input("Enter marks of Science: "))
Social=float(input("Enter marks of Social: "))
Hindi=float(input("Enter marks of Hindi: "))

total=English+Maths+Science+Social+Hindi
percentage=total/5*100

print("Total marks:", total)
print("Percentage:", percentage)