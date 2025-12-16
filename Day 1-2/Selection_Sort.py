def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        min_index = i
        for j in range(i, len(arr)):
            if arr[j]<min:
                min = arr[j]
                min_index = j
            temp = arr[i]
            arr[i] = min
            arr[min_index] = temp
    return arr


print(selectionSort([1,2,4,5,3,7,8]))
