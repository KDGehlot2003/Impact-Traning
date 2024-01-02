# 02/01/2024

"""
# Write program to read list elements from the user, with and without for loop
l = list(map(int, input().split()))
print(l)

# OR you can do this...
n = int(input())
a = list(map(int, input().split()))[:n]
print(a)

# OR you can do this...
n = int(input())
r = []
for p in range(n):
    r.append(int(input()))
print(r)


# Print (min, max, next min, next max,...)
# Input: [5,2,3,4,6,5,-2]
# Output: [-2,6,2,5,5,4]
n = int(input())
a = list(map(int, input().split()))[:n]
ans = []
a.sort()
print(a)
for p in range(len(a)//2):
    ans.append(a[p])
    ans.append(a[-(p + 1)])
if len(a) % 2 != 0:
    ans.append(a[len(a) // 2])
print(*ans)


# Print given string as output without duplicate elements, without using remove(), pop(), del or set
n = int(input())
a = list(map(int, input().split()))[:n]
ans = []
for i in a:
    if i in ans:
        continue
    ans.append(i)
print(*ans)

# HackerRank Question
# Mimic operations
# Make output: ['1','3','2']
n = int(input())
ans = []
i = 1
while i <= n:
    cmd = input("Enter operation: ")
    s = cmd.split()
    if s[0] == "append":
        b = int(s[1])
        ans.append(s[1])
    elif s[0] == "insert":
        b = int(s[1])
        c = int(s[2])
        ans.insert(b, c)
    elif s[0] == "print":
        print(ans)
    i += 1


# Mimic operations (more...)
n = int(input())
ans = []
i = 1
while i <= n:
    cmd = input("Enter operation: ")
    s = cmd.split()
    if s[0] == "append":
        b = int(s[1])
        ans.append(s[1])
    elif s[0] == "insert":
        b = int(s[1])
        c = int(s[2])
        ans.insert(b, c)
    elif s[0] == "print":
        print(ans)
    elif s[0] == "pop":
        ans.pop()
    elif s[0] == "reverse":
        ans.reverse()
    elif s[0] == "remove":
        b = int(s[1])
        ans.remove(6)
    elif s[0] == "sort":
        ans.sort()          // Check here
    i += 1


# Accenture Question
# Given n = 2
# If digit is odd, print as it is in front, after that print even digits in reverse of their occurrence
# Input: 2143658790
# Output:1357908642

num = int(input())
l = list(map(int, str(num)))
o = []
e = []
for i in l:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
e.reverse()
r = list(map(str, o + e))
print(''.join(r))

OR you can do this...
# num = int(input())
num = 2143658790
l = list(map(int, str(num)))
o = []
e = []
a = [o.append(p) if p%2!=0 else e.append(p) for p in l]
o.sort()
e.sort(reverse=True)
r = list(map(str, o + e))
print(''.join(r))


# Logic: (sum of fibonacci elements) + (first position element of string) + (first position number of fibonacci) + (...
# Input: abcde
# Output: 12a1b1c2d3e5
string = input()
length = len(string)
fibonacci = [1, 1]
ans = ''
while len(fibonacci) < length:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
for i in range(0, length):
    ans += string[i] + str(fibonacci[i])
print(str(sum(fibonacci)) + ans)


# [1,2,3,4,3,5,3,7,3]
# Remove '3' by writing "remove()" only one time
# If any other number has duplicate, don't remove it
l = [1, 2, 3, 4, 3, 4, 5, 3, 7, 3]
count = 0
ans = []
for i in l:
    if i == 3:
        if 3 not in ans:
            ans.append(i)
    else:
        ans.append(i)
print(ans)


# Input:
# 5
# 7868190130M2522
# 5303914400F3211
# 9273338290F4010
# 2921522980M6544
# 1313579440F2036
# Output: 1
# Explanation: A person with a mobile number 2921522980 is having age above or equal to 60

n = int(input())
l = []
count = 0
for i in range(0,n):
    l.append(input())
for i in l:
    if int(i[-4:-2]) >= 60:
        count += 1
print(count)
"""
