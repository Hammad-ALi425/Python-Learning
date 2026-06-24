# Write a function to convert temperature from Fahrenheit to Celcius.


def temp(fahren):
    return 5 * (fahren-32) /9

fahren = int(input("Enter temperature in Fahrenheit: "))
celcius = temp(fahren)
print(f"{round(celcius,2)}°C")