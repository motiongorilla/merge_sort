arr = [12, 11, 13, 5]
# [12, 11, 13, 5, 6, 10, 78, 101, 7, 15, 22, 23, 34, -1, -5, 55, 12, 241]
def sort(to_sort):
    if len(to_sort) > 1:
        l_arr = to_sort[:len(to_sort)//2]
        r_arr = to_sort[len(to_sort)//2:]

        # recursion
        sort(l_arr)
        sort(r_arr)
        
        # merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                to_sort[k] = l_arr[i]
                i += 1
            else:
                to_sort[k] = r_arr[j]
                j += 1
            k += 1
        
        while i < len(l_arr):
            to_sort[k] = l_arr[i]
            i += 1
            k += 1
        
        while j < len(r_arr):
            to_sort[k] = r_arr[j]
            j += 1
            k += 1

    return print(to_sort)

sort(arr)