import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data
# print("data", data)

data = [list([int(x) for x in line]) for line in data]
trailheads = [[x, y] for y, line in enumerate(data) for x, char in enumerate(line) if char == 0]
# print(data, trailheads)
# print(*data, sep="\n")
# print(trailheads)

trail_dict = {}
for x, y in trailheads:
    if (x, y) not in trail_dict:
        trail_dict[(x, y)] = []
# print(trail_dict)

def move(start_x:int, start_y:int, x:int, y:int, current_value:int, end_value:int):
    global trail_dict
    if current_value == end_value:
        trail_dict[(start_x, start_y)].append((x, y))
        return trail_dict
    else:
        if upcheck2x2(data, x, y, current_value + 1) == True:
            move(start_x, start_y, x, y - 1, current_value + 1, end_value)
        if rightcheck2x2(data, x, y, current_value + 1) == True:
            move(start_x, start_y, x + 1, y, current_value + 1, end_value)
        if downcheck2x2(data, x, y, current_value + 1) == True:
            move(start_x, start_y, x, y + 1, current_value + 1, end_value)
        if leftcheck2x2(data, x, y, current_value + 1) == True:
            move(start_x, start_y, x - 1, y, current_value + 1, end_value)
    return trail_dict

for x, y in trailheads:
    # print(x, y)
    # exit()
    move(x, y, x, y, data[y][x], 9)
# print(trail_dict)
sm = 0
for k, v in trail_dict.items():
    if len(v) > 0:
        sm += len(v)
print(sm) # part 2 # 1034
print(f.end())

