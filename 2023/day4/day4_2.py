import re
import math

with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()
#End with

card_counts = {}

for card in input_lines:
    card_regex = re.match(r"^Card\s+(?P<card_id>\d+):\s+(?P<winning_numbers>(\d+\s+)+)\|(?P<card_numbers>(\s+\d+)+)$", card.strip())
    card_id = int(card_regex.group("card_id"))
    winning_numbers = card_regex.group("winning_numbers").split()
    card_numbers = card_regex.group("card_numbers").split()

    card_counts.setdefault(card_id, 0)
    card_counts[card_id] += 1

    for _ in range(card_counts[card_id]):
        num_winners = 0

        for card_number in card_numbers:
            if card_number in winning_numbers:
                num_winners += 1
                card_counts.setdefault(card_id + num_winners, 0)
                card_counts[card_id + num_winners] += 1
            #End if
        #End for
    #End for
#End for

print(sum(card_counts.values()))
