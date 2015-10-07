def dead(reason):
    print reason, "Game over."
    exit(0)

def kungfu():
    print "You have been trasnported to the sparring program, "
    print "more commonly known as a dojo."
    print "Do you kick or punch Morpheus first?"
    punched = False
    kicked = False

# Needs work
    while True:
        move = raw_input("What's your move? \n> ")
        if "kick" in move and not punched:
            print "Morpheus parries."
            kicked = True
        elif "kick" in move and kicked:
            dead("Kicking again allowed Morpehus to parry and knock you out.")
        elif "punch" in move:
            print "Morpheus stumbles back."
            punched = True
        elif "punch" in move and punched:
            dead("Morpheus was anticipating another punch and "
            "countered with a kick to the head.")
        elif "kick" in move and punched:
            print "That was a lethal combination to Morpheus."
            print "Victory! You really are the chosen one."
            exit(0)
        else:
            print "I don't understand what %s means." % move



def morpheus():
    print "Morpheus says, \"The time has come to train you in the martial arts."
    print "Do you want to learn kung fu or karate?"

    arts = raw_input("> ")
    if "kung fu" in arts:
        kungfu()
    elif "karate" in arts:
        karate()
    else:
        print "%s is not an option!" % arts
        arts = raw_input("> ")


def construct():
    print "Welcome to the real world!"
    print "You open your eyes and find yourself in a white space, "
    print "with only two armchairs and a TV in it."
    print "What do you do next?"
    print "1. Watch TV."
    print "2. Look for Morpheus."



    while True:
        choice = raw_input("> ")
        if "1" in choice:
            print "You find the show entertaining and enjoy being a lazy American, "
            print "but it doesn't get you anywhere. I suggest looking for your friend."
        elif "2" or "look" in choice:
            print "Morpheus appears in the armchair with a smirk."
            morpheus()
        else:
            print "Because you can't follow directions, you're not qualified to "
            print "be in the Matrix. Good bye."
            exit(0)


def start():
    print "You are sitting in a bare room with only two armchairs."
    print "Across from you is Morpheus, a dark skinned man wearing shades."
    print "He holds his hands out, each holding a pill."
    print "One is blue, the other is red."
    print "Morpheus asks you to choose which path you will take."
    print "Which one do you choose?"

    pill = raw_input('> ')

    if pill == "blue" or pill == "Blue":
        print "The story ends. You wake up in your bed and believe "
        print "whatever you want to believe."
        exit(0)
    elif pill == "red" or pill == "Red":
        construct()
    else:
        print "%s isn't an option!" % pill
        pill = raw_input('> ')

start()
