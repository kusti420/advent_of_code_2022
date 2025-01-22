if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    import os; exec(open(f"{idk}\\setup.txt").read())
    
    red = 12
    blue = 14
    green = 13
    
    possible_games = []
    
    for line in data:
        
        line = line.split(": ")
        
        gameID = int(line[0].split(" ")[1])
        line = line[1]
        
        line = line.split("; ")
        line = [string.split(", ") for string in line]
        line = [[string.split(" ") for string in lst] for lst in line]
        
        # print(line, len(line))
        
        def parse(lst):
            lst = sorted(lst)
            # print(lst)
            r = 0
            g = 0
            b = 0
            for l in lst:
                
                # print(l)
                match l[1]:
                    case "red":
                        r = int(l[0])
                    case "green":
                        g = int(l[0])
                    case "blue":
                        b = int(l[0])
            return (r, g, b)
            
            
        
        parsed_game = []
        for ln in line:
            parsed_game.append(parse(ln))
        # print(gameID, parsed_game)
        
        impossible = False
        # print(red, green, blue)
        r_max = 0
        g_max = 0
        b_max = 0
        for s in parsed_game:
            # print(s)
            if s[0] > r_max:
                r_max = s[0]
            if s[1] > g_max:
                g_max = s[1]
            if s[2] > b_max:
                b_max = s[2]
        if r_max > red or g_max > green or b_max > blue:
            impossible = True

        if not impossible:
            possible_games.append(gameID)
    print(sum(possible_games), len(possible_games), possible_games) # 2348

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
