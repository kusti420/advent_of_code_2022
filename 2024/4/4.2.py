import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data

counter = 0
for i in range(len(data) - 2):
    for j in range(len(data[i])-2):
        x = [d[j:j+3] for d in data[i:i+3]]
        if x[0][0] + x[1][1] + x[2][2] == "MAS" or x[0][0] + x[1][1] + x[2][2] == "SAM":
            if x[0][2] + x[1][1] + x[2][0] == "MAS" or x[0][2] + x[1][1] + x[2][0] == "SAM":
                counter+=1
print(counter) # part 2 # 1941

