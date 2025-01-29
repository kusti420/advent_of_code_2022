import os, sys
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = 2024
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()
sys.setrecursionlimit(150000)
import copy
data = [list(line) for line in data]
initial_data = copy.deepcopy(data)
# print(*data, sep="\n")
moves = []
turns = []
direction = 0  # up
steps = 0
y_coord, x_coord = 0, 0
loopcounter = 0
itercase = 0
for y_coord, line in enumerate(data):
    if "^" in line:
        x_coord = line.index("^")
        break
# print(y, x)
def turn():
    global direction, turns, x_coord, y_coord
    direction += 1
    direction %= 4
    turns.append([x_coord, y_coord])
def upcheck(x = None, y = None):
    if x == None and y == None:
        try:
            if y_coord-1 == 0 and data[y_coord-1][x_coord] != "#":
                return 2
            elif y_coord-1 >= 0 and data[y_coord-1][x_coord] == "#":
                return 0
            elif y_coord-1 >= 0 and data[y_coord-1][x_coord] != "#":
                return 1
        except:
            return 2
    else:
        try:
            if y == 0 and data[y-1][x] != "#":
                return 2
            elif y >= 0 and data[y-1][x] == "#":
                return 0
            elif y >= 0 and data[y-1][x] != "#":
                return 1
        except:
            return 2
def rightcheck(x = None, y = None):
    if x == None and y == None:
        try:
            if x_coord+1 == len(data[y_coord]) and data[y_coord][x_coord+1] != "#":
                return 2
            elif x_coord+1 <= len(data[y_coord]) and data[y_coord][x_coord+1] == "#":
                return 0
            elif x_coord+1 <= len(data[y_coord]) and data[y_coord][x_coord+1] != "#":
                return 1
        except:
            return 2
    else:
        try:
            if x+1 == len(data[y]) and data[y][x+1] != "#":
                return 2
            elif x+1 <= len(data[y]) and data[y][x+1] == "#":
                return 0
            elif x+1 <= len(data[y]) and data[y][x+1] != "#":
                return 1
        except:
            return 2
def downcheck(x = None, y = None):
    if x == None and y == None:
        try:
            if y_coord+1 == len(data) and data[y_coord+1][x_coord] != "#":
                return 2
            elif y_coord+1 <= len(data) and data[y_coord+1][x_coord] == "#":
                return 0
            elif y_coord+1 <= len(data) and data[y_coord+1][x_coord] != "#":
                return 1
        except:
            return 2
    else:
        try:
            if y+1 == len(data) and data[y+1][x] != "#":
                return 2
            elif y+1 <= len(data) and data[y+1][x] == "#":
                return 0
            elif y+1 <= len(data) and data[y+1][x] != "#":
                return 1
        except:
            return 2
def leftcheck(x = None, y = None):
    if x == None and y == None:
        try:
            if x_coord-1 == 0 and data[y_coord][x_coord-1] != "#":
                return 2
            elif x_coord-1 >= 0 and data[y_coord][x_coord-1] == "#":
                return 0
            elif x_coord-1 >= 0 and data[y_coord][x_coord-1] != "#":
                return 1
        except:
            return 2
    else:
        try:
            if x-1 == 0 and data[y][x-1] != "#":
                return 2
            elif x-1 >= 0 and data[y][x-1] == "#":
                return 0
            elif x-1 >= 0 and data[y][x-1] != "#":
                return 1
        except:
            return 2

def check_surroundings():
    # 0 -> wall -> turn
    # 1 -> no wall -> no win
    # 2 -> no wall -> win
    # print("dir", direction)
    try:
        if direction == 0: # up
            return upcheck()
        elif direction == 1: # right
            return rightcheck()
        elif direction == 2:
            return downcheck()
        elif direction == 3:
            return leftcheck()
    except:
        return 2
def move_up():
    global x_coord, y_coord, moves
    moves.append([x_coord, y_coord, direction])
    y_coord -= 1
def move_right():
    global x_coord, y_coord, moves
    moves.append([x_coord, y_coord, direction])
    x_coord += 1
def move_down():
    global x_coord, y_coord, moves
    moves.append([x_coord, y_coord, direction])
    y_coord += 1
def move_left():
    global x_coord, y_coord, moves
    moves.append([x_coord, y_coord, direction])
    x_coord -= 1

def isloop():
    try:
        for i in range(len(turns)):
            if itercase == 6:
                print(turns[i:i+4], turns[i+4:i+8])
                # exit()
            if turns[i:i+4] == turns[i+4:i+8]:
                return True
        return False
    except:
        return False
def move():
    global steps, direction, y_coord, x_coord, loopcounter
    c = check_surroundings()
    if isloop():
        loopcounter += 1
        return steps
    # print(y, x, c)
    if c == 0:
        turn()
        move()
    elif c == 1:
        data[y_coord][x_coord] = "X"
        if direction == 0:
            move_up()
        elif direction == 1:
            move_right()
        elif direction == 2:
            move_down()
        elif direction == 3:
            move_left()
        steps += 1
        data[y_coord][x_coord] = "^"
        # print(*data, sep="\n")
        # print(y, x, c)
        # print()
        move()
    elif c == 2:
        return steps
move()
# print(steps)
counter = 1
for line in data:
    counter += line.count("X")
print("count", counter) # 6082 steps, answer = 5404
# end = time.time()
# print(end - start)
# # print(data)
# obstructions = []
# # print(moves[60])

# a = upcheck(moves[60][0], moves[60][1])

# print(moves)
# import copy
# def does_it_loop(x, y, dr):
#     # new_obstructions = [v for v in [[x + 1, y] if x + 1 < len(data[y]) else None, [x - 1, y] if x - 1 >= 0 else None, [x, y + 1] if y + 1 < len(data) else None, [x, y - 1] if y - 1 >= 0 else None] if v != None]
#     # print(new_obstructions)
#     start = [x, y]
#     x, y = copy.deepcopy(start)
#     def find_next_obstruction_up(x, y):
#         # xx, yy = copy.deepcopy([x, y])
#         while True:
#             if data[y - 1][x] == "#":
#                 return [x, y - 1]
#                 break
#             y -= 1
            
#     def find_next_obstruction_right(x, y):
#         # xx, yy = copy.deepcopy([x, y])
#         while True:
#             # print(xx, yy)
#             if data[y][x + 1] == "#":
#                 return [x + 1, y]
#                 break
#             x += 1
            
#     def find_next_obstruction_down(x, y):
#         # x, y = copy.deepcopy([x, y])
#         while True:
#             if data[y + 1][x] == "#":
#                 return [x, y + 1]
#                 break
#             y += 1
            
#     def find_next_obstruction_left(x, y):
#         # xx, yy = copy.deepcopy([x, y])
#         while True:
#             if data[y][x - 1] == "#":
#                 return [x - 1, y]
#                 break
#             x -= 1
    
#     if dr == 0:
#         new_obstruction = [x, y - 1]
#     elif dr == 1:
#         new_obstruction = [x + 1, y]
#     elif dr == 2:
#         new_obstruction = [x, y + 1]
#     elif dr == 3:
#         new_obstruction = [x - 1, y]
#     print("new", new_obstruction) # 59, 76
#     xxx, yyy = new_obstruction
#     print("new", xxx, yyy)
#     # up = find_next_obstruction_up(xxx, yyy)
#     # print("up", up)
#     # right = find_next_obstruction_right(up[0], up[1])
#     # print("right", right)
#     # down = find_next_obstruction_down(right[0], right[1])
#     # print("down", down)
#     # left = find_next_obstruction_left(down[0], down[1])
#     # print("left", left)
    
#     points = []
#     previous = [xxx, yyy]
#     for i in range(1, 5):
#         if dr + i % 4 == 0:
#             tmp = find_next_obstruction_up(previous[0], previous[1])
#             previous = tmp
#             points.append(tmp)
#         elif dr + i % 4 == 1:
#             tmp = find_next_obstruction_right(previous[0], previous[1])
#             previous = tmp
#             points.append(tmp)
#         elif dr + i % 4 == 2:
#             tmp = find_next_obstruction_down(previous[0], previous[1])
#             previous = tmp
#             points.append(tmp)
#         elif dr + i % 4 == 3:
#             tmp = find_next_obstruction_left(previous[0], previous[1])
#             previous = tmp
#             points.append(tmp)
#     print(points)
#     print(start)    
#     pass



# def find_next_obstruction_up(x, y):
#     # xx, yy = copy.deepcopy([x, y])
#     while True:
#         if data[y - 1][x] == "#":
#             return [x, y - 1]
#             break
#         y -= 1

# def find_next_obstruction_right(x, y):
#     # xx, yy = copy.deepcopy([x, y])
#     while True:
#         # print(xx, yy)
#         if data[y][x + 1] == "#":
#             return [x + 1, y]
#             break
#         x += 1
        
# def find_next_obstruction_down(x, y):
#     # x, y = copy.deepcopy([x, y])
#     while True:
#         if data[y + 1][x] == "#":
#             return [x, y + 1]
#             break
#         y += 1
        
# def find_next_obstruction_left(x, y):
#     # xx, yy = copy.deepcopy([x, y])
#     while True:
#         if data[y][x - 1] == "#":
#             return [x - 1, y]
#             break
#         x -= 1

# for x, y, dr in moves:
#     a, b, c , d = upcheck(x, y), rightcheck(x, y), downcheck(x, y), leftcheck(x, y)
#     print(a, b, c, d, moves[0])
#     does_it_loop(x, y, dr)
    # exit()



















# find all obstructions (#)
# find all points guard visits
# if 3 obstructions almost create a loop, 
# check if guard visits the point next to the last point going in the right direction to create a loop

# all_obstructions = []
# for y, line in enumerate(data):
#     for x, char in enumerate(line):
#         if char == "#":
#             all_obstructions.append([x, y])
# print(all_obstructions)
# print(moves)
# extract turns from moves
# turns = []
# previous = moves[0][2]
# for x, y, dr in moves:
#     if dr != previous:
#         turns.append([x, y, dr])
#         previous = dr
# # print(turns)
# counter = 0
# for i in range(len(turns)):
#     sl = turns[i:i+3]
#     if len(sl) != 3:
#         break
#     print(sl, data[sl[0][1] - 1][sl[0][0]], data[sl[0][1]][sl[0][0] + 1], data[sl[0][1] + 1][sl[0][0]], data[sl[0][1]][sl[0][0] - 1])

# print(len(turns))
# s = set()
# [s.add(str(a)) for a in turns]
# print(turns, s)


mvs = copy.deepcopy(moves)
for i, mv in enumerate(mvs):
    itercase = i
    print(i, len(mvs))
    # global data
    data = copy.deepcopy(initial_data)
    data[mv[1]][mv[0]] = "#"
    x_coord, y_coord = 59, 77
    # print(data[mv[1]][mv[0]])

    # for y_coord, line in enumerate(copy.deepcopy(initial_data)):
    #     if "^" in line:
    #         x_coord = line.index("^")
    #         print(x_coord, y_coord)
    #         break
    print(x_coord, y_coord)
    # exit()
    moves = []
    turns = []
    move()
    print("loopcounter", loopcounter)
print("loopcounter", loopcounter)