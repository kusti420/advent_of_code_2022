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
        self.start = self.start()

    def get_session_id(self):
        with open(f"{self.ROOT}/session_id.txt", "r", encoding="utf-8", newline="") as f:
            session_id = f.read()
        return session_id

    def get_input(self):
        if os.path.isfile(f"{self.path}/{self.folder}.txt"):
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
    
    def start(self):
        return time.time()
    
    def end(self):
        return time.time()-self.start

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

def init(path):
    ff = f(path)
    return ff

def upcheck2x2(data:list[list[any]] = None, x:int = None, y:int = None, value_to_check_for:any = None):
    try:
        if y == 0:
            return False
        elif data[y - 1][x] == value_to_check_for:
            return True
        else:
            return False
    except:
        return False

def rightcheck2x2(data:list[list[any]] = None, x:int = None, y:int = None, value_to_check_for:any = None):
    try:
        if x == len(data[0]):
            return False
        elif data[y][x + 1] == value_to_check_for:
            return True
        else:
            return False
    except:
        return False

def downcheck2x2(data:list[list[any]] = None, x:int = None, y:int = None, value_to_check_for:any = None):
    try:
        if y == len(data):
            return False
        elif data[y + 1][x] == value_to_check_for:
            return True
        else:
            return False
    except:
        return False

def leftcheck2x2(data:list[list[any]] = None, x:int = None, y:int = None, value_to_check_for:any = None):
    try:
        if x == 0:
            return False
        elif data[y][x - 1] == value_to_check_for:
            return True
        else:
            return False
    except:
        return False

def array_swap(array:list[any], index1:int, index2:int):
    array[index1], array[index2] = array[index2], array[index1]
    return array

def string_swap(string:str, index1:int, index2:int):
    string_list = array_swap(list(string), index1, index2)
    return "".join(string_list)

