## Magic behind print() function in Python.

# Python’s print() function comes with a parameter called ‘end’. And I didn't know about it till now.
# By default, the value of this parameter is ‘\n’, i.e. the new line character.
# You can end a print statement with any character/string using this parameter.

# Let's test it.
print('Avengers ')
print('Endgame')  

# Output: Avengers
#         Endgame

# Now, using end parameter.
print('Avengers',end=" ")
print('Endgame',end="")

# Output: Avengers Endgame

#------------------------------------------------------------------------------------------------

## A must-know fact about Tuples.

# When ever you want you create a tuple with just 1 element/item, you need to do the following.

tuple1 = (12,) # This is the right way to do it.

tuple2 = (12) # Not like this

# You may ask why not. Well! Let's see why.

print(type(tuple1),type(tuple2))

# Output: <class 'tuple'> <class 'int'>
# In tuple1 we used a comma to explicitly define it as a tuple, but in the tuple2 Python Intrepreter considered it to be a 'int' datatype value.

#------------------------------------------------------------------------------------------------------------------------------------------------

## Now onwards to sets and dictionaries.
# Since, we know both of them have same syntax braces, there are some things to take care of when we are dealing with both of them.

# I want to create a empty set and a empty dictionary. So, how do we do it?

set1={}
dict1={} # Is this correct?
print(type(set1),type(dict1))

# Output: <class 'dict'> <class 'dict'>
# Which means it's not the right way to do it, because Python intrepreter considers any {} assigned to valid variable as a dictionary by default.

# So, is this it? Can't we create a empty set? There is a way to do it as well.
set2 = set()
print(type(set2))

# Output: <class 'set'> # We did it, yay!
# So, that's how we can create empty sets without issues.