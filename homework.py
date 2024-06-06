
shopping_list = []

def main(): # Hold the main functionality of my app
    while True:
        ans = input('''
Welcome to the Shopping List Maker!
What would you like to do?
Enter the corresponding number for the action you'd like to take:
                    
1 - Add to your shopping list
2 - Remove an item from the shopping list
3 - View the shopping list
4 - Quit
''')
        if ans == '1':
            add_item() # add function to add to the list
        elif ans == '2':
            remove_item() # function for removing from the list
        elif ans == '3':
            view_list() # function to view current list
        elif ans == '4':
            print("Thanks for using our app!")
            break

def add_item():
    ans = input("What would you like to add? ")
    shopping_list.append(ans)

def remove_item():
    ans = input("what would you like to remove? ")
    shopping_list.remove(ans)

def view_list():
    print("Here's your current shopping list")
    for index in range(len(shopping_list)):
        print(index, shopping_list[index])

# while True:
#     ans = input('''
# Welcome to the Shopping List Maker!
# What would you like to do?
# Enter the corresponding number for the action you'd like to take:
                
# 1 - Add to your shopping list
# 2 - Remove an item from the shopping list
# 3 - View the shopping list
# 4 - Quit
# ''')
#     if ans == '1':
#         add_item() # add function to add to the list
#     elif ans == '2':
#         remove_item() # function for removing from the list
#     elif ans == '3':
#         view_list() # function to view current list
#     elif ans == '4':
#         print("Thanks for using our app!")
#         break
#     else:
#         print("enter a valid number fool!!")