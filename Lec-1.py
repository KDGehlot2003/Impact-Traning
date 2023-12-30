"""
Take input from keyboard
n = input("Enter a string: ")
print(n)

Take two integer input using type conversion
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print(a, " ", b)

Take two integer input using a single line of coding
a, b = map(int, input("Enter teo numbers: ").split(" "))
print(a," ",b)
"""
# ============================================================
"""
OPERATORS
Operator is a special kind of symbol and it performs specific operation
Operators are categorized into 6 types:
1.Arithmetic Operator
2.Relational Operator
3.Logical Operator
4.Bitwise operator
5.Special Operator
    Python supports 3 types of special operators:
        1.Membership Operator
        2.Identity Operators
        3.Walrus Operator
        
    1.Membership
        Used for comparison or searching related operations.
        Two types of Membership function:
            in, not in

a = "krishna"
print('r' in a)
print('f' in a)
a = [1, 2, 3, 4, 5]
print(4 in a)
print(6 not in a)
print(7 in a)

Read 2 numbers and find maximum
a, b = map(int, input("Enter two numbers: ").split(" "))
if a > b:
    print("a is max")
else:
    print("b is max")
    
# Write a program to read a character from the user, and check whether it is a vowel or consonant
a = input("Enter a character: ")
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print("Vowel")
else:
    print("Consonant")

# OR..., You can write this way:

ch = input("Enter a character: ")
v = "aeiou"
if ch in v:
    print("Vowel")
else:
    print("Consonant")


        2.Identity
            Used for comparing the address
            Two types: is, is not
            
a = 10
b = 10
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
a=10
b=20
print(a is b)

        3.Walrus
            Used to reduce number of lines in our code
            It is introduced from Python 3.8 version

# Without Walrus
a, b = 3, 2
a1 = a ** 2
b1 = b ** 2
c1 = 2 * a * b
c = a1 + b1 + c1
print(a1, b1, c1, c)

# Using Walrus
a, b = 1, 2
c = ((a1 := a ** 2) + (b1 := b ** 2) + (c1 := a * b * 2))
print(a1, b1, c1, c)

# Write a program to read 2 numbers and perform addition operation in a single line using Walrus, without using split()
print((a:=int(input()))+(b:=int(input())))

6.Conditional Operator
    It requires 3 arguments: Left-side, middle-side, and right-side arguments
    Middle-side is a condition
    If a condition is evaluated as true, then left-side argument will return value
    If the condition is evaluated as false, then right-side argument will return value
    Using the condition operator, we can reduce number of lines in our code

Ques: Does difference number of lines in python affect the complexity or not?    

# Read 2 numbers and find maximum
a, b = map(int, input("Enter two numbers: ").split())
print("a is max") if (a > b) else print("b is max")

# Read 3 numbers and find max
a, b, c = map(int, input("Enter three numbers: ").split())
print("a,b,c are equal") if (a == b and b == c) else (print("a is max") if (a > c) else print("c is max")) if (
            a > b) else (print("b is max") if (b > c) else print("c is max"))

# Replace the character which has maximum count in a string
def frequent_character_replace(string, X):
    counted = {e: string.count(e) for e in set(string)}
    Y = counted.keys(max(counted.values()))
    return Y

ans = frequent_character_replace("bbadbbababb", "t")
print(ans)
""" 
