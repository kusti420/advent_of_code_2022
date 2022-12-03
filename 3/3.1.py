if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    matches = []
    for line in data:
        line = [line[0:int(len(line)/2)], line[int(len(line)/2):len(line)]]
        for char in line[1]:
            if line[0].__contains__(char):
                matches.append(char)
                break
    matches = [ord(match) % ord('a') + 1 if match.islower() else ord(match) % ord('A') + 26 + 1 for match in matches]
    print(sum(matches))

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")