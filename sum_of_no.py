# Write a Program to read n values at a time and print its sum.

x = input("Enter the numbers: ").split(" ")

total = 0 
for i in x:
    total = int(total) + int(i)

print("The sum of numbers are: ",total)

