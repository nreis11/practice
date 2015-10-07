from sys import argv

script, name = argv
prompt = "Your choice: "

print "You are running the %s script." % script
print "Hello %s, this is a test of the emergency" % name
print "political system."

print "Which political party do you affiliate with most?"
politics = raw_input(prompt)

print "Who was the best US president?"
best = raw_input(prompt)

print "And the worst?"
worst = raw_input(prompt)

print """
Your answers are quite interesting. Because you identify
mostly with %ss, you thought %s was the best US president
and that %s was the worst. """ % (politics, best, worst)
