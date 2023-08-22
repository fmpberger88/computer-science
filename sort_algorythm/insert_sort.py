def insertion_sort(arr):
    # Iterate from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
print("PRE SORT:", arr)
insertion_sort(arr)
print("POST SORT:", arr)
