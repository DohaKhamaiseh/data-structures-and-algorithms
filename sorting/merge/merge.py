def Mergesort(arr):
    if len(arr)==0:
        return []
    
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        Mergesort(left)
        Mergesort(right)
        Merge(left, right, arr)

    return arr


def Merge(left, right, arr):
    i, j, k = 0, 0, 0

    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # print(left)
    # print(right)
    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]


arr = [8, 4, 23, 42, 16, 15]
print(Mergesort(arr))
