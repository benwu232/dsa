
def quick_sort(a, start, end):
    if start >= end:
        return
    pivot = a[end]
    pivot_idx = start
    for k in range(start, end):
        if a[k] <= pivot:
            a[pivot_idx], a[k] = a[k], a[pivot_idx]
            pivot_idx += 1
    a[end] = a[pivot_idx]
    a[pivot_idx] = pivot
    # a[pivot_idx], a[end] = a[end], a[pivot_idx]
    quick_sort(a, start, pivot_idx-1)
    quick_sort(a, pivot_idx+1, end)



if __name__ == '__main__':
    # a = [1, 9,8,7,6,5,4,3,2,1,0]
    # print(a)
    a = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    ]

    for l in a:
        quick_sort(l, 0, len(l)-1)
        print(l)