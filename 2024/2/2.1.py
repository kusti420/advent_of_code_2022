import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data

data = [[int(x) for x in line.split(" ")] for line in data]
safe = 0
unsafe = 0
usafe = []
for line in data:
    def test(line):
        if len(list(set(line))) != len(line):
            return False
        if list(sorted(line)) != line:
            if list(sorted(line)) != list(reversed(line)):
                return False
        isGrowing = None
        for i in range(len(line) - 1):
            if 1 <= line[i] - line[i + 1] <= 3:
                isGrowing = False
            elif -1 >= line[i] - line[i + 1] >= -3:
                isGrowing = True
            else:
                return False
            if isGrowing:
                if 1 <= line[i] - line[i + 1] <= 3:
                    return False
            if not isGrowing:
                if -1 >= line[i] - line[i + 1] >= -3:
                    return False
        return True
    if test(line) == False:
        unsafe += 1
        usafe.append(line)
    else:
        safe += 1
print(safe) # part 1
for case in usafe:
    res = []
    for i in range(len(case)):
        c = case[0:i] + case[i+1:]
        res.append(test(c))
    if any(res):
        unsafe -= 1
        safe += 1
print(safe) # part 2
