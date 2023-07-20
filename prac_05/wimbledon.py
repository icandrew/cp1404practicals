with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        data = line.strip().split(",")
        print(f"{data[1]}, {data[2]}")

