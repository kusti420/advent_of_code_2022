import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data
data = [[int(y) for y in x.split(" ")] for x in data][0]

print(data)

cache = {}

def blink(blinks = 1, end = 25, stones = data):
    global cache
    tmp = []
    def rule1(stone):
        if stone == 0:
            return [1]
        return None
    def rule2(stone):
        stone_string = str(stone)
        if len(stone_string) % 2 == 0:
            return [int(stone_string[:len(stone_string) // 2]), int(stone_string[len(stone_string) // 2:])]
        return None
    def rule3(rule1, rule2, stone):
        if rule1 is None and rule2 is None:
            return [stone * 2024]
        return None
    
    for stone in stones:
        if stone in cache:
            tmp.extend(cache[stone])
            if blinks == end:
                return tmp
            return blink(blinks + 1, end, tmp)
        r1 = rule1(stone)
        r2 = rule2(stone)
        r3 = rule3(r1, r2, stone)
        if r1 is not None:
            tmp.extend(r1)
            cache[stone] = r1
        elif r1 is None and r2 is not None:
            tmp.extend(r2)
            cache[stone] = r2
        elif r1 is None and r2 is None:
            tmp.extend(r3)
            cache[stone] = r3
            
    # print(tmp)
    # print()
    print(blinks)
    if blinks == end:
        return tmp
    return blink(blinks + 1, end, tmp)
    pass

stones_after_blinks = blink()
print(len(stones_after_blinks))