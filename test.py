if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    # print(arr)
    min_val = min(arr)
    # print(min_val)
    arr.remove(min_val)
    # print(arr)
    min_val = min(arr)
    arr2 = []
    for i in arr:
        # print(i[1])
        # print(min_val[1])
        if i[1]== min_val[1]:
            arr2.append(i[0])
    arr2.sort()
    print(arr2)
    for i in arr2:
        print(i)