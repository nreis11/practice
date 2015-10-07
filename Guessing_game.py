answer = 30
question = 'What number am I thinking of?'
count = 0
print ('Let\'s play the guessing game!')

while True:
    guess = int(input(question))
    count = count + 1
    if abs(guess - answer) > 50: # > 50 deviation
        print ('Are you even trying?')
    elif abs(guess - answer) < 5 and guess != answer: # 5 deviation
        print ('You\'re so close!')
    elif guess < answer:
        print ('Higher')
    elif guess > answer:
        print ('Lower')
    else: # guess == answer
        print ('Genius!')
        print ('Number of guesses:%s') % count
        break
