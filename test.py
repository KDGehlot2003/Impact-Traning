if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    lst = []
    for i in arr:
        i = int(i)
        lst.append(i)
    max_val=max(lst)
    lst.remove(max_val)
    print(max(lst))

    # print(max_val)
    # lst = []
    # for i in arr:
    #     lst.append(i)
    # print(lst)
    # print(type(lst))
    # print(arr)
    # print(type(arr))
    # # print(max(arr))
    # print(arr)
