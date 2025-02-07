import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data
data = [[int(y) for y in x.split(" ")] for x in data][0]
import copy

def rule1(stone):
    if stone == 0:
        # return [1]
        return True
    return False
def rule2(rule1, stone):
    if rule1 is False:
        stone_string = str(stone)
        if len(stone_string) % 2 == 0:
            # return [int(stone_string[:len(stone_string) // 2]), int(stone_string[len(stone_string) // 2:])]
            return True
    return False
# def rule3(rule1, rule2, stone):
#     if rule1 is False and rule2 is False:
#         # return [stone * 2024]
#         return True
#     return False

def r(r1, r2, stone):
    if r1:
        return [1]
    elif r2:
        stone_string = str(stone)
        return [int(stone_string[:len(stone_string) // 2]), int(stone_string[len(stone_string) // 2:])]
    else:
        return [stone * 2024]

dt = {}
for x in data:
    dt[x] = 1
print(dt)
# after = {}
count = {}
cache = {}
for stone in data:
    count[stone] = 1
    # cache[stone] = []
def blink(data, start = 1, end = 25):
    dt = {}
    count = {}
    for stone in data:
        if stone in cache:
            new_stone = cache[stone]
        else:
            new_stone = r(rule1(stone), rule2(rule1(stone), stone), stone)
            cache[stone] = new_stone
        tmp = data[stone]
        for st in new_stone:
            # print(st)
            if st not in dt:
                dt[st] = tmp
            else:
                dt[st] += tmp
            # data.pop(stone)
            
    # data = dt
    print(start)
    if start == end:
        return dt
    return blink(dt, start + 1, end)
# count.pop(data[0], None)

x = blink(dt, 1, 75)
# print(x)
print(sum([v for v in x.values()])) # 221291560078593
print(f.end())