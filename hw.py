def largest_factor(n):
    total = n * n - 1
    x = 1
    y = total / x

    while (x + 1) < n:
        if total / (x + 1) % 0:
            return total / (x + 1)
        else:
            continue
