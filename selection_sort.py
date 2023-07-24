
def selection_sort(a):
    for j in range(len(a)-1):
        min = j
        for k in range(j+1, len(a)):
            if a[min] > a[k]:
                min = k
            tmp = a[min]
            a[min] = a[j]
            a[j] = tmp
    return a


if __name__ == '__main__':
    a = [9,8,7,6,5,4,3,2,1,0]
    print(a)

    b = selection_sort(a)
    print(b)