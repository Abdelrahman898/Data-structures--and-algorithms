
# 2. Bubble Sort

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [74, 8, 49, 1, 666, 55, 8888, 2, 10]
print(BubbleSort(arr))   # time complexity = O(n^2)


# OR
def BubbleSort(arr):
    n = len(arr)
    premutation = True
    while premutation:
        premutation = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                premutation = True
    return arr

print(BubbleSort(arr))   # time complexity = O(n^2)




