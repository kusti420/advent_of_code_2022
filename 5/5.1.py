if __name__ == "__main__":
    import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/setup.txt").read())
    import re
    # print(data)
    board_list = data[0: data.index("")]
    instructions = data[data.index("")+1:]
    # print(board_list)
    """
    move 0 from 1 to 2
    """
    class board:
        def __init__(self, board_list, instructions):
            # self.board = [i.replace("[", " ").replace("]", " ") for i in board_list]
            self.board_list = board_list
            self.board = self.parse_board()
            self.instructions = [self.parse_move(move) for move in instructions]
            self.solve()
            pass

        def __repr__(self):
            print(*self.board, sep = "\n")

        def parse_board(self):
            self.board_list = [list(s) for s in self.board_list]
            for i in range(len(self.board_list[-1])):
                for i in range(len(self.board_list[-1])):
                    # print(self.board_list[-1][i])
                    if self.board_list[-1][i] == " ":
                        self.board_list = [lst[:i] + lst[i + 1:] for lst in self.board_list]
                        break
            return self.board_list

        def parse_move(self, move):
            return [int(i) for i in re.split(r"(\d+)", move) if i.isdigit()]
            pass

        def move(self, move):
            moves, from_, to_ = list(range(move[0])), move[1] - 1, move[2] - 1
            # rint(moves, from_ + 1, to_ + 1)
            def find_height(board, from_, to_):
                h1, h2 = None, None
                for i in range(len(self.board)):
                    if self.board[i][from_] != " " and h1 == None:
                        h1 = i
                    if self.board[i][to_] != " " and h2 == None:
                        h2 = i
                    if h1 != None and h2 != None:
                        return h1, h2

            def mv(from_, to_, h1, h2):
                tmp = self.board[h1][from_]
                self.board[h1][from_] = " "
                self.board[h2 - 1][to_] = tmp

            for _ in moves:
                h1, h2 = find_height(self.board, from_, to_)
                if h1 == 0 or h2 == 0:
                    self.board = [[" "] * len(self.board[0])] + self.board
                    h1 += 1
                    h2 += 1
                mv(from_, to_, h1, h2)
            while (list(set(self.board[0])) == [" "]):
                self.board = self.board[1:]
            pass

        def solve(self):
            [self.move(self.instructions[i]) for i in range(len(self.instructions))]
            pass

        def get_answer(self):
            # going from top to bottom, get only the first non-space character or each column
            lst = []
            for j in range(len(self.board[0])):
                for i in range(len(self.board)):
                    if self.board[i][j] != " ":
                        lst.append(self.board[i][j])
                        break
            return "".join(lst)



    b = board(board_list, instructions)
    b.__repr__()
    print(b.get_answer())

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")