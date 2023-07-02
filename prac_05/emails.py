def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        verification = input(f"Is your name {name}? (Y/n) ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ").title()
        email_to_name[name] = email
        email = input("Email: ")

    for name, email in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    parts = email.split("@")[0]
    name_parts = parts.split(".")
    name = " ".join(name_parts).title()
    return name


main()
