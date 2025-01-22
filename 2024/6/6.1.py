import os
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()

data = [list(line) for line in data]
# print(*data, sep="\n")
direction = 0  # up
y, x = 0, 0
for y, line in enumerate(data):
    if "^" in line:
        x = line.index("^")
        break
# print(x, y)

fin = False
while not any([fin]):
    try:
        if direction == 0:
            # print(data[y - 1][x])
            # print()
            if data[y - 1][x] == "." or data[y - 1][x] == "X":
                # data[y - 1] = "".join([v if i != x else "^" for i, v in enumerate(data[y - 1])])
                # data[y] = data[y].replace("^", "X")
                data[y][x] = "X"
                data[y - 1][x]  = "^"
                y -= 1
            else:
                direction = 1
        elif direction == 1:
            if data[y][x + 1] == "." or data[y][x + 1] == "X":
                data[y][x] = "X"
                data[y][x + 1] = "^"
                x += 1
            else:
                direction = 2
        elif direction == 2:
            if data[y + 1][x] == "." or data[y + 1][x] == "X":
                data[y][x] = "X"
                data[y + 1][x] = "^"
                y += 1
            else:
                direction = 3
        elif direction == 3:
            if data[y][x - 1] == "." or data[y][x - 1] == "X":
                data[y][x] = "X"
                data[y][x - 1] = "^"
                x -= 1
            else:
                direction = 0
    except:
        fin = True
        break
    if x == 0 or y == 0:
        fin = True
        # print(*data, sep="\n")
        # print(x, y, direction)
        break
    # print(*data, sep="\n")
    # print(x, y, direction)
# count X in data
count = 0
for line in data:
    count += line.count("X")
print(count + 1)
end = time.time()
print(end - start)
