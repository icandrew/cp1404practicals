"""
Menus
"""
name = input('Enter name: ')
menu = "(H)ello \n(G)oodbye \n(Q)uit"
print(menu)
choice = input(">>> ")

while choice.upper() != "Q":
    if choice.upper() == "H":
        print(f"Hello {name}")
        print(menu)
        choice = input(">>> ")
    elif choice.upper() == "G":
        print(f"Goodbye {name}")
        print(menu)
        choice = input(">>> ")
    else:
        print(menu)
        print("Invalid choice")
        choice = input(">>> ")
print("Finished.")
