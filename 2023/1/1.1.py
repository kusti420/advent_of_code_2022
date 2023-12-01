if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    print(idk)
    import os; exec(open(f"{idk}\\setup.txt").read())
    
    # print(data)
    calibration_values = []
    for line in data:
        firstchar = None
        lastchar = None
        for i in range(len(line)):
            if line[i].isnumeric() and firstchar is None:
                firstchar = line[i]
            if line[~i].isnumeric() and lastchar is None:
                lastchar = line[~i]
            if firstchar is not None and lastchar is not None:
                calibration_values.append(int(firstchar + lastchar))
                break
    print(sum(calibration_values))

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
