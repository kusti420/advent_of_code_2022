if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    """
    A = Rock
    B = Paper
    C = Scissors

    X = Rock = +1 point
    Y = Paper = +2 points
    Z = Scissors = +3 points

    win = +6 points
    tie = +3 points
    loss = +0 point
    """
    points = 0
    for row in data:
        row = row.split(" ")
        if row[0] == "A":
            if row[1] == "X":
                points += (1 + 3)
            if row[1] == "Y":
                points += (2 + 6)
            if row[1] == "Z":
                points += (3 + 0)
        elif row[0] == "B":
            if row[1] == "X":
                points += (1 + 0)
            if row[1] == "Y":
                points += (2 + 3)
            if row[1] == "Z":
                points += (3 + 6)
        elif row[0] == "C":
            if row[1] == "X":
                points += (1 + 6)
            if row[1] == "Y":
                points += (2 + 0)
            if row[1] == "Z":
                points += (3 + 3)
    print(points) # 8933

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")