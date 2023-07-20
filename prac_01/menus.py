# Get user name
name = input("Enter Name: ")

# Create a list of options
options = ["(H)ello", "(G)oodbye", "(Q)uit"]

# Assign the first three elements of the list to H, G, and Q, respectively
H, G, Q = options[0], options[1], options[2]


def display_menu():
    """Display Menu & Get User Choice"""
    for option in options:
        print(option)
    choice = input(">>>>")
    return choice


def main():
    selection = display_menu()
    while selection != "Q":
        if selection == "H":
            print(f"Hello {name}")
        elif selection == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid Choice")
        selection = display_menu()
    print("Finished.")

main()