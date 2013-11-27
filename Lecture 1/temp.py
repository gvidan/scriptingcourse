print "I'm using \\n as a string, hello \"world\""


# problem: concatinating mixed types
x = 4
y = " square"


# solution one:
print "%d" % x + y


#solution two:
print str(x) + y


# split a list to a string
stringToSplit = "hello could i split this?"
splittedList = stringToSplit.split(" ")
print splittedList