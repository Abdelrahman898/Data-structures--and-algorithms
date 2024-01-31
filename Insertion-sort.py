
# 3. Insertion Sort

def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            
    return arr
    
arr = [74, 8, 49, 1, 666, 55, 8888, 2, 10]
print(InsertionSort(arr))   # time complexity = O(n^2)



