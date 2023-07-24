def insert_sort(a):
    for j in range(1, len(a)):
        tmp = a[j]
        for k in range(j-1, -1, -1):
            if a[k] > tmp:
                a[k+1] = a[k]
        a[k] = tmp
    return a


if __name__ == '__main__':
    a = [9,8,7,6,5,4,3,2,1,0]
    print(a)

    b = insert_sort(a)
    print(b)