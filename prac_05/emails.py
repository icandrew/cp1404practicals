def main():
    email = input("Email: ")
    while email != "":
        parts = email.split("@")[0]
        name_parts = parts.split(".")
        name = " ".join(name_parts)
        verification = input(f"Is your name {name}? (Y/n) ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
            print(name)
        email = input("Email: ")


main()
