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
    student_score = float(input("Enter the score: "))
    min_score = 0
    max_score = 100
    category = score_parameter(min_score, max_score, student_score)
    print(category)


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
