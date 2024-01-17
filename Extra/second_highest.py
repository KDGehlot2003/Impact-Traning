x = input("Enter the numbers: ").split(" ")
# arr = []
# for i in x:
#     y = int(i)
#     arr.append(y)

# max_value = max(arr)

# ind = arr.index(max_value)

# arr.pop(ind)


# print("The second highest number is: ", max(arr))

m,sm = 0,0

for i in x:
    i = int(i)
    
    if i>m:
        sm = m
        m = i
print(sm)