def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temperatures = [0, 20, 37, 100]
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))
print(fahrenheit_temperatures)