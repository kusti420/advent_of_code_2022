import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data
data = [[int(y) for y in x.split(" ")] for x in data][0]

print(data)


def blink(blinks = 1, end = 25, stones = data):
    tmp = []
    def rule1(stone):
        if stone == 0:
            return [1]
        return None
    def rule2(rule1, stone):
        if r1 is None:
            stone_string = str(stone)
            if len(stone_string) % 2 == 0:
                return [int(stone_string[:len(stone_string) // 2]), int(stone_string[len(stone_string) // 2:])]
        return None
    def rule3(rule1, rule2, stone):
        if rule1 is None and rule2 is None:
            return [stone * 2024]
        return None
    
    for stone in stones:
        r1 = rule1(stone)
        r2 = rule2(r1, stone)
        r3 = rule3(r1, r2, stone)
        for x in [r1, r2, r3]:
            if x is not None:
                tmp.extend(x)
    # print(tmp)
    # print()
    print(blinks)
    if blinks == end:
        return tmp
    return blink(blinks + 1, end, tmp)
    pass

stones_after_blinks = blink()
print(len(stones_after_blinks)) # part 1 # 186203