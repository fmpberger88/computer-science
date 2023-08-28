"""
The naive solution has a quadratic runtime, but it’s possible to solve this problem in O(n) time by using two pointers.
The pointers will start at each end of the array and move towards each other.
The two-pointer approach is a common approach for problems that require working with arrays,
as it allows you to go through the array in a single loop and without needing to create copy arrays.
"""

def efficient_solution(heights):
    total_water = 0
    left_pointer = 0
    right_pointer = len(heights)-1
    left_bound = 0
    right_bound = 0

    while left_pointer < right_pointer:
        if heights[left_pointer] <= heights[right_pointer]:
            left_bound = max(heights[left_pointer], left_bound)
            total_water += left_bound - heights[left_pointer]
            left_pointer += 1
        else:
            right_bound = max(heights[right_pointer], right_bound)
            total_water += right_bound - heights[right_pointer]
            right_pointer -= 1

    return total_water



