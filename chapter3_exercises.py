# Exercises for chapter 3:

# Name: Brendan Gassler

#Excercise 3.1
#My error said: "NameError: name 'repeat_lyrics' is not defined"

#Exercise 3.2
#The program runs the same as the original program because the 
#print_lyrics function is still defined before repeat_lyrics is
#ever called

#Exercise 3.3

def right_justify(word):
	length = len(word)
	extra_spaces = 70 - length
	print((' '*extra_spaces)+word)

right_justify('Exercise 3.3')

#Exercise 3.4
def do_twice(f, value):
	f(value)
	f(value)

def print_twice(string):
	print string

#do_twice(print_twice, 'spam')

def do_four(f, value):
	do_twice(f, value)
	do_twice(f, value)

do_four(print_twice, 'spam')