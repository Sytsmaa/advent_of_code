import re

with open("input.txt", "r") as input_file:
    games = input_file.readlines()
#End with

total_power = 0

for game in games:
    min_colors = {"red": 0, "green": 0, "blue": 0}

    pulls = game[game.index(":") + 2:].split(";")

    for pull in pulls:
        for color in min_colors.keys():
            color_regex = re.search(r"(?P<color>\d+) " + color, pull)

            if color_regex and int(color_regex.group("color")) > min_colors[color]:
                min_colors[color] = int(color_regex.group("color"))
            #End if
        #End for
    #End for

    power = 1

    for color_value in min_colors.values():
        power *= color_value
    #End for

    total_power += power
#End for

print(total_power)
