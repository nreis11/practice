def largest_factor(n):
    total = n * n - 1
    x = 1
    y = total / x

    while (x + 1) < n:
        if total / (x + 1) % 0:
            return total / (x + 1)
        else:
            continue

def factorial(n):
    total = 1
    while n > 0:
        total = total * n
        n -= 1
    return total

def reverse(string):
    result = ''
    i = -1
    for char in range(len(string)):
        result += string[i]
        i -= 1
    return result
