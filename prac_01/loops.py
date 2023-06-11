for i in range(1, 21, 2):
    print(i, end=' ')
print()

""""
Count in 10s from 0 to 100:
"""

for j in range (0, 110, 10):
    print(j, end=" ")
print()

""""
Count down from 20 to 1:
"""

for r in range(20, 0, -1):
    print(r, end=" ")
print()

""""
Print N Stars
"""
star_count = int(input("Number of Stars: "))
stars = star_count * "*"
for l in stars:
    print(l, end="")
print()

""""
Print N Lines Increasing
"""
star_count = int(input("Number of Stars: "))
for star_increase in range(star_count):
    print(f"*" * (star_increase + 1))
print()