if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    print(idk)
    import os; exec(open(f"{idk}\\setup.txt").read())
    
    nrs = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]
    
    def txt_to_int(string):
        match string:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9
            case _:
                return 0

    
    # print(data)
    calibration_values = []
    for line in data:
        firstchar = None
        lastchar = None
        
        for i in range(len(line)):
            if line[i].isnumeric() and firstchar is None:
                firstchar = line[i]
                minindex = None
                for nr in nrs:
                    try:
                        if minindex is None or line.index(nr) < minindex:
                            minindex = line.index(nr)
                    except:
                        pass
                # print(line, firstchar, minindex, line.index(firstchar))
                if minindex != None and minindex < line.index(firstchar):
                    temp = line[minindex:line.index(firstchar)]
                    for i2 in range(3, 6, 1):
                        # print(i)
                        if temp[:i2] in nrs:
                            v = txt_to_int(temp[:i2])
                            if i2 != 0:
                                firstchar = str(v)

            # print(line, i)
            if line[~i].isnumeric() and lastchar is None:
                lastchar = line[~i]
                maxindex = None
                for nr in nrs:
                    try:
                        if maxindex is None or line.rindex(nr) > maxindex:
                            maxindex = line.rindex(nr)
                    except:
                        pass
                # print(line, lastchar, maxindex, line.rindex(lastchar))
                
                if maxindex != None and maxindex > line.rindex(lastchar):
                    temp = line[maxindex:]
                    # print(line, temp)
                    for i2 in range(3, 6, 1):
                        # print(i)
                        if temp[:i2] in nrs:
                            v = txt_to_int(temp[:i2])
                            if i2 != 0:
                                lastchar = str(v)
                
                
            if firstchar is not None and lastchar is not None:
                calibration_values.append(int(firstchar + lastchar))
                break
    print(sum(calibration_values))

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
