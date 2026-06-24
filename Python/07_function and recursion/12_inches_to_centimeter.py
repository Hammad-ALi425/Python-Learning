# Write a function to convert inchs to centimeter


def converter(inches):
    return inches * 2.54

a = int(input("Enter value in inches: "))
print(f"{a} inches in centimeters is {converter(a)}")