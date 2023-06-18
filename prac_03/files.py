def main():
    filename = "name.txt"
    get_name(filename)


def get_name(filename):
    out_file = open(filename, "w")
    name = str(input("Enter Name: "))  # Ask user to input a name
    print(name, file=out_file)  # Print name
    out_file.close()


main()
