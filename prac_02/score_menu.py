MENU = """(G) - Get a valid score
(P) - Print Result
(S) - Show stars
(Q) - Quit
"""
print(MENU)
choice = input(">>> ").upper()


def main():
    global choice
    min_score, max_score = 0, 100
    while choice != "Q":
        if choice == "G":
            student_score = float(input("Enter the score: "))
            category = score_parameter(min_score, max_score, student_score)
        elif choice == "P":
            result(category)
        elif choice == "S":
            print_star(student_score)
        else:
            print("Invalid option")
        choice = input(">>> ").upper()


def result(category):
    print(f"Your Score {category}")


def score_parameter(low, high, score):
    if score < low or score > high:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_star(student_score):
    print("*" * student_score)


main()
print("Farewell")
