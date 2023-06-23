"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    #  Changed months to number_of_months
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        #  Used f-string instead of string concatenation (+)
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    print_report(incomes, number_of_months, total)


def print_report(incomes, number_of_months, total):
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        #  Refactor the line that calculates total income
        total = calculate_total_income(income, total)
        #  Format the display using f-string
        print(f"Month {month:2} - Income: ${income:10.2f} Total: {total:10.2f}")


def calculate_total_income(income, total):
    total += income
    return total


main()
