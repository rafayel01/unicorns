def fahrenheit_to_celsius(num):
    return (num - 32) / 1.8

f = float(input("Enter a degree of fahrenheit: "))
print(f'Celsius: {fahrenheit_to_celsius(f)}')
