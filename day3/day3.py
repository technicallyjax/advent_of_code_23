# """
#     need func that makes list of any numbers adjacent to symbol (inc diagonally)
#     needs to factor in line above/below
#         create list of current, prev, next lines - done
#     needs to allow for a range of digits - if index+1 = num, increase index etc?
#     find isdigit, find isnot digit??
#     need list of possible symbols? - done
# """

# # func to replace input symbols for easier split
# def replace_symbols(line):
#     all_symbols = ['$', '/', '*', '+', '=', '&', '%', '#', '@', '-']

#     for i in all_symbols:
#         line = str(line).replace(i,"!")
#     return line

# # func to get list of numbers per line
# def get_numbers(line):
#     temp_line = line.replace(".","!")
#     numbers = temp_line.split("!")
#     counter = numbers.count('')
#     while counter > 0:
#         numbers.remove('')
#         counter = numbers.count('')
#     if numbers[-1] == '\n':
#         numbers.remove('\n')
#     return numbers

# def is_adjacent(num,listlines):
#     total = 0
#     num_length = len(num)
#     index1 = listlines[1].find(num)
#     index2 = index1 + num_length
#     if num_length == 1:
#         # check line above/below
#         for item in listlines:
#             for char in item[index1 - 1:index1+1]:
#                 if char == "!":
#                     total += int(num)
#     else:
#         if index1 > 0 and listlines[1][index1 - 1] == "!":
#             total += int(num)
#         elif index2 < len(listlines):
#             if listlines[1][index2] == "!":
#                 total += int(num)
#         else:
#             # check line above/below
#             for item in listlines:
#                 for char in item[index1 - 1:index2+1]:
#                     if char == "!":
#                         total += int(num)
#     return total

# # sample_list = [('1' * 141),'............................................411.....................363..134.........463.775..........................506...................','......429...836..$............../..960........*.............+..........*...=....381.....*........67......426.....=..../...304...............']
# # sample_list = [sample_list[0],replace_symbols(sample_list[1]),replace_symbols(sample_list[2])]
# # sample_nums = get_numbers(sample_list[1])

# # total = 0
# # print(sample_nums)
# # for i in sample_nums:
# #     if is_adjacent(i,sample_list):
# #         print('yep')
# #         total += int(i)
# #     else:
# #         print('nope')
# # print(total)

# with open(r"day3/sample2.txt","r") as day3:
#     lines = day3.readlines()
#     total = 0
#     sum_nums = 0
#     # get lines in list
#     for i in range(len(lines)):
#         current_trio = []
#         if i == 0:
#             line_above = ('.' * len(lines[i]))
#             current_line = replace_symbols(lines[i])
#             line_below = replace_symbols(lines[i+1])
#         elif i == len(lines)-1:
#             line_above = replace_symbols(lines[i-1])
#             current_line = replace_symbols(lines[i])
#             line_below = ('1' * len(lines[i]))
#         else:
#             line_above = replace_symbols(lines[i-1])
#             current_line = replace_symbols(lines[i])
#             line_below = replace_symbols(lines[i+1])
#         current_trio = [line_above,current_line,line_below]
#         nums = get_numbers(current_line)
#         counter = 0
#         for num in nums:
#             sum_nums += int(num)
#             total += is_adjacent(num,current_trio)
#             if is_adjacent(num,current_trio) > 0:
#                 counter += 1
#             print(total)
#         print(f"Line {i + 1} has {counter} rel nums")
#         print(nums)
    
#     print(sum_nums)
#     print(total)
#     print(sum_nums - total)

# # Jen Gori solution
from collections import defaultdict

with open("day3/day3.txt") as f:
    engine_schematic = [line.strip() for line in f.readlines()]

# Construct a list containing a dictionary for each number in the engine schematic.
# Each dictionary contains the number's value, start position, and end position
# (start and end positions are matrix coordinates (i, j))

numbers_in_engine_schematic = []

for i in range(len(engine_schematic)):
    j = 0

    while j < len(engine_schematic[i]):
        if engine_schematic[i][j].isnumeric():
            number = {"value": engine_schematic[i][j], "start_position": (i, j)}

            while j < len(engine_schematic[i]) - 1:
                j += 1
                if engine_schematic[i][j].isnumeric():
                    number["value"] += engine_schematic[i][j]
                    if j == len(engine_schematic[i]) - 1:
                        number["value"] = int(number["value"])
                        number["end_position"] = (i, j - 1)
                        numbers_in_engine_schematic.append(number)
                else:
                    number["value"] = int(number["value"])
                    number["end_position"] = (i, j-1)
                    numbers_in_engine_schematic.append(number)
                    break

        j += 1


#  for each number in the engine schematic, construct an array containing the positions of all the number's neighbours,
# Add this neighbour's array to the dictionary for this number in numbers_in_engine_schematic

for number in numbers_in_engine_schematic:
    neighbours = []

    for x in range(number["start_position"][1]-1, number["end_position"][1]+2):
        if number["start_position"][0]-1 >= 0:
            neighbours.append((number["start_position"][0]-1, x))

    for x in range(number["start_position"][1]-1, number["end_position"][1]+2):
        if number["start_position"][0]+1 < len(engine_schematic):
            neighbours.append((number["start_position"][0]+1, x))

    if number["start_position"][1]-1 >= 0:
        neighbours.append((number["start_position"][0], number["start_position"][1]-1))

    if number["end_position"][1] + 1 < len(engine_schematic[number["start_position"][0]]):
        neighbours.append((number["start_position"][0], number["end_position"][1] + 1))

    number["neighbours"] = neighbours


# For each number in numbers_in_engine_schematic, establish whether it is a part number
# Add this information to the dictionary for this number in numbers_in_engine_schematic
for number in numbers_in_engine_schematic:
    for neighbour in number["neighbours"]:
        # if the neighbour is not a symbol:
        if engine_schematic[neighbour[0]][neighbour[1]].isnumeric() \
                or engine_schematic[neighbour[0]][neighbour[1]] == ".":
            pass
        # if the neighbour is a symbol:
        else:
            number["is_part"] = True
            break
        number["is_part"] = False

# calculate result
result = 0
for number in numbers_in_engine_schematic:
    if number["is_part"]:
        result += number["value"]

print(f"The answer to part 1 is {result}")


# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.

# Construct a dictionary of potential gears
# Each entry in the dictionary has a key which is the position of an '*' in engine_schematic
# and a value, which is an array containing the numbers that * is adjacent to

potential_gears = defaultdict(list)

for number in numbers_in_engine_schematic:
    for neighbour in number["neighbours"]:
        if engine_schematic[neighbour[0]][neighbour[1]] == "*":
            potential_gears[(neighbour[0], neighbour[1])].append(number["value"])

# Establish which of the 'potential gears' are actual gears, i.e. are adjacent to exactly two numbers,
# and put these in an array called 'gears':

gears = {entry: potential_gears[entry] for entry in potential_gears if len(potential_gears[entry]) == 2}

# find the sum of the gear ratios (product of the two numbers the gear is adjacent to)
sum_of_gear_ratios = 0

for gear in gears:
    gear_ratio = gears[gear][0] * gears[gear][1]
    sum_of_gear_ratios += gear_ratio

print(f"The answer to part 2 is {sum_of_gear_ratios}")