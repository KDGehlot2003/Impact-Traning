# 01/01/2024

"""
STRING METHODS

a = "Rohan Luhar"
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isalnum())

b = "12345"
print(a.isdigit())

s = "Rohan123"
print(s.isalnum())

# Take an alphanumeric string and create a string as a combination of indices of integers
num = input()
out = ''
count = 0
for i in num:
    if i.isdigit():
        out += str(count)
    count += 1
print(out)

OR you can do this...
num = input()
ans = ''
for i in range(len(num)):
    if num[i].isdigit():
        ans += str(i)
print(ans)

# In an alphanumeric string, alphabets are reversed and integers remains at same position
s = input()
r = ''
for i in s:
    if i.isalpha():
        r = r + i
r = r[::-1]
result = ''
j = 0
for i in s:
    if i.isalpha():
        result = result + r[j]
        j += 1
    else:
        result += i
print(result)

# Count of special characters in a string
s = input()
count = 0
for i in s:
    if i.isdigit() or i.isalnum() or i.isspace():
        continue
    else:
        count += 1
print(count)

list = ['a', 'e', 'i', 'o', 'u']
# print(list[2])
res = ''
s = input()
for i in s:
    if i in list:
        if i == 'u':
            index = 0
        else:
            index = list.index(i) + 1
        res = res + list[index]
    else:
        res = res + i
print(res)

COLLECTIONS
    Python supports 4 types of collections
        1. List
        2. Tuple
        3. Set
        4. Dictionary
    All collection objects are used to store multiple values in a single variable

LISTS
    It can be created using [] or by calling the 'list' function
    It is a mutable object i.e. we can update the elements of list
    Insertion order is preserved
    Duplicate elements are allowed
    List is a collection of homogeneous and heterogeneous elements
    It supports both indexing and slicing

NESTED LIST
    A list in the another list

LIST COMPREHENSION
    Using the list comprehension, we can reduce number of lines in our code
    The concept of generating element into list object by writing some logic in the list, is known as List comprehension

# Declaration of List
l = []
print(type(l))
s = list()
print(type(s))

a = list(range(1, 10))
print(a)
print(len(a))
print(id(a))
a[5] = 58
print(id(a))

b = list(range(10, 110, 10))
print(b)
print(b[2:5])
print(b[3])
print(b[-5:-2])

# while loop in list
l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
    print(l[i], end=" ")
    i += 1
print()

# for loop in list
for p in l:
    print(p, end=" ")
print()
for p in range(len(l)):
    print(l[p], end=" ")
print()


LIST METHODS
    append()   -> Add element at the end (only one element at a time)
    insert()   -> Add element at specific position
    extend()   -> Add multiple elements at the end
    copy()     -> Copy elements of one list into another
    count()    -> Returns how many times a corresponding element is repeated
    index()    -> Finds index position
    remove()   -> Removes element based on values
    del, pop() -> Removes element using index
    sort()     -> Arrange elements in ascending order
    reverse()  -> Arrange elements in descending order
    clear()    -> Clears all elements of list

# List methods
print(max(l))
print(min(l))
print(sum(l))
avg = sum(l)/len(l)
print(avg)

l = [10, 20, 30, 40, 50, 60, 70, 80]
l.append(80)
print(l)
l.extend([90, 100, 110])
print(l)
l.insert(2, 25)
print(l)
y = l.copy()
print(y)
l.remove(80)
print(l)
l.pop()
print(l)
del l[2]
print(l)
del l[2:5]
print(l)
print(l.index(80))
print(l.index(80, 2))          # Searches for '80' starting from index-2 of list
print(l.index(90,2,5))  # Searches for '90' starting from index-2 and stops searching at index-4
                                             # This throws 'ValueError'
l.insert(5, 20)
print(l.count(20))
l.insert(1, 152)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
l.clear()
print(l)
print(y)
y[2:5] = [1, 2, 23]
print(y)

# Take an integer as input, sort the digits in descending order and print digits-sorted integer
num = int(input())
l = list(map(int, str(num)))
l.sort(reverse=True)
print(l)                    # list of integers
# print(''.join(l))         # join() is not applicable for int elements
r = list(map(str, l))       # list of integer-elements can't be converted into single string
print(r)                    # list of strings
print(str(r))               # no changes; list of strings; no use
print(''.join(r))           # converts list of string-elements into single string

# Take an integer as input, sort it in ascending order and print an integer not having '0' as first element
num = int(input())
l = list(map(int, str(num)))
l.sort()
i = 0
while l[0] == 0:
    l[0], l[i] = l[i],l[0]
    i += 1
    # temp = l[1]
    # l[1] = l[0]
    # l[0] = temp
r = list(map(str, l))
print(''.join(r))

# Inout: [1, 2, 3, "krishna", "ramu", "anil", "saritha", 7, 10]
# Output: [1, 2, 3, 7, 10, "anil", "krishna", "ramu", "sarithi"]
l = [1, 2, 3, "krishna", "ramu", "anil", "saritha", 7, 10]
digits = []
strings = []
for i in l:
    if isinstance(i, int):
        digits.append(i)
    else:
        strings.append(i)
digits.sort()
strings.sort()
print(digits + strings)
"""

l = [1, 2, 3, "krishna", "ramu", "anil", "saritha", 7, 10]
l.sort()
print(l)
# ans = ''
# # print(l.pop(1))
# for i in l:
#     if isinstance(i, int):
#         ans.append(i)
#         l.remove(l)
# ans
# ans = []
# for i in l:
#     if isinstance(i, int):
#         print("Index: ", l.index(i))
#         ans.append(l.pop(l[l.index(i)]), 'x')
#         print("l: ", l)
#         print("Ans: ", ans)
# print(ans)
