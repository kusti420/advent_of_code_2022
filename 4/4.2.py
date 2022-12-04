if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/setup.txt").read())
    data = [[x.split(",")[0].split("-"), x.split(",")[1].split("-")] for x in data]
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j])):
                data[i][j][k] = int(data[i][j][k])
    data2 = []
    for lst in data:
        for i in range(lst[1][0], lst[1][1] + 1):
            if range(lst[0][0], lst[0][1] + 1).__contains__(i):
                data2.append(i)
                break
    
    print(len(data2)) # 914

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")