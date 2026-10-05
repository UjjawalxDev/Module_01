# Take the length and width of a rectangle and print the area and perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)