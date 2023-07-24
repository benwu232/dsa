def bubble_sort(a):
    for j in range(len(a)-1):
        for k in range(len(a)-2-j):
            if a[k] > a[k+1]:
                tmp = a[k]
                a[k] = a[k+1]
                a[k+1] = tmp
    return a


if __name__ == '__main__':
    a = [9,8,7,6,5,4,3,2,1,0]
    print(a)

    b = bubble_sort(a)
    print(b)