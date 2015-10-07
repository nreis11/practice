def reverse(word):
    letters = list(word)
    r_list = letters
    i = 0
    for items in range(len(r_list)):
        end = r_list.pop()
        r_list.insert(i,end)
        i += 1
    delimiter = ''
    processed = delimiter.join(r_list)
    print processed

def reverse_2(word):
    modified = ''
    i = -1
    for item in range(len(word)):
        modified = modified + word[i]
        i -= 1
    print modified
