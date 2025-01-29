# Solution --------------------------------------------------
import os
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()
import sys
sys.setrecursionlimit(150000)

data = data[0]
input_list = data
print(input_list)

represent = tuple()
file_id = 0
space = 0

for l in input_list:
    if not space:
        for i in range(int(l)):
            represent += (file_id,)
        file_id += 1
        space += 1
    else:
        for i2 in range(int(l)):
            represent += (".",)
        space -= 1

print(represent)

rtl = []
n = 0
for l in represent:
    if l != ".":
        rtl.append(n)
    n += 1

rtl = set(reversed(rtl))
moved = list(represent)
free_space = represent.count(".")

i = 0
for l in represent:
    if l == ".":
        moved[i] = represent[max(rtl)]
        moved[max(rtl)] = "."
        rtl.remove(max(rtl))

        if all(moved[i] == "." for i in range(0-free_space, 0)):
            break
    i += 1

print(moved)

result = 0
i = 0
for n in moved:
    if n == ".":
        break
    result += i*n
    i += 1

print(result,
"is the result of filesystem checksum")
