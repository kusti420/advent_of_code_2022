import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())

if __name__ == "__main__":
    data2 = []
    lst = []
    for val in data:
        if val != "":
            lst.append(int(val))
        else:
            data2.append(lst)
            lst = []
    data2.append(lst)
    data2 = sorted(([sum(lst) for lst in data2]), reverse=True)
    print(sum(data2[0:3])) # 200945