"""
The naive solution to the problem is to:

Traverse every element in the array
Find the highest left bound for that index
Find the highest right bound for that index
Take the lower of those two values
Subtract the height of that index from that minimum
Add the difference to the total amount of water

bigO = O(n^2)
"""

def naive_solution(heights):
  total_water = 0
  for i in range(1, len(heights) - 1):
    left_bound = 0
    right_bound = 0
    # We only want to look at the elements to the left of i, which are the elements at the lower indices
    for j in range(i+1):
      left_bound = max(left_bound, heights[j])

   # Likewise, we only want the elements to the right of i, which are the elements at the higher indices
    for j in range(i, len(heights)):
      right_bound = max(right_bound, heights[j])

    total_water += min(left_bound, right_bound) - heights[i]

  return total_water

# Testing
test_array = [4, 2, 1, 3, 0, 1, 2]
print(naive_solution(test_array))