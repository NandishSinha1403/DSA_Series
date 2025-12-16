from math import inf
def Merge(a, b):
    arrm = []
    l = r = 0

    while l < len(a) and r < len(b):
        if a[l] <= b[r]:
            arrm.append(a[l])
            l += 1
        else:
            arrm.append(b[r])
            r += 1
    arrm.extend(a[l:])
    arrm.extend(b[r:])
    return arrm

def MergeSort(arr):
    if len(arr)==1:
        return arr
    q = len(arr) // 2
    left_half = arr[:q]
    right_half = arr[q:]

    arr1 = MergeSort(left_half)
    arr2 = MergeSort(right_half)
    return Merge(arr1,arr2)

arr= [1,5,6,4,3,2]
print(MergeSort(arr))
