#a dictionary is a collection of key values pairs, they can contain everything

age = {'Dante': 34,
       'Samantha': 64,
       'Dimitri': 45,
       'John': 'unknown'}

print(age)

#to access a value in a dictionary use the associated key

print(age['Samantha'])

#dictionaries are dynamic we can add entries
age['Pluto'] = 74
print(age)

#modify a value
age['Pluto'] = 45
print(age)
print(age['Pluto'])

del age['Pluto']
print(age)