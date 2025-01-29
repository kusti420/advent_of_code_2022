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
print(data)
id = -1
initial_uncompressed = ""
files = []
class File:
    def __init__(self, is_whitespace, char):
        self.is_whitespace = is_whitespace
        self.ID = self.get_id()
        self.size = int(char)
    
    def get_id(self):
        if self.is_whitespace:
            return None
        global id
        id += 1
        return id
    
    def __repr__(self):
        return str([self.ID, self.size, self.is_whitespace])

for i, char in enumerate(data):
    if i % 2 == 1:
        f = File(True, char)
    else:
        f = File(False, char)
    files.append(f)
print(files)

for file in files:
    if not file.is_whitespace:
        initial_uncompressed += str(file.ID) * file.size
    else:
        initial_uncompressed += "." * file.size
    pass
print(initial_uncompressed)
# print(len("00...111...2...333.44.5555.6666.777.888899"))
i2 = 1
initial_uncompressed = list(initial_uncompressed)

def swap(initial_uncompressed, l):
    print(initial_uncompressed)
    def is_correct(initial_uncompressed):
        first_dot = None
        for idx, char in enumerate(initial_uncompressed):
            if char == "." and first_dot is None:
                first_dot = idx
                continue
            if char != "." and first_dot is not None:
                if first_dot < idx:
                    return False
        return True

    def find_r():
        for idx, val in enumerate(reversed(initial_uncompressed)):
            if val != ".":
                return idx + 1

    if initial_uncompressed[l] == ".":
        r = find_r()
        tmp = initial_uncompressed[l]
        initial_uncompressed[l] = initial_uncompressed[-r]
        initial_uncompressed[-r] = tmp

    if is_correct(initial_uncompressed):
        return initial_uncompressed

    return swap(initial_uncompressed, l + 1)

compressed = swap(initial_uncompressed, 0)
print("compressed: ", compressed)

# checksum = 0
result = 0
i = 0
for n in compressed:
    if n == ".":
        break
    result += i*int(n)
    i += 1

print(result)

end = time.time()
print(end - start)
