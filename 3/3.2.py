if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())

    data = [[data[i], data[i+1], data[i+2]] for i in range(0, len(data), 3)]
    matches = []
    for lst in data:
        for char in lst[0]:
            if lst[1].__contains__(char) and lst[2].__contains__(char):
                matches.append(char)
                break
    matches = [ord(match) % ord('a') + 1 if match.islower() else ord(match) % ord('A') + 26 + 1 for match in matches]
    print(sum(matches))

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")