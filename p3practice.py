# Write a method that takes an array of integers and 
# an integer to search for. The method should return 
# the index of the item, or nil if the integer is not 
# present in the array. Don't use built-in array methods like .index. 
# You are allowed to use .length and .each.

def search_array(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      return i
      break
  else:
      return None

my_nums = [1, 3, 5, 5, 10, 3, 0]

print(search_array(my_nums, 10)) # returns index
print(search_array(my_nums, 55)) # returns None
