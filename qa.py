import random

qa = {
    'Let\'s cut to the ____': 'chase',
    '____ off more than you can chew': 'bite',
    'A picture paints a thousand ____': 'words',
    'Don\'t put all your ____ in one basket': 'eggs',
    'Every cloud has a _____ lining': 'silver',
    'Get up on the wrong side of the ____': 'bed',
    'Go out on a ____': 'limb',
    'Have an ____ to grind': 'axe',
    'Knock on _____' : 'wood',
    'Let the ____ out of the bag' : 'cat',
    'Mumbo ____': 'jumbo'
    }

qa_copy = dict(qa)
num = int(raw_input("How many questions would you like? (1 - 20)"))
score = 0.0

print "\nComplete these popular expressions:"
for i in range(num):
    question = random.choice(list(qa_copy.keys()))
    answer = qa_copy.pop(question)

    print "\n Question " + str(i + 1)
    print question
    guess = raw_input('> ')

    if guess.lower() == answer:
        print 'Correct!'
        score += 1
    else:
        print 'Incorrect.'
print "Final score: %d" % (score)
per = score / num * 100.0
print str(per) + '%'
