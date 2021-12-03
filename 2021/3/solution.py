import os, sys


def sol1(data):
    bin_gama: str = ''
    bin_epsilon: str = ''

    for line in zip(*data):
        if line.count('1') > line.count('0'):
            bin_gama += '1'
            bin_epsilon += '0'
        else:
            bin_gama += '0'
            bin_epsilon += '1'

    return int(bin_gama, 2) * int(bin_epsilon, 2)

def find_o2_rating(data):
    for i in range(len(data[0])):
        if len(data) == 1:
            break

        line = list(zip(*data))[i]

        if line.count('1') >= line.count('0'):
            data = [datum for datum in data if datum[i] == '1']
        else:
            data = [datum for datum in data if datum[i] == '0']
    return data[0]

def find_co2_rating(data):
    for i in range(len(data[0])):
        if len(data) == 1:
            break

        line = list(zip(*data))[i]

        if line.count('0') <= line.count('1'):
            data = [datum for datum in data if datum[i] == '0']
        else:
            data = [datum for datum in data if datum[i] == '1']
    return data[0]

def sol2(data):
    bin_o2 = find_o2_rating(data)
    bin_co2 = find_co2_rating(data)

    return int(bin_o2, 2) * int(bin_co2, 2)




data = [line.strip() for line in open(os.path.join(sys.path[0], "input"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")

ans1 = sol1(data)

print(f"The answer to part 1 is {ans1}")
solution.write(f"The answer to part 1 is {ans1}\n")

ans2 = sol2(data)

print(f"The answer to part 2 is {ans2}")
solution.write(f"The answer to part 2 is {ans2}\n")

solution.close()

