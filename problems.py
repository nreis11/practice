# 00
def reverse(x):
    """Reverses the characters"""
    modified = ''
    i = -1
    for char in range(len(x)):
        modified += x[i]
        i -= 1
    return modified

# 01
def factorial(n):
    """Returns total of n * (n - 1), (n - 2), etc...

    >>> factorial(6)
    720
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total

# 02
def longest_word(sentence):
    """Takes a string and prints out the longest word.

    >>> longest_word('short longest')
    'longest'
    >>> longest_word('one')
    'one'
    >>> longest_word('abc def abcde')
    'abcde'
    """
    mylist = sentence.split(' ')
    mylist.sort(key=len)
    return mylist[-1]

def longest_word_2(sentence):
    return max(sentence.split(), key=len)

def longest_word_3(a_list):
    longest = a_list[0]
    for i in range(len(a_list)):
        if len(a_list[i]) > len(longest):
            longest = a_list[i]
    return longest

my_words = ['hello', 'goodbye', 'hi', 'bye']
print(longest_word_3(my_words))



# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.

# 03
def sum_nums(num):
    """Takes an integer and returns the sum of all integers between zero and num
    >>> sum_nums(1)
    1
    >>> sum_nums(2)
    3
    >>> sum_nums(3)
    6
    >>> sum_nums(4)
    10
    >>> sum_nums(5)
    15
    """
    total, x = 0, 0
    while x <= num:
        total += x
        x += 1
    return total

# 04

def time_conversion(minutes):
    """Takes in minutes and converts it to an hour:minute format.
    >>> time_conversion(15)
    '0:15'
    >>> time_conversion(150)
    '2:30'
    >>> time_conversion(360)
    '6:00'
    """
    hours, minute = minutes // 60, minutes % 60
    return "%d:%02d" % (hours, minute)

# 05

def count_vowels(string):
    """Count the number of vowels in a string. 'Y' is considered a consonant.
    """
    vowels = 'aeiou'
    count = 0
    for c in vowels:
        count += string.count(c)
    return count

#06

def palindrome(string):
    """Returns a True value if string is the same forwards or backwards.
    >>> palindrome("level")
    True
    >>> palindrome("mother")
    False
    >>> palindrome("radar")
    True
    """
    backwards = string[::-1]
    return string == backwards

# 07

def nearby_az(string):
    """Returns a True value if the letter "z" is within three letters after
    the letter "a"
    >>> nearby_az("baz")
    True
    >>> nearby_az("abz")
    True
    >>> nearby_az("abcz")
    True
    >>> nearby_az("a")
    False
    >>> nearby_az("z")
    False
    """
    index_a = 0
    index_z = index_a + 1
    while index_a < len(string):
        if string[index_a] == 'a':
            while index_z < len(string):
                if string[index_z] == 'z' and 0 < (index_z - index_a) <= 3:
                    return True
                    break
                else:
                    index_z += 1
            return False
        index_a += 1
    return False

# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.
# 08
def two_sum(nums):
    """A method that takes an array of numbers. If a pair of numbers
    in the array sums to zero, return the positions of those two numbers.
    If no pair of numbers sums to zero, return `nil`.
    >>> two_sum([1, 3, 5, -3])
    [1, 3]
    >>> two_sum([3, 5, 7, 9])
    'nil'
    """
    index_1 = 0
    while index_1 < len(nums):
        index_2 = index_1 + 1
        while index_2 < len(nums):
            if nums[index_1] + nums[index_2] == 0:
                return [index_1, index_2]
                break
            index_2 += 1
        index_1 += 1
    return 'nil'

# Write a method that takes in a number and returns true if it is a
# power of 2. Otherwise, return false.
# 09
def is_power_of_two(num):
    if num < 1:
        return False

    while True:
        if num == 1:
            return True
        elif num % 2 == 0:
            num = num / 2
        else:
            return False


# Difficulty: medium.
# 10
def third_greatest(nums):
    """Write a method that takes an array of numbers in. Your method should
    return the third greatest number in the array. You may assume that
    the array has at least three numbers in it."""
    uniques = []
    for num in sorted(nums):
        if num not in uniques:
            uniques.append(num)
    return uniques[-3]

# 11
def most_common_letter(string):
    """Write a method that takes in a string. Your method should return the
    most common letter in the array, and a count of how many times it
    appears.

    Difficulty: medium."""
    max_count = string.count(string[0])
    max_value = string[0]

    for letter in string.lower():
        if string.count(letter) > max_count:
            max_count = string.count(letter)
            max_value = letter
    return max_value, max_count

# 12
# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

def dasherize_number(num):
    """Write a method that takes in a number and returns a string, placing
    a single dash before and after each odd digit. There is one
    exception: don't start or end the string with a dash.

    >>> dasherize_number(5678)
    '5-6-7-8'
    >>> dasherize_number(5000)
    '5-000'
    >>> dasherize_number(8888)
    '8888'
    >>> dasherize_number(1111)
    '1-1-1-1'
    """
# Needs work

    n = list(str(num))
    delimiter = '-'
    result = []
    index_1= 0
    while index_2 < len(n):
        index_2 = index_1 + 1
        if int(n[index_1]) % 2 == 1 and int(n[index_2]) % 2 == 0:
            result.append(delimiter)
            result.append(n[index_1] + delimiter)
        elif int(n[index_1]) % 2 == 1 and int(n[index_2]) % 2 == 1:
            result.append(n[index_1] + delimiter)
        else:
            result.append(n[index_1])
        index_1 += 1
    print result
    if result[0] == '-':
        del result[0]
    if result[-1] == '-':
        del result[-1]
    return ''.join(result)

# 13

#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.

def capitalize_words(string):
    """Write a method that takes in a string of lowercase letters and
    spaces, producing a new string that capitalizes the first letter of
    each word.
    >>> capitalize_words('this is a sentence')
    'This Is A Sentence'
    >>> capitalize_words('happy birthday')
    'Happy Birthday'
    """
    my_list = string.split()
    new = []
    for word in my_list:
        new.append(word.capitalize())
    return " ".join(new)

# 14
def scramble_string(string, positions):
    """Write a method that takes in a string and an array of indices in the
    string. Produce a new string, which contains letters from the input
    string in the order specified by the indices of the array of indices.

    Difficulty: medium.
    >>> scramble_string('abcd', [3, 1, 2, 0])
    'dbca'
    >>> scramble_string("markov", [5, 3, 1, 4, 2, 0])
    'vkaorm'
    """
    new = []
    for idx in positions:
        new.append(string[idx])
    return "".join(new)

















# 15
def is_prime(x):
    for n in range(2, x):
        if x % n == 0:
            print "Not prime."
            break
    print "Prime number."
