"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- ValueError occurs when user inputs a string, or a float
- But except ValueError in Line16 will caught this and will display "Numerator and denominator must be valid numbers!"
2. When will a ZeroDivisionError occur?
- ZeroDivisionError occurs when a number is divided by 0
- If the user input 0 on the denominator the program continues because the ZeroDivisionError will caught in Line20
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, put this code in a while loop until the user enters a number > 0
"""


def main():
    is_valid_input = False
    while not is_valid_input:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            fraction = calculate_fraction(denominator, numerator)
            if denominator < 0:
                print("Enter number greater than 0")
            else:
                is_valid_input = True
        except ZeroDivisionError:
            print("Enter number greater than 0")
    print(fraction)


def calculate_fraction(denominator, numerator):
    fraction = numerator / denominator
    return fraction


main()
