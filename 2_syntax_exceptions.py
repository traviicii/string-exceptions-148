# In Python there are only two types of issues that will break your code
#-- stop your code from functioning or executing and trhow an error

# Syntax Errors : error in you coding grammar, a structural error
#--- misspelling
#--- indentation error
#--- code structure that is missing entirely or overly
#--- colons, indentation, parenthesis, ' '. " "

# Exceptions are the other big issue that can cause your program to break/stop executing

# Exceptions : arise when our code structured correctly, but some operation doean't execute for a variety of reasons

#--- ZeroDivisionError : occurs when you try to divide by 0

quotient = 10/0

#--- NameError : trying to call a variable or function before it's defined

print(x)
print(divi())
def divi():
    pass

#--- ValueError : trying to perform operations with invalid values

str_num = 'nine'
# int_num = int(str_num) # trying to convert an invalid value

my_list = ['apple', 'bananas', 'ornage']
my_list.remove('grapes')

#--- TypeError : trying to perform operations on values of inappropriate types

num = 5
total_people = num + 'people' # cannot concatinate a str and an int together

#--- AttributeError : trying to use methods on improper objects (wrong data type)

word = "Hello"
rword = word.reversed()

word.append(' world')