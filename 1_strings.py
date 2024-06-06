# Strings in Python

# Strings ar IMMUTABLE: Once created, their content cannot be changed.
# you can reassign the variable name to a new string, but the original data remains unchanged

my_string = "Hello, World!"
print(id(my_string))

my_string = "Hello, Python!"
print(id(my_string))

#-- Indexing into a string : accessing idividual letters in a string

first_char = my_string[0]
print(first_char)

#-- Slicing : you can grab a chunk of a string (substring) using slicing

substring = my_string[0:5]
print(substring)

#-- Iterating : you can iterate over a string to access each character

for char in my_string:
    print(char)


#-- Formatted Strings

#--- Using .format()
name = "Alice"
formatted_str = "Hello, {}!".format(name)
print(formatted_str)

#--- Using f-strings
formatted_str = f"Hello, {name}!"
print(formatted_str)


#-- Useful String Methods

#-- len() : returns the number of characters in a string, or the length of an iterable
test = "How many CHARACTERS are in this string?"
print(len(test))

#-- .upper() : return a full uppercase version of a given string
print(test.upper())

#-- .lower() : return a full lowercase version of a given string
print(test.lower())

#-- .isupper() : Returns True or False to check if all characters are uppercase or not
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#-- .title() : formats strings in a Title Case, capitalizing every word that is seperated by a space
person = "abraham lincoln"
print(person.title())

#-- .replace(<thing to replace>, <what to replace with>) : replace a substring with a new value
txt = "I like bananas!"
x = txt.replace("bananas", "apples")
print("using .replace method: ", x)

new_text = ''
words = txt.split()
print(words)
for word in words:
    print(word)
    if word == "bananas!":
        new_text += "apples"
    else:
        new_text += word

print("Using a for loop: ", new_text)

#-- .lstrip(), .rstrip(), .strip() : allow us to strip the whitespace (empty spcae) out of a string
test = "               wow this class is awesome!!              "
print(test)

left_strip = test.lstrip() # strip the whitespace on the left side of the string only
print(left_strip)

right_strip = test.rstrip() # strip the whitespace on the right side of the string only
print(right_strip)

reg_strip = test.strip() # strips whitespace on both sides of the string
print(reg_strip)

#-- ' '.join() : joins a list of string together to form one single string
words = ["Let's", 'join', 'these', 'words', 'together!']
joined = ' '.join(words)
another_join = '  @@@@@  '.join(words)
print(joined)
print(another_join)

#-- .find() : search for a word in a string and return the index it starts at
txt = "Hello, welcome to my world!"
found = txt.find('welcome')
print(found)

#-- .count() : counts the occurances of a substring in the main string
txt = "Foxy Brown is a foxy lady. Is she actually a fox? Idk maybe we should ask a real fox?"
print(txt.lower().count('fox'))

#-- .startswith(<substring>) : return True or False depending on whether a string starts with this substring or not
people = ['Alex', "Aj", 'Brian', 'Clinton', 'Gerardo', 'Sarah']
al_team = []
for student in people:
    if student.lower().startswith('al'):
        al_team.append(student)

print(al_team)

#-- .endswith(<substring>) : return True or False depending on whether a string ends with a substring or not
name = "Travis"
print(name.endswith('s'))

#-- .isalpha() : returns Ture if the string is made entirely of alphabetic characters
letter = 'asdfghj'
print(letter.isalpha())

#-- .isdigit() : return True is made of entirely numeric characters
nums = '123456789'
print(nums.isdigit())

#-- .isspace() : returns True if the string is comprised of ONLY whitespace
empty_string = '          '
print(empty_string.isspace())

#-- .split() : splits your string based on a specified substring into a list of string, default split is on spaces
words = 'This-is-one-big string with many words'
words_list = words.split()
print(words_list)

words_list = words.split('-')
print(words_list)

flavors = input("Tell me all your favorite flavors, (serperated by a space plaes): ").split()
print(flavors)

