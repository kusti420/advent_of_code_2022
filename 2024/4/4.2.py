if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("/")[-1]
    idk = idk.replace(f"/{year}", "")
    print(idk)
    import os
    exec(open(f"{idk}/setup.txt").read())


    counter = 0
    for i in range(len(data) - 2):
        for j in range(len(data[i])-2):
            # print(data[i:i+3], [d[j:j+3] for d in data[i:i+3]])
            x = [d[j:j+3] for d in data[i:i+3]]
            if x[0][0] + x[1][1] + x[2][2] == "MAS" or x[0][0] + x[1][1] + x[2][2] == "SAM":
                if x[0][2] + x[1][1] + x[2][0] == "MAS" or x[0][2] + x[1][1] + x[2][0] == "SAM":
                    counter+=1
            #print(*x, sep="\n")
            #print()
    print(counter) # 1941

