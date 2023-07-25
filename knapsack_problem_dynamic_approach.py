# Diese Lösung stellt eine naive rekursive Lösung vor

"""
Imagine that you’re a thief breaking into a house. There are so many valuables to steal
- diamonds, gold, jewelry, and more! But remember, you’re just one person who can only carry so much.
Each item has a weight and value, and your goal is to maximize the total value of items
while remaining within the weight limit of your knapsack.
This is called the knapsack problem and is commonly used in programming interviews.
"""


def dynamic_knapsack(weight_cap, weights, values):
    """
    Hier setze ich die Zeilen und Spalten für die 2D-Matrix, wobei ich jeweils 1 addiere,
    die Möglichkeit abbilden zu können, dass Werte auch 0 beinhalten
    """
    rows = len(weights) + 1
    cols = weight_cap + 1

    """
    Hier initialisiere ich die Matrix, wobei als Standardwert die Matrix mit -1
    aufgefüllt wird, um klarzumachen, dass diese Zellen noch nicht berechnet wurden
    """
    matrix = [[-1 for _ in range(cols)] for _ in range(rows)]

    # Iterate through every row (each item)
    for index in range(rows):
        # Initialize columns for this row (each possible weight)
        matrix[index] = [-1 for _ in range(cols)]

        # Iterate through every column (each possible weight)
        for weight in range(cols):
            # Base case: When either no items or no weight capacity left,
            # the maximum value is 0.
            if index == 0 or weight == 0:
                matrix[index][weight] = 0
            # If the weight of the current item is less than or equal to the current weight,
            # we can consider including it in the knapsack or excluding it.
            elif weights[index - 1] <= weight:
                # Calculate the value if we include the current item
                include = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]
                # Calculate the value if we exclude the current item
                exclude = matrix[index - 1][weight]
                # Choose the maximum value between including and excluding the item
                matrix[index][weight] = max(include, exclude)
            # If the weight of the current item is greater than the current weight,
            # we cannot include it in the knapsack, so we use the previous row's value.
            else:
                matrix[index][weight] = matrix[index - 1][weight]

    # Return the value at the bottom right of the matrix, which represents the maximum value achievable
    return matrix[rows - 1][weight_cap]


# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, values))
