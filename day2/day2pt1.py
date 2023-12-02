# func to assess 12 red cubes, 13 green cubes, and 14 blue cubes
def listify(text):
    instances = text.split(";")
    return instances

# 12 reds
def poss_reds(thislist):
    possible = True
    for i in range(len(thislist)):
        element = thislist[i]
        if "red" in element:
            index = element.find("red") - 3
            if element[index] != " ":
                num = int(element[index:index+2])
                if num > 12:
                    possible = False
    return possible

def poss_greens(thislist):
    possible = True
    for i in range(len(thislist)):
        element = thislist[i]
        if "green" in element:
            index = element.find("green") - 3
            if element[index] != " ":
                num = int(element[index:index+2])
                if num > 13:
                    possible = False
    return possible

# 14 blues
def poss_blues(thislist):
    possible = True
    for i in range(len(thislist)):
        element = thislist[i]
        if "blue" in element:
            index = element.find("blue") - 3
            if element[index] != " ":
                num = int(element[index:index+2])
                if num > 14:
                    possible = False
    return possible


with open(r"day2/day2.txt", "r") as cube_game:
    sum_nums = 0
    for line in cube_game:
        num_start_i = line.find(" ") + 1
        num_end_i = line.find(":")
        separated_pulls = listify(line)
        print(separated_pulls)
        if poss_reds(separated_pulls):
            if poss_blues(separated_pulls):
                if poss_greens(separated_pulls):
                    sum_nums += int(line[num_start_i:num_end_i])
        print(sum_nums)

print(sum_nums)
