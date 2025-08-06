try:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f}")  # Rounds to 2 decimal places
except ValueError:
    print("Error: Please enter a valid number.")