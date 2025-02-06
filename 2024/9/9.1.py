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
        [initial_uncompressed.append("𘚟") for _ in range(int(char))]
    else:
        [[initial_uncompressed.append(chr(i // 2)), ln := ln + 1] for _ in range(int(char))]
# print(initial_uncompressed)


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
            if val != "𘚟":
                return idx + 1


    if initial_uncompressed[l] == "𘚟":
        r = find_r()
        tmp = initial_uncompressed[l]
        initial_uncompressed[l] = initial_uncompressed[-r]
        initial_uncompressed[-r] = tmp
    
        if l < r:
            return swap(initial_uncompressed, l + 1)
        else:
            if is_correct(initial_uncompressed):
                return initial_uncompressed
            else:
                return swap(initial_uncompressed, l + 1)
    else:
        return swap(initial_uncompressed, l + 1)

    

compressed = swap(initial_uncompressed, 0)
# print("compressed: ", compressed)

# checksum = 0
result = 0
i = 0
for n in compressed:
    if n == "𘚟":
        break
    result += i*int(ord(n))
    i += 1

print(result) # 6288707484810
end = time.time()
print(end - start) # 12.67971420288086
