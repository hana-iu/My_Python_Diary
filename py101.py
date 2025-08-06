import math
try: 
    radius = float(input("Enter the radius of the circle: "))
    if radius <0: 
        print("Error: Radius cannot be negative")
    else:
        area = math.pi * radius**2
        circumference = 2 * math.pi * radius 
        print(f"The circle's area: {area:.2f} square units")
        print(f"The circle's circumference: {circumference:.2f} square units")
except ValueError: 
    print("Error:Please enter a valid number")
