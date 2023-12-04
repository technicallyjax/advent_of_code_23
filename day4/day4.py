# part 1

def winning_nums(text):
    return [int(char) for char in text.split(":")[1].split("|")[0].strip().split(" ") if char != ""]

def possible_nums(text):
    return [int(char) for char in text.split(":")[1].split("|")[1].strip().split(" ") if char != ""]

def find_winners(text):
    winners = winning_nums(text)
    potentials = possible_nums(text)
    total = 0
    for num in winners:
        if num in potentials:
            if total == 0:
                total = 1
            else:
                total = total * 2
    return total

with open(r"day4/day4.txt","r") as cards:
    overall = 0
    for line in cards:
        overall += find_winners(line)
    
    print(overall)

# part 2
def calc_winning_nums(text):
    winners = winning_nums(text)
    potentials = possible_nums(text)
    count = 0
    for num in winners:
        if num in potentials:
            count += 1
    return count

def max_card_num(file):
    with open(file) as f:
        return len(f.readlines())

def total_cards(file):
    max_card_number = max_card_num(file)
    cards_dict = {i + 1: 1 for i in range(max_card_number)}
    card_num = 1
    with open(file) as f:
        for line in f:
            winners = calc_winning_nums(line)
            for n in range(card_num + 1, min(card_num + 1 + winners, max_card_number + 1)):
                cards_dict[n] += cards_dict[card_num]
            card_num += 1
    
    return sum(cards_dict.values())

print(total_cards("day4/day4.txt"))