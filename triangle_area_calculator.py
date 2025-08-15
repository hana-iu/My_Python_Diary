import math
try: 
  a = float(input("Enter the first triangle side: "))
  b= float(input("Enter the second side: "))
  c = float(input("Enter the third side: "))
  if a<0 or b<0 or c<0 : 
     print("Invalid input, please enter a positive number!")
  else: 
     if (a+b>c) and (a+c>b) and (c+b>a): 
       s = (a + b + c)/2
       area = math.sqrt(s*(s-a)*(s-b)*(s-c))
       print(f"The area of the triangle: {area:.2f}")
     else:
        print("Error: Invalid triangle sides (sum of any two sides must be greater than the third).")
        
except ValueError:
   print("Error: enter a valid number!")