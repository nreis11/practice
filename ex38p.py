list = ['spring','summer','fall','winter']
extra = "Get busy living or get busy dying."
more_items = extra.split(' ')

while len(list) < 10:
    new = more_items.pop()
    list.append(new)
    end = list.pop()
    list.insert(0,end)

print list
