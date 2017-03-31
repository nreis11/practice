# Problem 1

# Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

nums = [3,5,3,5,2,3,5,3,3]

def sum_with_for_loop(nums):
  total = 0
  for num in nums:
    total += num
  return total

def sum_with_while_loop(nums):
  total = 0
  end = len(nums)
  i = 0
  while i < end:
    total += nums[i]
    i += 1
  return total

def sum_with_recursion(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + sum_with_recursion(nums[1:])

# print(sum_with_for_loop(nums))
# print(sum_with_while_loop(nums))
# print(sum_with_recursion(nums))

# Problem 2

# Write a function that combines two lists by alternatingly taking elements. 
# For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

a = ['a', 'b', 'c']
b = [1, 2, 3]

def combine_two_lists(list1, list2):
  result = []
  for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])
  return result

# print(combine_two_lists(a, b))

# Problem 3

# Write a function that computes the list of the first 100 Fibonacci numbers. 
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
# and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def fibonacci():
  result = [0, 1]
  a = 0
  b = 1
  while len(result) < 100:
    a, b = b, a + b
    result.append(b)
  return result

print(fibonacci())

# Problem 4

# Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. 
# For example, given [50, 2, 1, 9], the largest formed number is 95021.

nums = []





