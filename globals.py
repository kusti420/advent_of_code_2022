import os
import requests
import time

old_dir = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path = os.path.dirname(os.path.realpath(__file__))
YEAR = time.localtime().tm_year
YEAR = 2024

def get_session_id():
    with open(f"{path}/session_id.txt", "r", encoding="utf-8", newline="") as f:
        session_id = f.read()
    return session_id

def get_input(folder):
    dir = f"{os.path.dirname(os.path.realpath(__file__))}\\{YEAR}\\{folder}"
    print(dir)
    if os.path.isfile(f"{dir}\\{folder}.txt"):
        return
    with open(f"{dir}\\{folder}.txt", "w", encoding="utf-8", newline="") as f:
        f.write(requests.get(f"https://adventofcode.com/{YEAR}/day/{folder}/input", cookies={"session": get_session_id()}).text)
os.chdir(old_dir)
