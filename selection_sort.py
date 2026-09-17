def selection_sort(arr):
    n = len(arr)
    
    # We only need n-1 passes
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: 
                min_idx = j
                
        # Swap the elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Print the array after every pass
        print(f"Pass {i + 1}: {arr}")
        
    return arr

# 1. Take input
user_input = input("Enter numbers separated by spaces: ")
data = list(map(int, user_input.split()))

print(f"\nOriginal array: {data}\n")

# 2. Sort and show passes
sorted_data = selection_sort(data)

# 3. Show final results
print(f"\nFinal Sorted array: {sorted_data}")
print(f"Total number of passes: {len(data) - 1}")