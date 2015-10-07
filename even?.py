print ("Input [x] for exit")
print ("This program will determine if a number is",
    "odd or even.")

while True:
    inp = input("Tell me a number: ")
    if inp == 'x':
        break
#catch any resulting ValueError with conversion
#to float
    try:
        number = float(inp)
    except ValueError:
        print ("I said tell me a number wise ass!")
    else:
            test = number % 2
            if test == 0:
                print (int(number),"is an even number.")
            elif test == 1:
                print (int(number),"is an odd number.")
            else:
                print (number,"is very strange.")
