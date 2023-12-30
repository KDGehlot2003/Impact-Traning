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
    