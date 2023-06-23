"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    get_data()
    print_subject_details()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(FILENAME, "r") as in_file:
        records = []
        for line in in_file:
            line = line.strip()
            pair = line.split(',')
            pair[2] = int(pair[2])
            records.append(pair)
        print(records)


def print_subject_details():
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            line = line.strip()
            pair = line.split(',')
            pair[2] = int(pair[2])
            print(f"{pair[0]} is taught by {pair[1]} and has {pair[2]} students")


main()
