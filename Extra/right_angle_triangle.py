# Write a program to take the sides of the triangle as a input and check whether it is right angle or not.

height = int(input("Enter the height of the triangle: "))
Base = int(input("Enter the Base of the triangle: "))
X = int(input("Enter the hipo of the triangle: "))


if X*X == height*height + Base*Base:
    print("Right angle Triangle... ")
else:
    print("Not Right Angle Triangle. 😔")