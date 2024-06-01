for i in range(1, 21, 2):
    print(i, end=' ')
print("\n--------------------------")

# count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
print("A:")
for i in range(0, 110, 10):
    print(i, end=' ')
print("\n--------------------------")

# count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
print("B:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n--------------------------")

# print n stars. Ask the user for a number, then print that many stars (*), all on one line.
print("C:")
count = int(input('Number of stars: '))
for star in range(count):
    print("*", end='')
print("\n--------------------------")

# print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1
# with no blank line.
print("D:")
count = int(input('Number of stars: '))
for star in range(1, count + 1):
    print("*" * star)
print("--------------------------")
