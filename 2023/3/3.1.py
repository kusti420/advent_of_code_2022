if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    
    import re
    all_symbols = []
    all_digits = []
    
    adjacent_digits = []
    # digits_counter = []
    for index, line in enumerate(data):
        # print(line)
        # match regex [^\.+|\d]
        # x = re.findall("[^\.+|\d]", line)
        symbols = re.finditer("[^\w.]", line)
        symbols = {match.start(): match.group() for match in symbols}
        # print(symbols)
        
        digits = re.finditer("\d+", line)
        digits = {(int(match.start()), index): int(match.group()) for match in digits}
        
        
        all_symbols.append(symbols)
        all_digits.append(digits)
    
    # print(all_digits)
    
    temp = {}
    for y in range(len(all_symbols)):
        for x in all_symbols[y]:
            # print(x, y, all_symbols[y][x])
            temp[(x, y)] = all_symbols[y][x]
            ...
    # print(temp)
    all_symbols = temp
    
    valid_digits = {}
    for y in range(len(all_digits)):
        # print(y, all_digits[y])
        for xk in all_digits[y]:
            x = xk[0]
            print(x, y, all_digits[y][xk])
            for xx in range(max(x - 1, 0), x+len(str(all_digits[y][xk])) + 2):
                # print(all_digits[y][x], x1)
                # print(xx)
                for symbol in all_symbols:
                    x2, y2 = symbol
                    # print(all_digits[y][xk])
                    if x2 == xx and (y2-1 == y or y2 == y or y2 + 1 == y):
                        # print(symbol)
                        valid_digits[(xx, y)] = all_digits[y][xk]
                        
            # print()
    # print(valid_digits)
    
    
    # for y in range(len(all_digits)):
    #     for xk in all_digits[y]:
    #         x = xk[0]
    #         print(x, y, all_digits[y][xk])
    #         for xx in range(max(x - 1, 0), x+len(str(all_digits[y][xk])) + 1):
    #             for symbol in all_symbols:
    #                 x2, y2 = symbol
    #                 if x2 == xx:
    #                     if y2 - 1 == y or y2 == y or y2 +1 == y:
    #                         valid_digits[(xx, y)] = all_digits[y][xk]
    
    
    print(sum(valid_digits.values()))
    

    print(adjacent_digits)
    

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
