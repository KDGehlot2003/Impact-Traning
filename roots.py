# Write a Program to find roots of qudratic equation

import math

a = int(input("Enter the Queficent of X^2: "))
b = int(input("Enter the Queficent of X: "))
c = int(input("Enter the Constant: "))

D = math.sqrt(b*b - 4*a*c)

x1 = (-b + D)/2*a

x2 = (-b - D)/2*a

print("The roots of Qudratic Eq are: ",x1," and ",x2)

