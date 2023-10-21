def MergeSort(arr):
    if len(arr) > 1:
        arrL = arr[:len(arr)//2]
        arrR = arr[len(arr)//2:]

        MergeSort(arrL)
        MergeSort(arrR)

        i =0
        j = 0
        k = 0

        while i < len(arrL) and j < len(arrR):
            if arrL[i] < arrR[j]:
                arr[k] = arrL[i]
                i = i+1
            else:
                arr[k] = arrR[j]
                j += 1
            k += 1
                
        while i < len(arrL):
            arr[k] = arrL[i]
            i += 1
            k += 1
            
        while j < len(arrR):
            arr[k] = arrR[j]
            j += 1
            k += 1

    return arr

val = [7, 3, 2, 11, 4, 6, 1, 5]
print(MergeSort(val))