def main():
    password_length = 0

    password_length = get_name(password_length)

    print_password(password_length)


def print_password(password_length):
    print("*" * password_length)


def get_name(password_length):
    while password_length < 6:
        password = input("Password: ")
        password_length = len(password)
    return password_length


main()
