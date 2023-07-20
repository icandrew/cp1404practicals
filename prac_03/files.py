def main():
    name_file = "name.txt"
    number_file = "numbers.txt"
    get_name(name_file)
    read_name(name_file)
    sum_of_two_lines(number_file)
    sum_of_all_lines(number_file)


# TODO 1: Write code that asks the user for their name, then opens a
#  file called "name.txt" and writes that name to it. Remember to close your file.


def get_name(name_file):
    out_file = open(name_file, "w")
    name = str(input("Enter Name: "))  # Ask user to input a name
    print(name, file=out_file)  # Print name
    out_file.close()


# TODO 2: Write code that opens "name.txt" and reads the name (as above) then prints,
#  Your name is {name}


def read_name(name_file):
    in_file = open(name_file, "r")
    name = in_file.read()
    print(f"Your name is {name}")  # Print name
    in_file.close()


# TODO 3: Write code that opens "numbers.txt", reads only the first two numbers
#  and adds them together then prints the result, which should be... 59.

def sum_of_two_lines(number_file):
    in_file = open(number_file, "r")
    numbers = in_file.read(5).split()
    print(int(numbers[0]) + int(numbers[1]))
    in_file.close()


# TODO 4: Now write a fourth block of code that prints the total for all lines
#  in numbers.txt or a file with any number of numbers.


def sum_of_all_lines(number_file):
    in_file = open(number_file, "r")
    numbers = in_file.read().split()
    total_sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    print(total_sum)
    in_file.close()


main()
