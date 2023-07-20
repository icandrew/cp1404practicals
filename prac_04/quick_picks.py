from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for number in range(number_of_quick_picks):
    is_valid_input = False
    while not is_valid_input:
        quick_picks = []
        try:
            if number_of_quick_picks < 0:
                print("Enter atleast 1")
            else:
                random_number = randint(MIN_NUMBER, MAX_NUMBER)
                quick_picks.append(random_number)
                is_valid_input = True
                print(quick_picks)
        except ValueError:
            print("Enter a valid number")

