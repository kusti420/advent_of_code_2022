import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data

counter = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j:j+4] == "XMAS" and len(data[i]) >= j+4:
            counter+=1
        if data[i][j:j+4] == "SAMX" and len(data[i]) >= j+4:
            counter+=1
        if i+4 <= len(data):
            d = data[i:i+4]
            if "".join([x[j] for x in d]) == "XMAS":
                counter+=1
            if "".join([x[j] for x in d]) == "SAMX":
                counter+=1
        if i+4 <= len(data):
            d = data[i:i+4]
            if j+4 <= len(d[0]):
                ln = [data[i+n][j+n] for n in range(len(d))]
                ln = "".join(ln)
                if ln == "XMAS" or ln == "SAMX":
                    counter+=1
            if j-3 >= 0:
                ln2 = [data[i+n][j-n] for n in range(len(d))]
                ln2 = "".join(ln2)
                if ln2 == "XMAS" or ln2 == "SAMX":
                    counter+=1
print(counter) # part 1 # 2532

