def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    print(arr)

arr = [7, 6, 5, 4, 3, 2, 1]
insertion_sort(arr)