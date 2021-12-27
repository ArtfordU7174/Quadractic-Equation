import cmath

print("\n*************** PROGRAM TO FIND THE ROOTS OF A QUADRACTIC EQUATION*************\n\n")
print("Equation of the form: ax^2 + bx +c = 0 \n\n")

#Input the value of the coefficient
a = float(input("\nEnter the value of a: "))
b = float(input("\nEnter the value of b: "))
c = float(input("\nEnter the value of c: "))

d = (b**2 - 3*a*c)
D = cmath.sqrt(d)

if d > 0:
  print("\n The roots of the equation are distinct ")

elif d == 0:
  print("\n The roots of the equation are equal ")

else: 
  print("\n The roots of the equation are complex")

x1 = (-b + D)/(2*a)
x2 = (-b - D)/(2*a)

#Display the results
print("\n The roots of the equation are: \n")
print ("x1 = {0}".format(x1))
print ("x2 = {0}".format(x2))

input("\n\nPress <Enter> to exist....")