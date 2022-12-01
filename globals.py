import os
import requests
import sys

old_dir = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path = os.path.dirname(os.path.realpath(__file__))
# print(path)
# print("path is", path)
sys.path.append(path)

def get_session_id():
    with open(f"{path}/session_id.txt", "r", encoding="utf-8", newline="") as f:
        session_id = f.read()
    return session_id

# print(get_session_id())

def get_input(folder):
    dir = os.path.dirname(os.path.realpath(__file__))
    # chdir to dr/{folder}
    dir = dir + f"\\{folder}"
    # print(dir)
    # if dir/{folder}.txt exists, return
    if os.path.isfile(f"{dir}\\{folder}.txt"):
        # print(f"{dir}\\{folder}.txt exists")
        return
    with open(f"{dir}/{folder}.txt", "w", encoding="utf-8", newline="") as f:
        f.write(requests.get(f"https://adventofcode.com/2022/day/{folder}/input", cookies={"session": get_session_id()}).text)
# get_input(1)
os.chdir(old_dir)