import os
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()

print(*data, sep="\n")

# find antennas
antennas = dict()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char not in antennas and char != ".":
            antennas[char] = set([(x, y)])
        elif char in antennas:
            antennas[char].add((x, y))
print(antennas)

antinodes = set()

def add_node(ant, diff):
    global antinodes
    x, y = [ant[i] - diff[i] for i in range(2)]
    if x < 0 or x > len(data[0]) - 1 or y < 0 or y > len(data) - 1:
        return
    else:
        antinodes.add((x, y))
        add_node([x, y], diff)




for key in antennas:
    for antenna in antennas[key]:
        x1, y1 = antenna
        for antenna2 in antennas[key]:
            x2, y2 = antenna2
            if antenna != antenna2:
                diff = [antenna2[i] - antenna[i] for i in range(2)]
                dx, dy = diff
                # print(diff, antenna, antenna2)
                # tmp = [[antenna2[i] - diff[i] for i in range(2)], [antenna2[i] + diff[i] for i in range(2)], \
                #     [antenna[i] - diff[i] for i in range(2)], [antenna[i] + diff[i] for i in range(2)]]
                # tmp.remove([x1, y1])
                # tmp.remove([x2, y2])
                # # print(len(tmp))
                # [antinodes.add(tuple(x)) for x in tmp] # part 1
                add_node(antenna, diff) # part 2
                add_node(antenna, [dx * -1, dy * -1])
# print(*data, sep="\n")

not_in_map = set()
for antinode in antinodes:
    x, y = antinode
    if x < 0 or x > len(data[0]) - 1:
        not_in_map.add(tuple(antinode))
    if y < 0 or y > len(data) - 1:
        not_in_map.add(tuple(antinode))
print(antinodes)
print(len(antinodes)-len(not_in_map))
print("time:", time.time()-start)
