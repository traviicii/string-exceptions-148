# Handling exceptions with Try and Except

#--- try : allows us to try a codeblock that will potentially raise an exception

#--- except : in the event that we do run into an exception, we can execute the codeblock without terminating our program with an error message

try: 
    x = 1
    print(x + 'person')
except:
    print("Sorry we can't do that!")

# Specific Exceptions : we can respond with a particular message for a specific kind of error


try:
    div = int(input('Give me a number to divide by 10 by: '))
    quotient = 10 / div
    print(f"10 divided by {div} = {quotient}")
except ValueError:
    print("Make sure you enter a valid number!!")
except ZeroDivisionError:
    print("You can't divide by 0!")
except:
    print("Invalid input, try again.")

#-- else : an additional code block that execute only when the Try block succeeds

while True:
    try:
        age = int(input("How old are you? "))
        birthday = age + 1
    except ValueError:
        print("Please respond with only numbers!")
    except:
        print("Invalid response.")
    else:
        print(f"On your birthday you will be {birthday} years old!")
        break

#-- finally : an additional code block that executes regardles of whether your try block succeeds or not

groceries = ['apple', 'bananas', 'walnuts', 'pear', 'bread']

while True:
    try:
        item = input("what item do you want to remove? ")
        groceries.remove(item)
    except ValueError:
        print(f"It looks like you don't have {item} on your list.")
    except:
        print("Invalid input")
    else:
        print(f"Successfully removed {item} from your list!")
        break
    finally: # this block executes regardless of whether the try block succeeds or not
        print("your current list: ")
        print('~' * 30)
        for item in groceries:
            print(item)


# Best Practices : consider logging any exception details so that you can prepare for specific unexpected errors in the future

try:
    number =int(input("enter a number: "))
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("Hey dude, you can't divide by zero. Duh!")
except ValueError:
    print("Please enter a valid number, my app isn't that smart yet. :(")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
