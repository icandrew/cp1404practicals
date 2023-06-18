FILENAME = "name.txt"

out_file = open("name.txt", "w")
name = str(input("Enter Name: "))  # Ask user to input a name
print(name, file=out_file)  # Print name
out_file.close()
