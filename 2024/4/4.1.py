if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("/")[-1]
    idk = idk.replace(f"/{year}", "")
    print(idk)
    import os
    exec(open(f"{idk}/setup.txt").read())


    counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # print(data[i], data[i][j:j+4])
            if data[i][j:j+4] == "XMAS" and len(data[i]) >= j+4:
                counter+=1
            if data[i][j:j+4] == "SAMX" and len(data[i]) >= j+4:
                counter+=1
            # print(counter) 5
            if i+4 <= len(data):
                # print(data[i:i+4])
                d = data[i:i+4]
                #print("".join([x[j] for x in d]))
                #print(*data[i:i+4], sep="\n")
                #print(counter, "".join([x[j] for x in d]) == "SAMX" or "".join([x[j] for x in d]) == "XMAS")
                if "".join([x[j] for x in d]) == "XMAS":
                    counter+=1
                    #print(counter)
                if "".join([x[j] for x in d]) == "SAMX":
                    counter+=1
                    #print(counter)
                #print()
            if i+4 <= len(data):
                d = data[i:i+4]
                if j+4 <= len(d[0]):
                    ln = [data[i+n][j+n] for n in range(len(d))]
                    ln = "".join(ln)
                    # print(ln)
                    if ln == "XMAS" or ln == "SAMX":
                        counter+=1
                if j-3 >= 0:
                    ln2 = [data[i+n][j-n] for n in range(len(d))]
                    ln2 = "".join(ln2)
                    if ln2 == "XMAS" or ln2 == "SAMX":
                        counter+=1
    print(counter) # 2532

