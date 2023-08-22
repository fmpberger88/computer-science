def selection_sort(arr):
    # Iterate through the entire array
    for i in range(len(arr)):
        # Assume the minimum value is the current value
        min_idx = i

        # Iterate through the unsorted part of the array
        for j in range(i + 1, len(arr)):
            # If a smaller value is found, update the index of the minimum value
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum value with the current value
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
