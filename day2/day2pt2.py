from day2pt1 import listify

def max_colour(thislist,colour):
    maximum = 0
    for i in range(len(thislist)):
        element = thislist[i]
        current = 0
        if f"{colour}" in element:
            index = element.find(f"{colour}") - 3
            if element[index] == " ":
                index += 1
                current = int(element[index:index+1])
            else:
                current = int(element[index:index+2])
            if current > maximum:
                maximum = current
    return maximum

with open(r"day2/day2.txt", "r") as cube_game:
    sum_powers = 0
    for line in cube_game:
        separated_pulls = listify(line)
        line_power = max_colour(separated_pulls,"red") * max_colour(separated_pulls,"blue") * max_colour(separated_pulls,"green")
        sum_powers += line_power

print(sum_powers)