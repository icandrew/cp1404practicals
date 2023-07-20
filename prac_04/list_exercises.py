numbers = []
for number in range(5):
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("Number: "))
            if number < 0:
                print("Enter number greater than 0")
            else:
                numbers.append(number)  # adds the input number in the list
                is_valid_input = True
        except ValueError:  # catch if the user inputs a string
            print("Enter a valid number")
print(f"The first number is {numbers[0]} ")  # display the first element in the list
print(f"The last number is {numbers[-1]} ")  # display the last element in the list
print(f"The smallest number is {min(numbers)} ")  # display the minimum value in the list
print(f"The larges number is {max(numbers)} ")  # display the maximum value in the list
print(f"The average number is {sum(numbers) / len(numbers)} ")  # display the average number of the list
print("-----------")

"""
Woefully inadequate security checker
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
is_valid_input = False
while not is_valid_input:
    username = str(input("Enter Username: "))
    if username not in usernames:
        print("Access denied")
    else:
        is_valid_input = True
print("Access Granted")
