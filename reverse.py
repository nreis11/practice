def reverse(n):
    letters = list(n)
    i = 0
    for items in range(len(letters)):
        end = letters.pop()
        letters.insert(i,end)
        i += 1
    delimiter = ''
    processed = delimiter.join(letters)
    print processed
