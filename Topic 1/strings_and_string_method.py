x = 'Peter Parker in Spider-man'

# capitalizes first letter in string
print(x.capitalize())

# essentially finds how many characters it takes to reach the beginning of 'Parker', starts at 0 (before 'P' in "Parker")
print(x.find('Parker'))

# figures out how many characters it takes to reach first 'S', starts at 0 (before 'P' in "Parker")
print(x.index('S'))

# figures out if string is alphanumeric
print(x.isalnum())

# figures out if string is all alphabetical (spaces don't count (?))
print(x.isalpha())

# figures out if string is all digits
print(x.isdigit())

# figures out if characters are lower cased
print(x.islower())

# figures out if characters are all upper-cased
print(x.isupper())

# figures out if characters in string are all spaces
print(x.isspace())

# figures out if string starts with ('Letter') (or number(?))
print(x.startswith('P'))

# find all these built-in functions in docs
# also remember the type is boolean if it's true or false !
