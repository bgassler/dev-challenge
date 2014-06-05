# Exercises for chapter 2:

# Name: Brendan Gassler

#Exercise 2.1: It is writing in octal, meaning 8 is a base
#insetead of 10

#Exercise 2.2: A)There is no output without using print statements
#B)The modified scripts looks like this:
print 5
x = 5
print x + 1
#output:
#5
#6

#Exercise 2.3
width = 17
height = 12.0
delimeter = '.'
print width/2       #8--int
print width/2.0     #8.5--float
print height/2      #6.0--int
print 1 + 2 * 5     #11--int 
print delimeter * 5 #.....--string

#Exercise 2.4
#problem 1
import math
print math.pow(5,3)*math.pi*(4.0/3.0) #output: 523.598775598
#problem 2
books = 60
book_cost = (24.95*0.6);
total_book_cost  = books * book_cost
total_shipping_cost = 3 + (.75 * (books - 1))
total_cost  = total_book_cost + total_shipping_cost
print total_cost #outputs: 945.45

#problem 3
easy_mile = (8*60)+15
tempo_mile = (7*60)+12
total_seconds  = (easy_mile*2) + (tempo_mile*3)
total_minutes = total_seconds/60
extra_seconds = total_seconds - (total_minutes*60)

print total_minutes
print extra_seconds

#which means you arrive home 38 minutes and 6 seconds later at 7:30am and 6 seconds