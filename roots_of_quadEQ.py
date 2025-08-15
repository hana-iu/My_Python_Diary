import math
a = float(input("Enter the value of the leading cofficient(a): "))
b = float(input("Enter the value of the linear cofficient(b): "))
c = float(input("Enter the value of the constant term(c): "))
D = b**2 - (4*a*c)
if D>0: #two real roots
   root_1 = ((-b) + math.sqrt(D)) / (2*a)
   root_2 = ((-b) - math.sqrt(D)) / (2*a)
   print ("The first root of the quadratic equation: ", root_1)
   print("The second root of the quadratic equation: ", root_2)
elif D==0: # One real root
   root = (-b) / (2*a)
   print(f"Single real root: {root}")
else: #complex roots (D <0)
   real_part = -b / (2*a)
   imag_part = math.sqrt(-D) / (2*a)
   print(f"Complex roots: {real_part} +{imag_part}i, {real_part} - {imag_part}i")
