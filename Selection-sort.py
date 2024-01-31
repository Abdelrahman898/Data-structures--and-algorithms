
# Sorting Algorithms


# 1. Selection Sort

def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        print(f"min_index = {min_index}")
        print(arr)
        
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"sorted min_index = {min_index}")
                print(arr)
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"{arr[i]} and {arr[min_index]}")
        print(arr)
        
    return arr

arr = [74, 8, 49, 10]
print(SelectionSort(arr))   # time complexity = O(n^2)


