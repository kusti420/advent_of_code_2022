import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from functions import *
os.chdir(os.path.dirname(os.path.realpath(__file__)))
f = init(os.getcwd())
data = f.data
# print("data", data)

data = [list([int(x) for x in line]) for line in data]
trailheads = [[x, y] for y, line in enumerate(data) for x, char in enumerate(line) if char == 0]
print(data, trailheads)


answer = 0
def upcheck(x, y):
    if y == 0:
        return None
    elif data[y - 1][x] == "#":
        return 0
    else:
        return 1
    
    
    
for i, [x, y] in enumerate(trailheads):
    def move(x, y):
        score = 0
        return score
    answer += move(x, y)

