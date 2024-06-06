# Python Basics: Strings and Exception Handling

## Introduction to Strings

Python uses strings to store text. Here are some key points to remember:

- **Strings are immutable**: Once created, their content cannot be changed.
- You can reassign the variable name to a new string, but the original data remains unchanged.

### Example:
```python
my_string = "Hello, World!"
print(id(my_string))  # Prints the memory address of the string

my_string = "Hello, Python!"
print(id(my_string))  # Prints a new memory address
```

## Accessing Characters in a String
### Indexing
- You can access individual characters in a string using indexing.

```python
first_char = my_string[0]
print(first_char)  # Output: H
```
### Slicing
- You can grab chunks of a string (substring) using slicing.

```python
substring = my_string[0:5]
print(substring)  # Output: Hello
```
### Iterating
- You can iterate over a string to access each character.

```python
for char in my_string:
    print(char)
```

## String Manipulation
### Concatenation
- You can add strings together using the + operator.

```python
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!
```
### Using `+=`
- You can reassign and add strings using +=.

```python
greeting += " How are you?"
print(greeting)  # Output: Hello, World! How are you?
```
### Casting with str()
- You can convert other data types to a string using str().

```python
num = 10
num_str = str(num)
print(num_str)  # Output: "10"
```
## Formatting Strings
- You can format strings using .format() and f-strings.

### Using `.format()`
```python
name = "Alice"
formatted_str = "Hello, {}!".format(name)
print(formatted_str)  # Output: Hello, Alice!
```
### Using f-strings
```python
formatted_str = f"Hello, {name}!"
print(formatted_str)  # Output: Hello, Alice!
```
## Other Useful String Methods
- `len()` : returns the number of characters in a string, or the length of an iterable
```python
test = "How many CHARACTERS are in this sentence?"
print(len(test))
```

- `.upper()` : returns a full uppercase version of a given string
```python
print(test.upper())
```

- `.lower()` : return the full lowercase version of a given string
```python
print(test.lower())
```

- `.title()` : formats strings in a Title Case, capitalizing every word separated by a space
```python
person = 'abraham lincoln'
print(person.title())
```

- `.replace()` : replace a substring with a new value
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
```

- `.lstrip()`, `.rstrip()`, `.strip()`
```python
test = "         wow this class is awesome!         "

left_strip = test.lstrip() # strips whitespace on the left side of a string only
print(left_strip)

right_strip = test.rstrip() # strips whitespace on the right side of a string only
print(right_strip)

reg_strip = test.strip() # strips whitespace on the both sides of a string
print(reg_strip)
```

- `.join()`
```python
words = ["Let's", "join", "these", "words", "together"]
joined = ' '.join(words)
print(joined)
```

- `.find()`
```python
# Search for a word in a string and return the index it starts at
txt = "Hello, welcome to my world."
found = txt.find("welcome")
print(found)
```

- `.count()` : counts the occurances of the substring in the main string
```python
txt = "Foxy Brown is a foxy lady. Is she actually fox? Idk maybe we should ask a real fox?"
print(txt.lower().count('fox'))
```

- `.startswith()` : returns True or False depending on whether the string starts with sub or not
```python
people = ['Alex', 'Aj', 'Brian', 'Clinton', 'Gerardo', 'Sarah']
al_team = []
for student in people:
    if stundent.lower().startswith('al'):
        al_team.append(student)

print(al_team)
```

`.endswith()` : returns a True or False depending on whether the string ends with the sub or not
```python
name = 'Travis'
print(name.endswith('s'))
```

- `.isalpha()` : returns true if the string is made entirly of alphabetic character

```python
letter = 'aasdf'
print(letter.isalpha())
```

- `.isdigit()` : return True if the string is made entirly of  numeric characters
```python
nums = '12345'
print(nums.isdigit())
```

- `.isspace()` : returns True if string is comprised of only whitespace
```python
empty_space = '      '
print(empty_space.isspace())
```

- `.split()` : splits your string based on a specified substring, into a list of strings, default split on space
```python
words = 'This-is-one-big string with many words'
words_list = words.split()

print(words_list)

flavors = input('Tell me all of your favorite flavors, (separate with space please): ').split()
print(flavors)
```


# Error and Exception Handling
## Syntax Errors
- Syntax errors occur when the code is written incorrectly, such as missing symbols or improper indentation.

## Exceptions
- Exceptions occur when an operation fails during execution.

## Common Exceptions
`NameError`: Calling variables or functions that are not defined.
`ValueError`: Invalid conversion, like converting "nine" to 9.
`FileNotFoundError`: Trying to open a non-existent file.
`OverflowError`: Number too large.
`TypeError`: Mixing incompatible data types, like adding 1 + '1'.
`RuntimeError`: General runtime error, often from infinite loops.

# Handling Errors with Try and Except

You can handle exceptions using `try` and `except` blocks.

## Specific Exceptions

When you use `except` with specific exceptions, it handles **only** those types of exceptions.

### Example:
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Additional Blocks
`else`: Executes if the try block does not raise an exception.
`finally`: Executes no matter what, useful for cleanup actions.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Operation successful!")
finally:
    print("This runs no matter what.")
```

## Generic Except
You can also use except without specifying an exception type. This will catch any exception that occurs.

### Example:
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except:
    print("An error occurred.")
```

## Best Practices
While using a generic except block is easier, it's better practice to catch specific exceptions to avoid hiding bugs. If you do use a generic except, consider logging the exception details.

### Example with Specific and Generic except:
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

