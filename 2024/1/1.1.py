import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data

left = []
right = []
sm = 0
for line in data:
    line = [int(i) for i in line.split()]
    left.append(line[0])
    right.append(line[1])

right.sort()
left.sort()

values = []
for i in range(len(left)):
    values.append(abs(left[i] - right[i]))
for i in left:
    sm += i * right.count(i)
print(sum(values)) # part 1
print(sm) # part 2



