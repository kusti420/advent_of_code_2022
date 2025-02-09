import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from functions import *
f = init(os.getcwd())
data = f.data
import time

import copy
start = time.time()

rules = [[int(y) for y in x.split("|")] for x in data[:data.index("")]]
cases = [[int(y) for y in x.split(",")] for x in data[data.index("")+1:]]
# print(cases)

r = {}
for rule in rules:
    if rule[0] not in r:
        r[rule[0]] = set([rule[1]])
    elif rule[1] not in r:
        r[rule[1]] = set()
        r[rule[0]] = set([rule[1]])
    else:
        r[rule[0]] = r[rule[0]].union(set([rule[1]]))


tmp = set()
for rule in rules:
    tmp.add(rule[0])
    tmp.add(rule[1])

correct = []
incorrect = []
# part 1
for case in cases:
    def iscorrect(case):
        for i in range(len(case)):
            for b in range(len(case)):
                if i == b:
                    continue
                if b < i:
                    if [case[b], case[i]] in rules:
                        continue
                    else:
                        return False
                if b > i:
                    if [case[i], case[b]] in rules:
                        continue
                    else:
                        return False
        return iscorrect
    if iscorrect(case):
        correct.append(case)
    else: # part 2
        incorrect.append(case)
print(sum([x[len(x) >> 1] for x in correct])) # part 1 # 5275
mid = time.time()

fixed = []
for case in incorrect:
    tmp = copy.copy(case)
    for i in range(len(case)):
        for b in range(len(case)):
            if i == b:
                continue
            if b < i:
                if [tmp[b], tmp[i]] in rules:
                    continue
                else:
                    tmpval = tmp[b]
                    tmp[b] = tmp[i]
                    tmp[i] = tmpval
            elif b > i:
                if [tmp[i], tmp[b]] in rules:
                    continue
                else:
                    tmpval = tmp[b]
                    tmp[b] = tmp[i]
                    tmp[i] = tmpval
    fixed.append(tmp)

print(sum([x[len(x) >> 1] for x in fixed])) # part 2 # 6191
end = time.time()
print(mid - start, end - start)

