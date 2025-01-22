if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("/")[-1]
    idk = idk.replace(f"/{year}", "")
    print(idk)
    import os; exec(open(f"{idk}/setup.txt").read())

    #allmatches = []
    # print(data)
    import re
    # print(len(data), data[5])
    data = "".join(data)
    matches = re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", data)
    sm = 0
    sm2 = 0
    for m in matches:
        case = re.findall(r"\d*,\d*", m)
        if case == []:
            continue
        case = case[0]
        l,r = [int(v) for v in case.split(",")]
        sm2 += l*r
    print(sm2)
    mult=True
    for m in matches:
        if mult == False:
            if m == "do()":
                mult = True
        if mult == True:
            if m == "don't()":
                mult = False
        if mult == True:
            try:
                case = re.findall(r"\d*,\d*", m)
                case = case[0]
                l,r = [int(v) for v in case.split(",")]
                sm += l*r
            except:
                pass
    print(sm)
