#print the right angle triangle in reverse

n = int(input("Enter the number: "))

for i in range(n):
    for j in range(i+1,n):
        print("* ",end=" ") # end next print ko ek hi line me print karata h
        
    print()