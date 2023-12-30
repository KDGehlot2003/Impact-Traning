x = input("Enter the number: ").split(" ")

m,sm = 0,0

for i in x:
    i = int(i)
    if i<m:
        sm = m
        m = i

print(sm)
