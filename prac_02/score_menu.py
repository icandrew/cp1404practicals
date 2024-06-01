"""
CP1404 Prac_02 - Score Menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ")
    while choice.upper() != "Q":
        if choice.upper() == "G":
            print("G option")
        elif choice.upper() == "P":
            print("P option")
        elif choice.upper() == "S":
            print("P option")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ")
    print("farewell")


main()
