# Anagram checker

# Steps
# 1. Split word into individual characters
# 2. Alphabatize the letters
# 3. Join letters
# 4. Compare words

def is_anagram(word, word2):
	letters1 = sorted(list(word))
	letters2 = sorted(list(word2))
	sorted_word = ''.join(letters1)
	sorted_word2 = ''.join(letters2)
	print(sorted_word == sorted_word2)

def is_palindrome(word):
	print(word == word[::-1])

is_anagram('level', 'veell')
