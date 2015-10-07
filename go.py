def go(n):
    if n % 2 != 0:
        print(n / 2)
        return
    while n > 0:
        print(n)
        n = n // 2
