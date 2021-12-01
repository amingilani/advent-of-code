from itertools import pairwise
import os, sys

data = [int(line.strip()) for line in open(os.path.join(sys.path[0], "input"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")

is_increasing = [pair[1] > pair[0] for pair in pairwise(data)]

answer = is_increasing.count(True)

print(f"The answer to part 1 is {answer}")
solution.write(f"The answer to part 1 is {answer}\n")


def three_window(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a + b + c

is_increasing = [pair[1] > pair[0] for pair in pairwise(three_window(data))]
answer = is_increasing.count(True)

print(f"The answer to part 2 is {answer}")
solution.write(f"The answer to part 2 is {answer}\n")

solution.close()
