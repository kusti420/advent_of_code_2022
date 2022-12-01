import os
import requests

old_dir = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path = os.path.dirname(os.path.realpath(__file__))

def get_session_id():
    with open(f"{path}/session_id.txt", "r", encoding="utf-8", newline="") as f:
        session_id = f.read()
    return session_id

def get_input(folder):
    dir = f"{os.path.dirname(os.path.realpath(__file__))}\\{folder}"
    if os.path.isfile(f"{dir}\\{folder}.txt"):
        return
    with open(f"{dir}/{folder}.txt", "w", encoding="utf-8", newline="") as f:
        f.write(requests.get(f"https://adventofcode.com/2022/day/{folder}/input", cookies={"session": get_session_id()}).text)
# get_input(1)
os.chdir(old_dir)
