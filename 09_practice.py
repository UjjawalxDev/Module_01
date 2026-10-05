# Take a three digit number and calculate the sum of its digits


number = int(input("Enter a three-digit number: "))
# Extracting the digits 
digit1 = number // 100
print("Digit 1:", digit1)
digit2 = (number // 10) % 10
print("Digit 2:", digit2)
digit3 = number % 10
print("Digit 3:", digit3)

sum_of_digits = digit1 + digit2 + digit3
print("Sum of digits:", sum_of_digits)
