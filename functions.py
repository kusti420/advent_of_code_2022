import sys, os, time, requests

class f:
    def __init__(self, path):
        self.path = path
        self.deliminator = self.get_deliminator()
        self.YEAR = int(path.split(self.deliminator)[-2])
        self.ROOT = os.path.dirname(os.path.realpath(__file__))
        self.folder = int(path.split(self.deliminator)[-1])
        
        self.session_id = self.get_session_id()
        self.get_input()
        self.data = self.get_data()

    def get_session_id(self):
        with open(f"{self.ROOT}/session_id.txt", "r", encoding="utf-8", newline="") as f:
            session_id = f.read()
        return session_id

    def get_input(self):
        if os.path.isfile(f"{dir}/{self.folder}.txt"):
            return
        with open(f"{self.path}/{self.folder}.txt", "w", encoding="utf-8", newline="") as f:
            f.write(requests.get(f"https://adventofcode.com/{self.YEAR}/day/{self.folder}/input", cookies={"session": self.session_id}).text)
            f.close()

    def get_data(self):
        self.data = open(f"{self.path}/{self.folder}.txt", "r", encoding="utf-8", newline="").read().splitlines()
        return self.data

    def get_deliminator(self):
        OS = sys.platform
        if OS == "win32":
            deliminator = "\\"
        else:
            deliminator = "/"
        return deliminator

def timer(func):
    def start():
        global start_time
        start_time = time.time()
    def end():
        global end_time
        end_time = time.time()
        print(end_time - start_time)
    start()
    func()
    end()

def meme():
    print("meme")

def init(path):
    ff = f(path)
    return ff
