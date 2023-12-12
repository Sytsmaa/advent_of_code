import re

MAX_COLORS = {"red": 12, "green": 13, "blue": 14}

with open("input.txt", "r") as input_file:
    games = input_file.readlines()
#End with

total_game_id = 0

for game in games:
    game_id = int(re.match(r"^Game (?P<game_id>\d+):", game).group("game_id"))

    game_possible = True
    pulls = game[game.index(":") + 2:].split(";")

    for pull in pulls:
        for color in MAX_COLORS.keys():
            color_regex = re.search(r"(?P<color>\d+) " + color, pull)

            if color_regex and int(color_regex.group("color")) > MAX_COLORS[color]:
                game_possible = False
                break
            #End if
        #End for
    #End for

    if game_possible:
        total_game_id += game_id
    #End if
#End for

print(total_game_id)
