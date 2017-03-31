def integers():
    nums = range(1,101)

    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

def first_letter():
    st = 'Create a list of the first letters of every word in this string'

    [word[0] for word in st.split()]

x = 'This is global.'
def func(x):
    print "Here's x: " + x
    x = 'This is local.'
    print "Now X is: " + x
