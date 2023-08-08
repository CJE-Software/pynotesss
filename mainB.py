#looking inside of lists using the index example below
#just like with strings, we can access any single element in a list using an index specified in square brackets []
listExampleA = ['bob', 'sarah', 'paulette', 'peter', 'george', 'garry']
print(listExampleA[2])
#should print 'paulette'^^^

# IMPORTANT! 'Strings' are IMMUTABLE- you cannot change the contents of a string, you must create a new string and copy it to make any change
# HOWEVER 'Lists' are MUTABLE - you can change an element of a List using the index operator

#fruit = 'apple'
#fruit[0] = 'i'
#^^^this will throw a traceback because the string stored in 'fruit' is IMMUTABLE
fruit = 'apple'
print(fruit[3])
fRUIT = fruit.upper()
print(fRUIT)
numSet =[3, 6, 9, 12, 48, 96, 192]
print(numSet)
numSet[4] = 15
print(numSet)
# notice the change at index 4 in the collection numSet

#using the RANGE FUNCTION
#the range function returns a list of numbers that range from zero to one less than the parameter
#we can construct an index loop using for and an integer iterator
print(range(4))
randomList = ['joe', 'bob', 'carl', 'sarah', 'george']
print(len(randomList))
print(range(len(randomList)))
