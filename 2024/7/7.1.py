if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    import time
    start = time.time()

    correct = []
    for line in data:
        e = int(line.split(":")[0])
        v = [int(x) for x in line.split(": ")[1].split(" ")]
        for _ in range(max(2**(len(v) - 2), 2)):
            eval = v[0]
            bval = '{:0{}b}'.format(_, len(v) - 1)
            brk = False
            for i, b in enumerate(bval):
                # print(line, bval, v, v[i+1])
                b = int(b)
                if b == 0:
                    eval += v[i+1]
                elif b == 1:
                    eval *= v[i+1]
                if eval == e:
                    correct.append(e)
                    brk = True
                    break
            if brk:
                break
    print(correct, sum(correct)) # 1611660863222 # 3749
    stop = time.time()
    print(stop - start)
