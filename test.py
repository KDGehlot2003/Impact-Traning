# Input:
# UDDLLRUUUDUURUDDUULLDRRRR
# 5
# 5
# 2
# 2 2
# 3 3


s = input()
row = int(input())
col = int(input())

o = int(input())

ob1 = list(map(int, input().split()))
ob2 = list(map(int, input().split()))

ele = 0
l=[]
for _ in range(row):
    
    a = []
    for _ in range(col):
        ele += 1
        a.append(ele)
    l.append(a)
    

for i in l:
    print(i)

i = j = 0

for mom in s:
    if i!=ob1[0] or j!=ob1[1] and i!=ob2[0] or j!=ob2[1]:
        if mom=="U":
            i -= 1
        elif mom=="D":
            i += 1
        elif mom=="L":
            j -= 1
        elif mom=="R":
            j += 1
    


print("Final position of the robot: ({}, {})".format(abs(j),abs(i)))
