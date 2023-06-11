# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")

""""
Using Function Definition
"""
from random import randint


def main():
    min_score, max_score = 0, 100
    student_score = randint(min_score, max_score)
    category = score_parameter(min_score, max_score, student_score)
    print(f"Your Score is {student_score} {category}")


def score_parameter(low, high, score):
    if score < low or score > high:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
