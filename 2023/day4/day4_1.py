import re
import math

with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()
#End with

total_points = 0

for card in input_lines:
    card_regex = re.match(r"^Card\s+\d+:\s+(?P<winning_numbers>(\d+\s+)+)\|(?P<card_numbers>(\s+\d+)+)$", card.strip())
    winning_numbers = card_regex.group("winning_numbers").split()
    card_numbers = card_regex.group("card_numbers").split()

    num_winners = 0

    for card_number in card_numbers:
        if card_number in winning_numbers:
            num_winners += 1
        #End if
    #End for

    #Converting to int we do not need to check for 0 winners
    total_points += int(math.pow(2, num_winners - 1))
#End for

print(total_points)
