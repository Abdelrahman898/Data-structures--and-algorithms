
# Searching Algorithms


# 2. Binary Search  [sorted array]

# with recursion
def BinarySearch(arr, star, end, target):
    if end >= star:
        mid = (int((star + end) // 2))
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return BinarySearch(arr, star, mid - 1, target)
        else:
            return BinarySearch(arr, mid + 1, end, target)
        
    else:
        return -1
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(BinarySearch(arr, 0, len(arr) - 1, 5))   # time complexity = O(log n)


# without recursion

def BinarySearch(arr, target):
    star = 0
    end = len(arr) - 1
    
    while star <= end:
        mid = (int((star + end) // 2))
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            star = mid + 1
    else:
        raise ValueError('Element not found')

print(BinarySearch(arr, 5))   # time complexity = O(log n)
print(BinarySearch(arr, 11))   




# bisection search algorithm (binary search)

cupe = 27
epsilon = 0.01
low = 0.0
high = cupe
num_guesses = 0

guess = int(input(f"Please guess a number between {low} and {high}: "))


while abs(guess**3 - cupe) < epsilon:
    if guess**3 < cupe:
        low = guess

    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cupe)



def unisearch(arr, low, high):
    mid = (high + low) // 2

    if mid > arr[mid-1] and mid > arr[mid+1]:
        return mid   # this is the highest point of the reversed U shape

    elif mid > arr[mid-1]:
        return unisearch(arr, low, mid - 1)

    else:
        return unisearch(arr, mid + 1, high)
