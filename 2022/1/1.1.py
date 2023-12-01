if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    data2 = []
    lst = []
    for val in data:
        if val != "":
            lst.append(int(val))
        else:
            data2.append(lst)
            lst = []
    data2.append(lst)
    data2 = max([sum(lst) for lst in data2])
    print(data2) # 69693

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
