if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("/")[-1]
    idk = idk.replace(f"/{year}", "")
    print(idk)
    import os
    exec(open(f"{idk}/setup.txt").read())
    #import numpy as np


    correct = []
    for line in data:

        e = int(line.split(":")[0])
        v = [int(x) for x in line.split(": ")[1].split(" ")]
        # eval = v[0]
        for _ in range(max(2**(len(v) - 1), 2)):
            #print('{:0{}b}'.format(i, len(v) - 1))
            eval = v[0]
            bval = '{:0{}b}'.format(_, len(v) - 1)
            def decimal_to_base3(num):
                if num == 0:
                    return '0'
                base3 = ''
                while num > 0:
                    base3 = str(num % 3) + base3
                    num = num // 3
                return base3
            #bval = decimal_to_base3(_)
            print(bval, v, e, correct)
            brk = False
            for i, b in enumerate(bval):
                # print(bval, b, i)
                b = int(b)
                print(b == 0, b == 1)
                print(eval, v[i+1])
                if b == 0:
                    eval += v[i+1]
                if b == 1:
                    # print(eval)
                    eval *= v[i+1]
                if b == "2":
                    eval = int(str(eval) + str(v[i+1]))
                if eval == e:
                    correct.append(e)
                    brk = True
                    #for i in range(100):
                    #    print(correct)
                    break
                #break
            if brk:
                break
        # exit()
            #print()
    print(correct, sum(correct))
