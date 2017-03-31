import re
s = 'aabbcd'

def reduce_str(s):
    while s:
        match = re.search(r'([a-z])\1', s)
        if match:
            s = re.sub(match.group(), '', s)
        else:
            return s

    return "Empty String"

print(reduce_str(s))