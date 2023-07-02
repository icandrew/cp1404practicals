with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    lines = [line.strip() for line in in_file.readlines()]
    print(lines)
