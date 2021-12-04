import os, sys
from itertools import zip_longest

def boards_from_text(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    raw_boards = zip_longest(*args, fillvalue=fillvalue)
    return [board_line.split() for board in raw_boards for board_line in board if board_line != '']

def sol1(data):
    announcements = data[0].split(',')
    boards = boards_from_text(data[1:], 6)
    print(boards)



def sol2(data):
    pass


data = [line.strip() for line in open(os.path.join(sys.path[0], "input"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")

ans1 = sol1(data)

ans1_text = f"The answer to part 1 is {ans1}"
print(ans1_text)
solution.write(f"{ans1_text}\n")

ans2 = sol2(data)

ans2_text = f"The answer to part 2 is {ans2}"
print(ans2_text)
solution.write(f"{ans2_text}\n")

solution.close()