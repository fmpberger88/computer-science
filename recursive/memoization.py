memo = {}

def fibonacci(num):
    if num < 0:
        raise ValueError("No negative number please!")
    answer = None
    if num in memo:
        return memo[num]
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]


# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))