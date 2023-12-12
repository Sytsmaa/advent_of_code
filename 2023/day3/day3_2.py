with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()
#End with

numbers = []
symbols = []

for row_index, row in enumerate(input_lines):
    number_start_index = -1

    for col_index, col in enumerate(row):
        #Note since each line ends with a newline we do not need to check if next character is the end
        if col.isdigit() and number_start_index == -1:
            number_start_index = col_index
        elif not col.isdigit():
            if number_start_index != -1:
                numbers.append({"number": row[number_start_index:col_index], "row": row_index, "col_start": number_start_index, "col_end": col_index})
                number_start_index = -1
            #End if

            if col == "*":
                symbols.append({"symbol": col, "row": row_index, "col": col_index})
            #End if
        #End if
    #End for
#End for

for number in numbers:
    for symbol in symbols:
        if symbol["row"] == number["row"]:
            if symbol["col"] + 1 == number["col_start"] or symbol["col"] == number["col_end"]:
                symbol.setdefault("numbers", []).append(number["number"])
                break
            #End if
        elif symbol["row"] - 1 == number["row"]:
            if symbol["col"] >= number["col_start"] - 1 and symbol["col"] < number["col_end"] + 1:
                symbol.setdefault("numbers", []).append(number["number"])
                break
            #End if
        elif symbol["row"] + 1 == number["row"]:
            if symbol["col"] >= number["col_start"] - 1 and symbol["col"] < number["col_end"] + 1:
                symbol.setdefault("numbers", []).append(number["number"])
                break
            #End if
        #End if
    #End for
#End for

total_gear_ratio = 0

for symbol in symbols:
    if "numbers" in symbol and len(symbol["numbers"]) == 2:
        total_gear_ratio += int(symbol["numbers"][0]) * int(symbol["numbers"][1])
    #End if
#End for

print(total_gear_ratio)
