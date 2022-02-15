# assigns og list and prints it
list_one = ['shadow', 'rain', 'moon']
print(list_one)

# adds string to list
list_one.append('sun')
print(list_one)

# copy's list_one to list_two
list_two = list_one.copy()
print(list_one)
print(list_two)

# finds where string is in list, so 'shadow' is in 0 place (remember counting starts at 0!)
print(list_one.index('shadow'))

# counts what place string is in
print(list_one.count('rain'))

# uses index, shows what happens when the index does not exist in list (taken out to keep output simple
# print(list_one.index('sun'))

# same as append but inserts string before the number, in this case inserts 'sun' before 'rain' and ends up being the new 1 in list
list_one.insert(1, 'sun')
print(list_one)

# removes string from list, because everything was put in one file, there are two 'sun' so this removes the first 'sun' in list
# put in idle to see more clearly or look at assignment
list_one.remove('sun')
print(list_one)

# reverses list order
list_one.reverse()
print(list_one)

# sorts list, in this case it puts it in alphabetical order
list_one.sort()
print(list_one)

# clears list, only leaves brackets
list_one.clear()
print(list_one)
