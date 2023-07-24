
def merge_sort(array):
    if len(array) > 1:
        # get the middle index
        mid = len(array) // 2
        # divide the array into two parts
        left_array = array[:mid]
        right_array = array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        # select the smaller one from left_array and right_array, move it to array, and modify the index
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        
        # if not finished, continue moving elements of left_array to array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        # if not finished, continue moving elements of right_array to array
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

if __name__ == '__main__':
    a = [9,8,7,6,5,4,3,2,1,0]
    print(a)

    merge_sort(a)
    print(a)