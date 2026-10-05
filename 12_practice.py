# Create a student marks calculator


# Create a student marks calculator

Name = input("Enter your name: ")

Maths = int(input("Enter Maths marks: "))
English = int(input("Enter English marks: "))
Science = int(input("Enter Science marks: "))
Computer = int(input("Enter Computer marks: "))
Hindi = int(input("Enter Hindi marks: "))

Total_Marks = Maths + English + Science + Computer + Hindi

Percentage = (Total_Marks / 500) * 100

print("Name:", Name)
print("Total Marks:", Total_Marks)
print("Percentage:", Percentage, "%")
