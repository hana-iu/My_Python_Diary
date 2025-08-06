try:
    centigrade = float(input("Enter the temperature in centigrade: "))
    fahrenheit = (centigrade*9/5) +32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
except ValueError:
    print("Error: Please Enter a valid number.")

