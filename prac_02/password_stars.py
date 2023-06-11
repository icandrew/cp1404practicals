password_length = 0

while password_length < 6:
    password = input("Password: ")
    password_length = len(password)

print("*" * password_length)