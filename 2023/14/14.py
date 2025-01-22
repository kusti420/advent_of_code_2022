if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    import sys
    sys.setrecursionlimit(1500000)

data = [list(line) for line in data]
# print(data)
def northshift():
    global data
    change = False
    for y, line in enumerate(data):
        if y == 0:
            continue
        if y > 0:
            for x, char in enumerate(line):
                if data[y][x] == "O":
                    if data[y - 1][x] != "#" and data[y - 1][x] != "O":
                        change = True
                        data[y][x] = "."
                        data[y - 1][x] = "O"
                        # print(*data, sep="\n")
                        # print()
                        # print(data[y][x])
    if change == True:
        # print(*data, sep="\n")
        # print()
        northshift()

def southshift():
    global data
    change = False
    for y, line in enumerate(data):
        if y == (len(data) - 1):
            continue
        if y < len(data) - 1:
            for x, char in enumerate(line):
                if data[y][x] == "O":
                    if data[y + 1][x] != "#" and data[y + 1][x] != "O":
                        change = True
                        data[y][x] = "."
                        data[y + 1][x] = "O"
                        # print(*data, sep="\n")
                        # print()
                        # print(data[y][x])
    if change == True:
        # print(*data, sep="\n")
        # print()
        southshift()

def eastshift():
    global data
    change = False
    for y, line in enumerate(data):
        # if y == (len(data) - 1):
        #     continue
        # if y < len(data) - 1:
        for x, char in enumerate(line):
            if x == len(line) - 1:
                continue
            if x < len(line) - 1:
                if data[y][x] == "O":
                    if data[y ][x + 1] != "#" and data[y][x + 1] != "O":
                        change = True
                        data[y][x] = "."
                        data[y][x + 1] = "O"
                        # print(*data, sep="\n")
                        # print()
                        # print(data[y][x])
    if change == True:
        # print(*data, sep="\n")
        # print()
        eastshift()

def eastshift():
    global data
    change = False
    for y, line in enumerate(data):
        # if y == (len(data) - 1):
        #     continue
        # if y < len(data) - 1:
        for x, char in enumerate(line):
            if x == len(line) - 1:
                continue
            if x < len(line) - 1:
                if data[y][x] == "O":
                    if data[y ][x + 1] != "#" and data[y][x + 1] != "O":
                        change = True
                        data[y][x] = "."
                        data[y][x + 1] = "O"
                        # print(*data, sep="\n")
                        # print()
                        # print(data[y][x])
    if change == True:
        # print(*data, sep="\n")
        # print()
        eastshift()

def westshift():
    global data
    change = False
    for y, line in enumerate(data):
        # if y == (len(data) - 1):
        #     continue
        # if y < len(data) - 1:
        for x, char in enumerate(line):
            if x == 0:
                continue
            if x > 0:
                if data[y][x] == "O":
                    if data[y ][x - 1] != "#" and data[y][x - 1] != "O":
                        change = True
                        data[y][x] = "."
                        data[y][x - 1] = "O"
                        # print(*data, sep="\n")
                        # print()
                        # print(data[y][x])
    if change == True:
        # print(*data, sep="\n")
        # print()
        westshift()


for _ in range(1000000000):
    northshift()
    westshift()
    southshift()
    eastshift()
    print(_)

def total_load():
    global data
    sm = 0
    for i, line in enumerate(reversed(data)):
        i += 1
        sm += (line.count("O") * i)
    print(sm)

total_load()