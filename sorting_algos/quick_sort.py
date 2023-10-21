def QuickSort(arr):
    n = len(arr)

    if n <= 1:
        return(arr)
    else:
        pivot = arr.pop()
    arrL = []
    arrR = []

    for i in range(0, n-1):
        if pivot > arr[i]:
            arrL.append(arr[i])
        else:
            arrR.append(arr[i])

    return QuickSort(arrL) + [pivot] + QuickSort(arrR)

obj= QuickSort([7, 3, 2, 11, 4, 6, 1, 5])
print(obj)
