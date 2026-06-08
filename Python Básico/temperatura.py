"""temperature"""

celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = 0
kelvin = 0

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"The temperature in fahrenheit is: {fahrenheit}")
print(f"The temperature in kelvin is : {kelvin}")
