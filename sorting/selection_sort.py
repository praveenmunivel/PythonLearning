num = [5,2,3,8,10,11]
# Find the minimum element in the unsorted array and swap it with element at beginning
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # Find the minimum element
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection_sort(num))