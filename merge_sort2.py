
def merge(a, start, mid, end):
    b = [0 for k in range(len(a))]
    left = start
    right = mid
    for k in range(start, end):
        if a[left] < a[right]:
            b[k] = a[left]
            left += 1
        else:
            b[k] = a[right]
            right += 1
    a[start:end] = b

def merge_sort(a, start, end):
    if start > end:
        return 
    if start == end - 1:
        tmp = a[start]
        a[start] = a[end]
        a[end] = tmp
    else:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid, end)
        merge(a, start, mid, end)

if __name__ == '__main__':
    a = [9,8,7,6,5,4,3,2,1,0]
    print(a)

    merge_sort(a, 0, len(a))
    print(a)