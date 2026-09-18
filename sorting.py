def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 1. Take input as a string, split by spaces, and convert to integers
user_input = input("Enter numbers separated by spaces: ")
data = [int(x) for x in user_input.split()]

# 2. Sort and print
print("Sorted array:", selection_sort(data))