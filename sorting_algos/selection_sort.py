class SelectionSort:
    def solve(arr):
        n = len(arr)
        for i in range(0, n):
            mini = i
            for j in range (i+1, n):
                if arr[mini] > arr[j]:
                    mini = j
                    
            arr[i], arr[min] = arr[min], arr[i]

        print(arr)

obj = SelectionSort
obj.solve([7, 3, 2, 11, 4, 6, 1, 5])