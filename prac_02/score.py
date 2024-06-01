"""
Refactor broken_score.py to use function
"""

from random import randint


def main():
    """Takes user input and a random number for a score, evaluates the score, and prints the result."""
    user_score = int(input("Enter score: "))
    mark = evaluate_mark(user_score)
    print(f"Your score of {user_score} is marked: {mark}")

    random_score = randint(1, 100)
    random_mark = evaluate_mark(random_score)
    print(f"Random score of {random_score} is marked: {random_mark}")


def evaluate_mark(score):
    """Evaluates the marks based on the provided score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
