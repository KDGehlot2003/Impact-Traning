if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([score,name])
    arr.sort()
    arr.remove(min(arr))
    print(arr)
    min_val = min(arr)
    min_score = min_val[0]
    print(min_score)
    marks = []
    i_marks = []
    for p in arr:
        marks.append(p[0])
    print(marks)
    for p in marks:
        if (min(marks)==p):
            i_marks.append(marks.index(p))
    print(i_marks)
    # min_val = min(arr)
    # # print(min_val)
    
    # # print(arr)
    # min_val = min(arr)
    # arr2 = []
    # for i in arr:
    #     # print(i[1])
    #     # print(min_val[1])
    #     if i[1]== min_val[1]:
    #         arr2.append(i[0])
    # arr2.sort()
    # # print(arr2)
    # for i in arr2:
    #     print(i)