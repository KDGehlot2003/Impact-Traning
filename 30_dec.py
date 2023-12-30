'''If using elif 

If all condition are false by default else block will be executed and writting else is always optional
'''

'''Read a character from user whether it is Uber case character or lower case character or is it a special character'''

# x = input("Enter the Character: ")

# if x.isupper():
#     print("Upper_case")
# elif x.islower():
#     print("Lower_case")
# elif x.isdigit():
#     print("Digit")
# else:
#     print("Special Character ")


'''Give Discount to Customer...'''

# name = input("Enter your name: ")
# amount = int(input("Enter the total bill Amount: "))

# if amount>=4000:
#     print("You Will get 4% Discount...")
#     print(amount-amount*4/100)
# elif amount>=3000:
#     print("You Will get 3% Discount...")
#     print(amount-amount*3/100)
# elif amount>=2000:
#     print("You Will get 2% Discount...")
#     print(amount-amount*2/100)
# elif amount>=1000:
#     print("You Will get 1% Discount...")   
#     print(amount-amount*1/100)        
# elif amount<1000:
#     print("You get no discount...")


'''Nested If Conditon : if condition in another if condtion 

    In Nested idf we have outer if conditon and inner if condition 
    if  outer if condition is true then only we check the inner if condition'''

'''WAP to read name of the student and roll no and subject if student is pass in all subject cal* the grade of the student.'''


# name = input("Enter the name: ")
# roll = int(input("Enter the Roll no: "))
# s1,s2,s3 = map(int,input("Enter the Marks of the subject: ").split(","))

# if s1>=35 and s2>=35 and s2>=35:
#     avg= (s1+s2+s3)*100/300
#     print("Percentage: ",avg)
#     if(avg>=60):
#         print(name," First Class Pass.")
#     elif(avg>=50):
#         print(name, " Second Class Pass.")
#     else:
#         print("Just Pass...")
# else:
#     print("Fail...")

'''WAP to read a number from the user and check whether is divisible by 3 and 5'''

# number = int(input("Enter the number: "))

# d3 = number %3 == 0
# d5 = number % 5 == 0

# if d3:
#     if d5:
#         print("The number is divisible by both 3 and 5...")
#     else:
#         print("The number is only dividible by 3.")
# else:
#     if d5:
#         print("The number is only divisible by 5.")
#     else:
#         print("The number is not divisible by both 3 and 5.")


'''strings:

1)It is a collection of char (or) array of characters 2)string indexing starts from zero and end with n-1

3)we can find length of the string using len function

4) We can declare strings in 3 ways

1)single quotes

2)Double quotes

3) Triple quotes

-->string supports both positive and negative indexing. *Positive indexing starts from zero and end with n-1

*Negative indexing starts from -1 and end with -(n+1)

string indexing:Accessing a char from string.

slicing:Accessing sub string or set of characters in string
'''

# s = "lokesh it"
# print(s[2])
# print(s[5])
# print(s[2:5])
# print(s[3:8])
# print(s[2:])
# print(s[:6])
# print(s[::1])
# print(s[::2])
# print(s[::1][::2])
# print(s[::1][::3])
# print(s[7:3])
# print(s[-2:-5])
# print(s[-2:-5:-1])
# print(s[2:-2])
# print(s[:-5])

'''
s = "Rohith"
r = 1
"ohitihR"


s = "Rohith"
r=2
"htihoR"
'''

# s = "Rohith"
# # r=1
# # print(s[r:]+s[:r])
# r = 2
# print(s[-r:]+s[:-r])

# arr = [1,2,3,4,5]
# x = int(input())
# print(*(arr[-x:]+arr[:-x]))


# n = int(input())
# l = list(map(int,input().split()))[:n]
# r = int(input())
# d=[]
# d=l[-r:]+l[:-r]
# print(*d)


'''
Python Programming Support 2 types of control statements:
    for loop
    while loop

For loop:
        for loop is applicale for iterable object only 
    iterable : The object which contains sequence of elements
        Ex: all collections,list,tuple,dict,set and string
    we can't apply for loop on non iterable objects 
        Ex: all Fundamental datatypes except string
    
'''

# s = "Krishna"
# for p in s:
#     print(p,end=" ")
# print()
# l = [2,4,6,8,10]
# for p in l:
#     print(p,end=" ")
# print()
# for p in range(len(l)):
#     print(p,l[p])
# for p in range(1,11):
#     print(p,end=" ")
# print()
# for p in range(2,21,2):
#     print(p,end=" ")
# print()


'''TCS Question'''
s = input()
s.lower()
r= ''
for p in range(97,123):
    d = chr(p)
    if d not in s:
        r = r+d
print(r)

# lst = list(input().split(" "))

# for i in lst:
#     print(i[::-1],end=" ")
    
# WAP a program to print prime number from 1 to 50

# for p in range(2,51):
#     c = 0 
#     for q in range(1,p+1):
#         if(p%q==0):
#             c = c+1
#     if c==2:
#         print(p,end=" ")

# WAP to print perfect number from 1-100
# total = 0

# for q in range(1,p):
#     if(p%q==0):
#         total = total + q
# if total==p:
#     print(p,"is Perfect Number.")
# else:
#     print(p,"is Not a Perfect Number.")


# num = input()
# r = ''
# for i in num:
#     i = int(i)
#     if i%2!=0:
#         v = i*i
#         r = r + str(v)
# print(r)


# i = 1
# while(i<=10):
#     print(i)
#     i = i+1
# i =1 
# while(i<=10):
#     if(i%2==0):
#         print(i)
#     i=i+1

'''WAP to print sum of digit'''

# n = int(input("Enter number: "))
# s = 0
# while(n!=0):
#     r = n%10
#     s = s + r
#     n = n//10
# print(s)

'''WAP to check the number is palindrome or not.'''

n = input("Enter the number: ")

if n[:]==n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#89---> Disarium number  9^2 + 8^1 = 81 +9 = 89
    # 175---> 5^3 + 7^2 + 1^1 = 125+49+1 =175
    
n = int(input())
