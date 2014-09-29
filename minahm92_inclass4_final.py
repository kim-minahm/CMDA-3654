#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

#Lecture 14
#creates a string 
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print "Wait there are not 10 things in that list. Let's fix that."

#splits the string, delimiting by spaces
stuff = ten_things.split(' ')
#makes an array 8 things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#checks length of stuff and if not 10 then go thruogh loop
while len(stuff) != 10:
    #remove last item from more_stuff(right to left) and store it into next one
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    #add the popped item to stuff
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

#print the list
print "The 'stuff' list: ", stuff

#Working with Dictionaries

#makes a dictionary where a is 'some value' and b is a list of 1 through 4
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]} #can contain lists

#Access an element by key
print d1['a']

#Add an element (a pair key: value) to the dict
d1[7] = 'an integer'
print d1

#Check if the dict contains a certain key
print "b" in d1

#Delete a value

del d1[7]
print d1

#Use functions defined for dictionaries
print "Keys", d1.keys()
print "Values", d1.values()
#/Lecture 14
print stuff[1]
print stuff[-1] 
print stuff.pop()
print ' '.join(stuff) 
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# creates a dictionary with the state name and its abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# linkes the state abbreviation to a city
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# adds a definition to ny and or to the capitals
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# prints the state and the capital
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#prints the abbreviation associated with the state 
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# prints all the cities found in the given state
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# iterates through the state and checks the abbreviations for it
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# prints all the cities and checks for a given abbreviation
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# checks for all the states through abbrev and finds the corrosponding abreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



