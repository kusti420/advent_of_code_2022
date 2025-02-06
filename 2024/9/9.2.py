import os
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()
import sys
sys.setrecursionlimit(15000000)

data = data[0]
# print(data)
initial_uncompressed = []

ln = 0
for i, char in enumerate(data):
    if i % 2 == 1:
        # [initial_uncompressed.append("𘚟") for _ in range(int(char))]
        initial_uncompressed.append(["𘚟", int(char)])
    else:
        # [[initial_uncompressed.append(chr(i // 2)), ln := ln + 1] for _ in range(int(char))]
        initial_uncompressed.append([chr(i // 2), int(char)])
        ln += int(char)
print(initial_uncompressed)
# exit()


def swap(initial_uncompressed, l):
    # print(initial_uncompressed)
    def is_correct(initial_uncompressed):
        # first_dot = None
        # for idx, char in enumerate(initial_uncompressed):
        #     if char == "𘚟" and first_dot is None:
        #         first_dot = idx
        #         continue
        #     if char != "𘚟" and first_dot is not None:
        #         if first_dot < idx:
        #             return False
        # return True # old method
        
        for idx in range(len(initial_uncompressed) - ln):
            if initial_uncompressed[idx + ln] != "𘚟":
                return False
        return True

    def find_r():
        for idx, val in enumerate(reversed(initial_uncompressed)):
            if val[0] != "𘚟":
                return idx + 1


    if initial_uncompressed[l][0] == "𘚟":
        r = find_r()
        if initial_uncompressed[r][1] == initial_uncompressed[l][1]:
            tmp = initial_uncompressed[l]
            initial_uncompressed[l] = initial_uncompressed[-r]
            initial_uncompressed[-r] = tmp
        elif initial_uncompressed[l][1] > initial_uncompressed[r][1]:
            tmpl = initial_uncompressed[l]
            tmpr = initial_uncompressed[r]
            initial_uncompressed = initial_uncompressed[:initial_uncompressed.index(tmpl)] + tmpr + [tmpl[0], tmpl[1] - tmpr[1]] + initial_uncompressed[initial_uncompressed.index(tmpl) + 2:]
    
        if l < r:
            return swap(initial_uncompressed, l + 1)
        else:
            if is_correct(initial_uncompressed):
                return initial_uncompressed
            else:
                return swap(initial_uncompressed, l + 1)
    else:
        if l + 1 >= len(initial_uncompressed):
            return initial_uncompressed
        return swap(initial_uncompressed, l + 1)

    

compressed = swap(initial_uncompressed, 0)
print("compressed: ", [[ord(x[0]), x[1]] for x in compressed])

# checksum = 0
result = 0
i = 0
for n in compressed:
    if n[0] == "𘚟":
        continue
    for char in range(n[1]):
        # result += i*int(ord(n[0]))
        # i += 1
        result += i*ord(n[0])
        i += 1

print(result) # 6288707484810
end = time.time()
print(end - start) # 12.67971420288086
