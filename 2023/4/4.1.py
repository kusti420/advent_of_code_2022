if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    
    points = 0
    
    for line in data:
        p = 1
        line = line.split(": ")[1]
        line = line.split(" | ")
        line = [x.split(" ") for x in line]
        line = [[int(y) for y in x if y != ""] for x in line]
        print(line)
        for value in line[1]:
            if value in line[0]:
                p *= 2
        if p == 1:
            p = 0
        else:
            p = int(p / 2)
        points += p
    print(points)
    
    

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
