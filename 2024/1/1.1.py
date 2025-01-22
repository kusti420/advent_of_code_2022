if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("/")[-1]
    idk = idk.replace(f"/{year}", "")
    print(idk)
    import os; exec(open(f"{idk}/setup.txt").read())

    left = []
    right = []
    sm = 0
    for line in data:
        line = [int(i) for i in line.split()]
        # print(line)
        left.append(line[0])
        right.append(line[1])
        # sm += abs(line[0] - line[1])
    # print(data)
    right.sort()
    left.sort()
    # print(sorted(left))
    # print(sorted(right))
    values = []
    for i in range(len(left)):
        values.append(abs(left[i] - right[i]))
    for i in left:
        sm += i * right.count(i)
    print(sum(values), len(values))
    print(sm)



if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
