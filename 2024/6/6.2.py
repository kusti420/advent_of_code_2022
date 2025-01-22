import os, sys
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()

sys.setrecursionlimit(150000)


data = [list(line) for line in data]
# print(*data, sep="\n")

direction = 0  # up
steps = 0
y, x = 0, 0
for y, line in enumerate(data):
    if "^" in line:
        x = line.index("^")
        break
# print(y, x)

def turn():
    global direction
    direction += 1
    direction %= 4

def check_surroundings():
    # 0 -> wall -> turn
    # 1 -> no wall -> no win
    # 2 -> no wall -> win
    # print("dir", direction)
    try:
        if direction == 0:
            if y-1 == 0 and data[y-1][x] != "#":
                return 2
            elif y-1 >= 0 and data[y-1][x] == "#":
                return 0
            elif y-1 >= 0 and data[y-1][x] != "#":
                return 1
        elif direction == 1:
            if x+1 == len(data[0]) and data[y][x+1] != "#":
                return 2
            elif x+1 <= len(data[0]) and data[y][x+1] == "#":
                return 0
            elif x+1 <= len(data[0]) and data[y][x+1] != "#":
                return 1
        elif direction == 2:
            if y+1 == len(data) and data[y+1][x] != "#":
                return 2
            elif y+1 <= len(data) and data[y+1][x] == "#":
                return 0
            elif y+1 <= len(data) and data[y+1][x] != "#":
                return 1
        elif direction == 3:
            if x-1 == 0 and data[y][x-1] != "#":
                return 2
            elif x-1 >= 0 and data[y][x-1] == "#":
                return 0
            elif x-1 >= 0 and data[y][x-1] != "#":
                return 1
    except:
        return 2

def move_up():
    global x, y
    y -= 1

def move_right():
    global x, y
    x += 1

def move_down():
    global x, y
    y += 1

def move_left():
    global x, y
    x -= 1

def move():
    global steps, direction, y, x
    c = check_surroundings()
    
    # print(y, x, c)
    if c == 0:
        turn()
        move()
    elif c == 1:
        data[y][x] = "X"
        if direction == 0:
            move_up()
        elif direction == 1:
            move_right()
        elif direction == 2:
            move_down()
        elif direction == 3:
            move_left()
        steps += 1
        data[y][x] = "^"
        # print(*data, sep="\n")
        # print(y, x, c)
        # print()
        move()
    elif c == 2:
        return steps
move()
print(steps)

counter = 1
for line in data:
    counter += line.count("X")
print("count", counter)

end = time.time()
print(end - start)