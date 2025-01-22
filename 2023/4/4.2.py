if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    
    cards = {}
    for i in range(len(data)):
        cards[i] = 1
    print(cards)
    
    
    for i, line in enumerate(data):
        matches = 0
        multiplier = cards[i]
        line = line.split(": ")[1]
        line = line.split(" | ")
        line = [x.split(" ") for x in line]
        line = [[int(y) for y in x if y != ""] for x in line]
        print(line)
        
        
        for value in line[1]:
            if value in line[0]:
                matches += 1
        
        for x in range(i + 1, i + 1 + matches):
            print(x)
            for y in range(multiplier):
                cards[x] += 1
            # cards[x] += multiplier
        print(cards)
        # print(matches)
    sm = 0
    for key in cards:
        sm += cards[key]
    print(sm)
    
    

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
