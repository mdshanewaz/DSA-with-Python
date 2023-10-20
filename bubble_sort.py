class BubbleSort:
    def solve(arr):

        print("Input : ", arr)

        n = len(arr)

        for i in range(0, n-1):
            for j in range(0, n-1-i):
                if arr[j] > arr[j+1]:
                    # temp = arr[j]
                    # arr[j] = arr[j+1]
                    # arr[j+1] = temp
                    arr[j], arr[j+1] = arr[j+1], arr[j]

            print(arr)

obj = BubbleSort
obj.solve([7, 3, 2, 11, 4, 6, 1, 5])

