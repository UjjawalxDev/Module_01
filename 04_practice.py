# Convert celcius to fahrenheit and fahrenheit to celcius
celcius=float(input("Enter temperature in celcius: "))
fahrenheit = (celcius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit=float(input("Enter temperature in Fahrenheit: "))
celcius = (fahrenheit - 32) * 5/9
print("Temperature in Celcius:", celcius)