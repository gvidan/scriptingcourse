"""
Week 1: Debugging exercise 4. Debugging Method Operations

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.

Each exercise should require only one kind of change/alteration.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'


#1. Calling a method
def shoutOut (str1):
	print "Yo! " + str1

shoutOut("Bernie!")
	

#2. Dealing with bad input (2 errors here)
def shoutOut(str1="Bernie"):
	try: 
		print "Yo! " + str1
	except:
		print "Exceptional Yo! " + str(str1)

shoutOut(42)

#3. Input / Output
def shoutOut(str1="Bernie"):
	try: 
		tempVar = str(str1)
		return tempVar
	except: 
		return 

print "You shall not pass, %s." % shoutOut("Dawg")

