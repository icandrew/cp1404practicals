"""
CP1404 Prac_02 - Score Menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the main menu-driven program for score input, evaluation, and display '*'."""
    valid_score = get_valid_score()
    print(MENU)
    choice = input(">>> ")
    while choice.upper() != "Q":
        if choice.upper() == "G":
            valid_score = get_valid_score()
            print(f"Your score is: {valid_score}")
        elif choice.upper() == "P":
            marks = evaluate_mark(valid_score)
            print(f"Your score of {valid_score} is marked: {marks}")
        elif choice.upper() == "S":
            display_stars(valid_score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ")
    print("farewell")


def get_valid_score():
    """Prompt the user to enter a score between 0 and 100, validating the input."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))
    return score


def evaluate_mark(score):
    """Evaluates the marks based on the provided score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def display_stars(score):
    """Displays number of '*' based on the provided score"""
    stars = "*" * score
    print(stars)


main()
