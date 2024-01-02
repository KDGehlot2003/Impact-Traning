n = int(input())
l = []
count = 0
for i in range(0,n):
    l.append(input())
for i in l:
    if int(i[-4:-2]) >= 60:
        count += 1
print(count)