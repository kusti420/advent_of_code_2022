import os
import importlib.util
os.chdir(os.path.dirname(os.path.realpath(__file__)))
folder = int(os.path.dirname(os.path.realpath(__file__)).split("\\")[-1])
module = importlib.util.spec_from_file_location("globals", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\globals.py")
globals = importlib.util.module_from_spec(module)
module.loader.exec_module(globals)
globals.get_input(folder)
data = open(f"{folder}.txt", "r", encoding="utf-8", newline="").read().splitlines()

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
    data2 = max([sum(lst) for lst in data2])
    print(data2) # 69693