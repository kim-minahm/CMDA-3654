#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#prints out the quoted text to terminal
print "I will now count my chickens:"

#prints Hens 30, which is 25+5
print "Hens", 25 + 30 / 6
#prints Roosters 97 which uses order of ops, 100 - 3
print "Roosters", 100 - 25 * 3 % 4

#prints quoted text
print "Now I will count the eggs:"
#does arithmatic, resulting in 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#prints the question to terminal
print "Is it true that 3 + 2 < 5 - 7?"
#prints false
print 3 + 2 < 5 - 7

#prints quote, then 5
print "What is 3 + 2?", 3 + 2
#prints quote then -2
print "What is 5 - 7?", 5 - 7

#more print statements
print "Oh, that's why it's False."
#more print statements
print "How about some more."
#prints the question the true
print "Is it greater?", 5 > -2
#prints the quote then true
print "Is it greater or equal?", 5 >= -2
#prints the quote, then falles
print "Is it less or equal?", 5 <= -2

#PART II

#initializes the string to days sep by space
days = "Mon Tue Wed Thu Fri Sat Sun"
#initializes the list of months to months seperated by new lines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#prints quote then the days on the same line
print "Here are the days: ", days2
#prints the months each on a new line, with jan on the first
print "Here are the months: ", months

#PART III
#places the array 1-5 into the_Count
the_count = [1, 2, 3, 4, 5]
#places fruits list into fruits
fruits = ['apples', 'oranges', 'pears', 'apricots']
#places combination of strings and integerse into change
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# Iterates through and prints this is the count with the number in the_count
for number in the_count:
    print "This is count %d" % number

# Iterates through and prints the fruits in fruits and a string
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# 
# Use %r format when you don't know
#if the elements are strings or integers
#formats and prints
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# prints all the elements with the quote
for i in elements:
    print "Element was: %d" % i