def main():
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        verification = input(f"Is your name {name}? (Y/n) ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
            print(name)
        email = input("Email: ")


def extract_name(email):
    parts = email.split("@")[0]
    name_parts = parts.split(".")
    name = " ".join(name_parts)
    return name


main()
