"""
Old Password_stars
"""

# MINIMUM_LENGTH = 6
#
# password = input('Enter a password: ')
# while len(password) < MINIMUM_LENGTH:
#     print(f"Your password must be at least {MINIMUM_LENGTH} characters long.")
#     password = input('Enter a password: ')
# else:
#     print(f"{'*' * len(password)}")


"""
New Password_stars
"""

MINIMUM_CHARACTERS = 12


def main():
    """ Prompts the user for a password and prints it with characters replaced by '*' """
    password = get_password(MINIMUM_CHARACTERS)
    print_password(password)


def get_password(minimum_password_length):
    """ Prompts the user to enter a password until it meets the minimum length requirement. """
    password = input('Enter a password: ')
    while len(password) < minimum_password_length:
        print(f"Your password must be at least {minimum_password_length} characters long.")
        password = input('Enter a password: ')
    return password


def print_password(password):
    """ Prints the masked version of the password with '*' replacing each character. """
    print(f"{'*' * len(password)}")


main()
