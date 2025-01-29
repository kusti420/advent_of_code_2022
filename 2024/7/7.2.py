if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    import time
    start = time.time()

    correct = set()
    for line in data:
        e = int(line.split(":")[0])
        # print(e), exit()
        try:
            numbers = [int(x) for x in line.split(": ")[1].split(" ")]
        except:
            numbers = line.split(": ")[1].split(" ")
            print(tmp)
        # print(numbers), exit()
        def to_base3(num, length):
            base3 = ''
            while num > 0:
                base3 = str(num % 3) + base3
                num //= 3
            return base3.zfill(length)
        answer = numbers[0]
        bvals = []
        for _ in range(3**(len(numbers) - 1)):
            if len(numbers) == 1:
                # bvals.append(to_base3(_, len(numbers)))
                brk = True
                if answer == e:
                    correct.append(e)
                    print("correct", line)
                break
            else:
                bvals.append(to_base3(_, len(numbers) - 1))
            
        
        # print(bvals, len(bvals), 3**(len(numbers) - 1), len(set(bvals))), exit()
        for bval in bvals:
            answer = numbers[0]
            for i, b in enumerate(bval):
                # print(line, bval, v, v[i+1])
                b = int(b)
                # print(b)
                if b == 0:
                    answer += numbers[i+1]
                elif b == 1:
                    answer *= numbers[i+1]
                elif b == 2:
                    answer = int(str(answer) + str(numbers[i+1]))
            if answer == e:
                correct.add(e)
                print("correct", line)
                break

    print(correct, sum(correct)) # 945341732469724
    stop = time.time()
    print(stop - start)
