name = raw_input("What is your name? ")

tries = 5
while True:
    if name.lower() == 'nick':
        pw = raw_input("\nPassword: ")
        tries -= 1
        if pw == 'soccer':
            print "Welcome to the master system."
            exit(0)
        elif tries == 0:
            print "You have been locked out of the system."
            exit(0)
        else:
            print "Try again. Remaining tries: %d" % tries

    else:
        print "You are not allowed access into the system."
        exit(0)
