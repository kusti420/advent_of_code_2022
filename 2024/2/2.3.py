import os
idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
year = idk.split("\\")[-1]
idk = idk.replace(f"\\{year}", "")
print(idk)
exec(open(f"{idk}\\setup.txt").read())
import time
start = time.time()

def isIncreasingOrDecreasing (levels: list) -> bool:
    result = None
    increasingReport = sorted(levels , key=lambda x: int(x))
    decreasingReport = sorted(levels, reverse=True, key=lambda x: int(x))
    print(increasingReport)
    if levels == increasingReport or levels == decreasingReport:
        result = True
    else:
        result = False
    for i in range(len(levels) -1): 
        if int(levels[i]) == int(levels[i+1]):
            result = False
    return result

def isSafeDiff(levels: list) -> bool:
    result = None
    for i in range(len(levels) -1):
        diff = int(levels[i]) - int(levels[i+1])
        if not max(diff, -diff) <=3:
            result = False
            break
        else:
            result = True
    return result
if __name__ == "__main__":
    with open("2.txt", 'r') as inputFile:
        reports = inputFile.readlines() 
        safeReports = 0
        for i in range(len(reports)):
            # levels = [int(x) for x in reports[i].split()]
            levels = reports[i].split()
            if isIncreasingOrDecreasing (levels) and isSafeDiff(levels):
                safeReports = safeReports + 1
        print(safeReports)
end = time.time()