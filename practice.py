def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    new = ''
    for c in text:
        if c not in vowels:
            new += c
    return new


def censor(text,word):
    t = text.split()
    n = []
    for w in t:
        if w == word:
            n.append('*' * len(word))
        else:
            n.append(w)
    return ' '.join(n)

def median(numbers):
    s = sorted(numbers)
    if len(s) % 2 == 0:
        median = (len(s) // 2)
        return (s[median - 1] + s[median]) / 2.0
    else:
        median = (len(s) // 2)
        return s[median]

def sorter(nums):
    i = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i + 1]:
            nums[i] = nums[i + 1]

def pyg_latin(original):
    """Processes the word so that the first letter of the word is appended to
    the end and then 'ay' is added
    >>> pyg_latin('computer')
    'omputercay'
    >>> pyg_latin('table')
    'abletay'
    >>> pyg_latin('laundromat')
    'aundromatlay'
    """

    pyg = 'ay'
    if len(original) > 0 and original.isalpha() == True:
        word = original.lower()
        first = word[0]
        new_word = word[1:] + first + pyg
        return new_word
    else:
        print "empty"

def longest_word(sentence):
    my_list = sentence.split(' ')
    my_list.sort(key=len)
    return my_list[-1]

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    tot = 0
    print ('Inventory: ')
    for k, v in inventory.items():
        print k, v
        tot += v
    print ('Total items: %d') % tot

def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print 'FizzBuzz'
        elif num % 3 == 0:
            print 'Fizz'
        elif num % 5 == 0:
            print 'Buzz'
        else:
            print num

def percentage():
    N = int(raw_input())
    names = {}

    for x in range(N):
        name = raw_input()
        name = name.split()
        names[name[0]] = name[1:4]

    print names
    N = raw_input()
    tot = 0
    for value in names[N]:
        tot += int(value)
    return format(tot / 3, '.2f')

def unique_letters(string):
    """Return True if the string contains only unique letters. Otherwise,
    return false.
    >>> unique_letters('habit')
    True
    >>> unique_letters('computer')
    True
    >>> unique_letters('level')
    False
    >>> unique_letters('door')
    False
    """

    letters = sorted(string)
    return sorted(set(string)) == letters

# Another way
#   return len(set(string)) == len(string)

def divisors(n):
    """Provides a list of all the factors of n"""
    return [1] + [x for x in range(2,n) if n % x == 0]

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        x = recursive_factorial(n - 1)
        print(n, "*", x, '=', n * x)
        return n * x

def recursion(level):
    if level < 10:
        print('Recusrion level:', level)
        level += 1
        recursion(level)


