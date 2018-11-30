# Hello world, for luck.
print('Hello world!')

# Python syntax and IDE playground.

# Dictionaries:

# A simple dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Accessing values in a dictionary.
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding new key-value pairs.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary.
alien_1 = {}
print(alien_1)

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# Modifying values in a dictionary.
print("The alien's color is " + alien_1['color'] + ".")

alien_1['color'] = 'yellow'
print("The alien's color is now " + alien_1['color'] + ".")
print(alien_1)

# Move alien to the right.
alien_0['speed'] = 'fast'
print(alien_0)
print("Original X position: " + str(alien_0['x_position']))

# Determine how far to move the alien.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This one must be the fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New X position: " + str(alien_0['x_position']))

# Removing key-value pairs.
# Important! This permanently removes the key-value pair.
del alien_0['speed']
print(alien_0)

# Dictionaries are similar to objects.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# Looping through a dictionary.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'}
print(user_0)

for key, values in user_0.items():
    print("\nKey: " + key)
    print("Values: " + values)

print()
print(favorite_languages)
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is " + languages.title() + ".")

# Looping through all the keys.
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
# Default way to loop through a dictionary.
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# Checking to see if a key exists.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a dictionaries keys in order.
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary.
print("The following vales have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()
# Using .set() to get values without repeated values
for language in set(favorite_languages.values()):
    print(language.title())

# Nesting dictionaries in lists.
alien_2 = {'color': 'blue', 'points': 5}
aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(alien)

# More aliens.
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show first 5 aliens.
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# Modifying specific parts of the list.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

# Lists in dictionaries.
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese']}
print("You have ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']}

for name, languages in favorite_languages.items():
    print("\n" + name.title())
    for language in languages:
        print("\t" + language.title())

# Dictionaries in dictionaries.
user = {'aeinstein': {'first': 'albert',
                      'last': 'einstein',
                      'location': 'princeton'},
        'mcurie': {'first': 'marie',
                   'last': 'curie',
                   'location': 'paris'}
        }
for username, user_info in user.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



