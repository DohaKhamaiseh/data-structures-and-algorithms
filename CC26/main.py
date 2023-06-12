def insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
         i += 1
    while i < len(sorted):
         temp = sorted[i]
         sorted[i]=value
         value = temp
         i += 1
    sorted.append(value)

def insertSort(inputted_array):
    sorted = []
    sorted.append(inputted_array[0])
    for i in range(1, len(inputted_array)):
        insert(sorted, inputted_array[i])
    return sorted

l = [8, 4, 23, 42, 16, 15]
print(insertSort(l))
