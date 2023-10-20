class InsertionSort:
    def solve(arr):
        
        for i in range(1, len(arr)):
            j = i

            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]

                j = j - 1

                # print(arr)
        
        print(arr)

obj = InsertionSort
val = [7, 3, 2, 11, 4, 6, 1, 5]
obj.solve(val)
