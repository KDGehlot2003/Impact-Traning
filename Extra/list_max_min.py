# Write a Program to read n values seperated with (,) and find the largest and smallest among the element.

x = input("Enter the number: ").split(",")
lst = []
for i in x:
    n = int(i)
    lst.append(n)

print("The largest number is ",max(lst)," and smallest number is ", min(lst))